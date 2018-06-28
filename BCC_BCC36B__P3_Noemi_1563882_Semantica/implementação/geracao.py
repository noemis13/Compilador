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
		self.modulo = ir.Module("ModuloLLVMLITE.bc")

		self.escrevaFlutuante = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), 'escrevaFlutuante')
		self.escrevaInteiro = ir.Function(self.modulo, ir.FunctionType(ir.IntType(32), [ir.IntType(32)]), 'escrevaInteiro')

		self.leiaFlutuante = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), []), 'leiaFlutuante')
		self.leiaInteiro = ir.Function(self.modulo, ir.FunctionType(ir.IntType(32), []), 'leiaInteiro')
		
		

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
		
		elif node.child[0].type == "inicializacao_variaveis":
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
		
		if len(node.child) == 0:
			self.cabecalho(node.child[0])

		else:
			self.cabecalho(node.child[1])
			
		#self.corpo_funcao(node.child[1].child[1].child[0])

		#self.builder.ret_void()
		self.escopo = "global"

	def cabecalho(self, node):
		self.corpo_funcao(node.child[1])		


				
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
			self.retorna(node.child[0])        		

	def expressao(self, node):
		if node.child[0].type == "atribuicao":
			nomeVar = node.child[0].child[0].value
			var = self.escopo+"-"+nomeVar
			
			self.expressao_logica(node.child[0].child[1].child[0], nomeVar)
		else:
			return self.expressao_logica(node.child[0], "")
			

	def expressao_logica(self, node, var):
		if node.child[0].type == "expressao_simples":
			return self.expressao_simples(node.child[0], var)

	def expressao_simples(self, node, var):
		if node.child[0].type == "expressao_aditiva":
			return self.expressao_aditiva(node.child[0], var)
	

	def expressao_aditiva(self, node, var):
		if node.child[0].type == "expressao_multiplicativa":
			return self.expressao_multiplicativa(node.child[0], var)

	def expressao_multiplicativa(self, node, var):
		if node.child[0].type == "expressao_unaria": #vai para fator
			return self.fator(node.child[0].child[0], var)
			

	def fator(self, node, var):
		if node.child[0].type == "numero":
			valor = node.child[0].value
			tipo= self.verifica_tipo(valor)
			varCompleto = self.verifica_escopo(var)
			if len(var) != 0:			
				if tipo == "inteiro":
					self.builder.store(ir.Constant(ir.IntType(32), valor), self.tabelaSimbolos[varCompleto][1])
					self.valores[varCompleto] = [valor]
				
				elif tipo == "flutuante":
					self.builder.store(ir.Constant(ir.FloatType(), valor), self.tabelaSimbolos[varCompleto][1])
					self.valores[varCompleto] = [valor]
			else:
				return valor, tipo #quando for retorna no codio


		elif node.child[0].type == "var":
			valorRecebido = node.child[0].value
			escopoVar = self.verifica_escopo(var)
			
			varCompleto = self.verifica_escopo(valorRecebido)
			tipo = self.tabelaSimbolos[varCompleto][3]
			if varCompleto in self.tabelaSimbolos:
				if self.tabelaSimbolos[varCompleto][2]==True:

					if varCompleto in self.valores:
						valor = self.valores[varCompleto][0]
						if tipo == "inteiro":
							#self.int_to_float(self.builder.load(self.tabelaSimbolos[varCompleto][1], escopoVar))
							
							#self.builder.store(ir.Constant(ir.IntType(32), int(valor)), self.tabelaSimbolos[escopoVar][1])
							l = self.builder.load(self.tabelaSimbolos[varCompleto][1], escopoVar)
							
							self.builder.store(l, self.tabelaSimbolos[escopoVar][1])
		 	
						else:
							self.builder.load(self.tabelaSimbolos[varCompleto][1])		


	def verifica_escopo(self, var):
		varCompleto = self.escopo+"-"+var
		if varCompleto not in self.tabelaSimbolos:
			varCompleto = "global"+"-"+var
		return varCompleto
		
	def verifica_tipo(self, valor):
		if "." in repr(valor):
			tipo = "flutuante"
		else:
			tipo ="inteiro"
		return tipo


	def float_to_int(self, num):
		return self.builder.fptosi(num, ir.IntType(32))

	def int_to_float(self, num):
		return self.builder.sitofp(num, ir.FloatType())



	def retorna(self, node):
		expRetorna, tipo = self.expressao(node.child[0])
		if tipo == "inteiro":
			expRetorna = ir.Constant(ir.IntType(32), expRetorna)
		elif tipo == "flutuante":
			expRetorna = ir.Constant(ir.FloatType(), expRetorna)

		self.builder.ret(expRetorna)





	def salva_arquivo(self):
		arquivo = open('gera.ll', 'w')
		arquivo.write(str(self.modulo))
		arquivo.close()
		print(self.modulo)
		call("./llc gera.ll --mtriple \"x86_64-unknown-linux-gnu\"", shell=True)
		call("gcc -c gera.s", shell=True)
		call("gcc -o saidaGeracao gera.o print_scanf.o", shell=True)
		call("./saidaGeracao", shell=True)

		

if __name__ == '__main__':
	import sys
	code = io.open(sys.argv[1], mode="r", encoding="utf-8")
	gen = Geracao(code) 
