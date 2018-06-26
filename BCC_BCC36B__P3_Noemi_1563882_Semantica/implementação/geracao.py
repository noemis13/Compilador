#!/usr/bin/env python
# -*- coding: utf-8 -*

from llvmlite import ir
from semantica import *
import io
from subprocess import call

class Geracao():
	def __init__(self, code, optz=True, debug=True):
		s = Semantica(code.read())
		self.tree = s.tree
		self.tabelaSimbolos = s.tabelaSimbolos
		self.cria_modulo()
		self.define_variaveis_auxiliares()
		self.geracao_codigo(self.tree)
		self.salva_arquivo()

	def cria_modulo(self):
		self.modulo = ir.Module("ModuloLLVMLITE")
		

	def define_variaveis_auxiliares(self):
		self.valores = {}
		self.builder = None
		self.escopo = "global"
		self.funcao = None
		self.var = None

	
	def geracao_codigo(self, node):
		if node.child[0].type == "lista_declaracoes":
			self.lista_declaracoes(node.child[0])



	def lista_declaracoes(self, node):
		if len(node.child) == 1:
			self.declaracao(node.child[0])
		else:
			self.lista_declaracoes(node.child[0])
			self.declaracao(node.child[1])


	def declaracao(self, node):
		if node.child[0].type == "declaracao_variaveis":
			self.declaracao_variaveis(node.child[0])
		elif node.child[0].type == "declaracao_funcao":
			tamNoFilho = len(node.child[0].child)
			if  tamNoFilho != 1:
				valorNoFilho = node.child[0].child[1].value 
			else:
				valorNoFilho = node.child[0].child[0].value
			self.declaracao_funcao(node.child[0], valorNoFilho)
		elif node.child[0].type == "inicializacao_varuiaveis":
			print("fazer unicialização")
		

	def declaracao_variaveis(self, node):
		var = node.child[1].child[0].value
		if self.escopo == "global":
			if self.tabelaSimbolos["global" + "-" + var][3]=="inteiro":
				self.tabelaSimbolos["global" + "-" + var][1] = ir.GlobalVariable(self.modulo, ir.IntType(32), name="global-" + var)
			else:
				self.tabelaSimbolos["global" + "-" + var][1] = ir.GlobalVariable(self.modulo, ir.FloatType(), name="global-" + var)					
		else:
			if self.tabelaSimbolos[self.escopo + "-" + var][3] == "inteiro":
				self.tabelaSimbolos[self.escopo + "-" + var][1] = self.builder.alloca(ir.IntType(32), name = self.escopo + "-" + var)

			else:
				self.tabelaSimbolos[self.escopo + "-" + var][3] = self.builder.alloca(ir.FloatType(), name= self.escopo + "-" + var)
		
		


	def declaracao_funcao(self, node, valorNoFilho):
		tipoFunc = node.child[0].value
		nomeFunc = valorNoFilho
		if valorNoFilho == "principal":
			nomeFunc = "main"

		if tipoFunc == "inteiro":
			self.funcao = ir.Function(self.modulo, ir.FunctionType(ir.IntType(32), ()), name=nomeFunc)
		elif tipoFunc == "flutuante":
			self.funcao = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), ()), name=nomeFunc)
		else:
			self.funcao = ir.Function(self.modulo, ir.FunctionType(ir.VoidType(), ()), name=nomeFunc)

		basicBlock = self.funcao.append_basic_block('entry')
		self.builder = ir.IRBuilder(basicBlock)
		self.escopo = valorNoFilho

		self.corpo_funcao(node.child[1].child[1].child[0])	
		#self.builder.ret_void()
		self.escopo = "global"

				
	def corpo_funcao(self, node):
		if len(node.child) != 1:
			self.corpo_funcao(node.child[0])
			tipoCorpo = self.acao(node.child[1])
			
	
	def acao(self, node):
		if node.child[0].type == "expressao":
			self.expressao(node.child[0])
		elif node.child[0].type == "declaracao_variaveis":
			self.declaracao_variaveis(node.child[0])
		elif node.child[0].type == "retorna":
        		print("rrrrreeeeeeeeeetorna \n")
        
	def expressao(self, node):
		nomeVar = node.child[0].child[0].value 
		var = self.escopo+"-"+nomeVar
		self.expressao_logica(node.child[0].child[1], nomeVar)		

	def expressao_logica(self, node, var):
		if node.child[0].child[0].type == "expressao_simples":
			self.expressao_simples(node.child[0].child[0], var)

	def expressao_simples(self, node, var):
		if node.child[0].type == "expressao_aditiva":
			self.expressao_aditiva(node.child[0], var)
	

	def expressao_aditiva(self, node, var):
		if node.child[0].type == "expressao_multiplicativa":
			self.expressao_multiplicativa(node.child[0], var)

	def expressao_multiplicativa(self, node, var):
		if node.child[0].type == "expressao_unaria": #vai para fator
			self.fator(node.child[0].child[0], var)
			

	def fator(self, node, var):
		if node.child[0].type == "numero":
			valor = node.child[0].value			
			tipo, varCompleto = self.verifica_tipo(var)
			if tipo == "inteiro":
				self.builder.store(ir.Constant(ir.IntType(32), valor), self.tabelaSimbolos[varCompleto][1])
				self.valores[varCompleto] = [valor]

				
			elif tipo == "flutuante":
				self.builder.store(ir.Constant(ir.FloatType(), valor), self.tabelaSimbolos[varCompleto][1])
				self.valores[varCompleto] = [valor]

		elif node.child[0].type == "var":
			tipoVar, escopoVar = self.verifica_tipo(var)
			valorRecebido = node.child[0].value
			tipo, varCompleto = self.verifica_tipo(valorRecebido)
			if varCompleto in self.tabelaSimbolos:
				if self.tabelaSimbolos[varCompleto][2]==True:
					#v = self.builder.load(self.tabelaSimbolos[varCompleto][1], "")
					if varCompleto in self.valores:
						valor = self.valores[varCompleto][0]
						if tipo == "inteiro":
							self.builder.store(ir.Constant(ir.IntType(32), valor), self.tabelaSimbolos[escopoVar][1])
						elif tipo == "flutuante":
							self.builder.store(ir.Constant(ir.FloatType, valor), self.tabelaSimbolos[escopoVar][1])
		
	
	
	def verifica_tipo(self, var):
		varCompleto = self.escopo+"-"+var
		if varCompleto not in self.tabelaSimbolos:
			varCompleto = "global"+"-"+var
		tipo = self.tabelaSimbolos[varCompleto][3]
		return tipo, varCompleto
		

	def salva_arquivo(self):
		arquivo = open('geracaoCodigo.ll', 'w')
		arquivo.write(str(self.modulo))
		arquivo.close()
		print(self.modulo)
		#call("llc geracaoCodigo.ll --mtriple \"x86_64-unknown-linux-gnu\"", shell=True)
		#call("gcc -c geracaoCodigo.s", shell=True)
		#call("gcc -o saidaGeracao geracaoCodigo.o print_scanf.o", shell=True)
		#call("./saidaGeracao", shell=True)

		

if __name__ == '__main__':
	import sys
	code = io.open(sys.argv[1], mode="r", encoding="utf-8")
	gen = Geracao(code) 
