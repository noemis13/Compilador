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

		

	def define_variaveis_auxiliares(self):
		self.valores = {}
		self.valoresExpressoes = {}
		self.valoresLeia = {}
		self.valoresRetorno = {}
		self.valoresRepita = {}
		self.valoresStore = {}
		self.escopoVar = []
		self.builder = None
		self.escopo = "global"
		self.escopoRepita = None
		self.funcao = None
		self.var = None
		self.escrevaFlutuante = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), 'escrevaFlutuante')
		self.escrevaInteiro = ir.Function(self.modulo, ir.FunctionType(ir.IntType(32), [ir.IntType(32)]), 'escrevaInteiro')
		
		self.leiaFlutuante = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), []), 'leiaFlutuante')
		self.leiaInteiro = ir.Function(self.modulo, ir.FunctionType(ir.IntType(32), []), 'leiaInteiro')
		

	
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
				
				self.tabelaSimbolos["global" + "-" + var][1] = ir.GlobalVariable(self.modulo, ir.IntType(32), name=var)
				(self.tabelaSimbolos["global" + "-" + var][1]).initializer = ir.Constant(ir.IntType(32), 0)
				(self.tabelaSimbolos["global" + "-" + var][1]).linkage = "common"
				(self.tabelaSimbolos["global" + "-" + var][1]).align = 4			 				
				
			else:
				self.tabelaSimbolos["global" + "-" + var][1] = ir.GlobalVariable(self.modulo, ir.FloatType(), name= var)				
				(self.tabelaSimbolos[self.escopo + "-" + var][1]).initializer = ir.Constant(ir.FloatType(), 0.0)
				(self.tabelaSimbolos[self.escopo + "-" + var][1]).linkage = "common"
				(self.tabelaSimbolos[self.escopo + "-" + var][1]).align = 4	
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

		self.escopo = valorNoFilho


		#parametros
		if len(node.child) == 0:
			parametros = self.lista_parametros(node.child[0].child[0])
			valorParam = self.valor_lista_parametros(node.child[0].child[0])
		else:
			valorParam = self.valor_lista_parametros(node.child[1].child[0])
			parametros = self.lista_parametros(node.child[1].child[0])
		carregaParametro = []
		for i in range(len(parametros)):
			carregaParametro.append(self.tipo_parametros(valorParam[i], parametros[i]))
		
		if len(carregaParametro) > 0:
		
			if tipoFunc == "inteiro":
				self.funcao = ir.Function(self.modulo, ir.FunctionType(ir.IntType(32), ( [carregaParametro[i][0][0] for i in range(0, len(carregaParametro))])), name=nomeFunc)

			elif tipoFunc == "flutuante":
				self.funcao = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), ( [carregaParametro[i][0][0] for i in range(0, len(carregaParametro))])), name=nomeFunc)

			else:
				self.funcao = ir.Function(self.modulo, ir.FunctionType(ir.VoidType(), ( [carregaParametro[i][0][0] for i in range(0, len(carregaParametro))])), name=nomeFunc)

			basicBlock = 	self.funcao.append_basic_block('entry')
			self.builder = ir.IRBuilder(basicBlock)


			for i, v in enumerate(carregaParametro):
				self.funcao.args[i].name = v[0][1]
				escopoParam = self.verifica_escopo(v[0][1])
				self.tabelaSimbolos[escopoParam][1] = self.builder.alloca(v[0][0], name=v[0][1])
				self.builder.store(self.funcao.args[i],self.tabelaSimbolos[escopoParam][1] )
				self.builder.load(self.tabelaSimbolos[escopoParam][1])			

		#declaracao sem parametros
		else:
			if tipoFunc == "inteiro":
				self.funcao = ir.Function(self.modulo, ir.FunctionType(ir.IntType(32), ()), name=nomeFunc)

			elif tipoFunc == "flutuante":
				self.funcao = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), ()), name=nomeFunc)

			else:
				self.funcao = ir.Function(self.modulo, ir.FunctionType(ir.VoidType(), ()), name=nomeFunc)


			basicBlock = self.funcao.append_basic_block('entry')
			self.builder = ir.IRBuilder(basicBlock)
		
		if len(node.child) == 0:
			self.cabecalho(node.child[0])
		else:
			self.cabecalho(node.child[1])
		
		self.escopo = "global"



	def lista_parametros(self, node):
		parametros = []
		if len(node.child) == 1:
			if node.child[0] != None:
				#parametros = "void"
	#		else:
				parametros.append(node.child[0].child[0].value)				
		else:
			parametros = self.lista_parametros(node.child[0])
			parametros.append(node.child[1].child[0].value)
				
		return parametros


	def valor_lista_parametros(self, node):
		valorParam = []
		if len(node.child) == 1:
			if node.child[0] != None:
				#valorParam = "void"
			#else:
				valorParam.append(node.child[0].value)
			
		else:
			valorParam = self.valor_lista_parametros(node.child[0])
			valorParam.append(node.child[1].value)
				
		return valorParam


	def tipo_parametros(self, valorParam, parametros):
		tipo = []
		if parametros == "inteiro":
			conv = ir.IntType(32)
		elif parametros == "flutuante":
			conv = ir.FloatType()
		else:
			conv = ir.VoidType
		tipo.append((conv, valorParam))
		return tipo



	def cabecalho(self, node):
		self.corpo_funcao(node.child[1])
		#return self.lista_parametros(node.child[0])


	def corpo_funcao(self, node):
		ret = []
		if node.child != None:
			if len(node.child) == 1:
				tipoCorpo = "void"
			else:
				self.corpo_funcao(node.child[0])
				return self.acao(node.child[1])
				
			
	
	def acao(self, node):
		if node.child[0].type == "expressao":
			return self.expressao(node.child[0])
		elif node.child[0].type == "declaracao_variaveis":
			return self.declaracao_variaveis(node.child[0])
		elif node.child[0].type == "se":
			return self.verifica_condicional(node.child[0])
		elif node.child[0].type == "leia":
			return self.leia(node.child[0])
		elif node.child[0].type == "escreva":
			return self.escreva(node.child[0])
		elif node.child[0].type == "retorna":
			return self.retorna(node.child[0]) 
		elif node.child[0].type == "repita":
			return self.verifica_repeticao(node.child[0])
			

	def expressao(self, node):
		if node.child[0].type == "atribuicao":
			nomeVar = node.child[0].child[0].value
			var = self.escopo+"-"+nomeVar
			
			return self.expressao_logica(node.child[0].child[1].child[0], nomeVar)
		else:
			return self.expressao_logica(node.child[0], "")
			

	def expressao_logica(self, node, var):
		if node.child[0].type == "expressao_simples":
			return self.expressao_simples(node.child[0], var)

	def expressao_simples(self, node, var):	
		if node.child[0].type == "expressao_aditiva":
			return self.expressao_aditiva(node.child[0], var)
		elif node.child[0].type == "expressao_simples":
			
			valor, tipo =  self.expressao_simples(node.child[0], var)
			valorNum, tipoNum = self.expressao_aditiva(node.child[2], var)
			operadorRelacional = node.child[1].value
			self.valoresExpressoes[valor] = [valorNum, tipoNum, operadorRelacional]
			if self.escopoRepita == "ate":
				ret = []
				ret = [valor, tipo, operadorRelacional, valorNum, tipoNum]
				return ret
			else:
				return valor, tipo			
			

	def expressao_aditiva(self, node, var):
		if node.child[0].type == "expressao_multiplicativa":
			return self.expressao_multiplicativa(node.child[0], var)
		elif node.child[0].type == "expressao_aditiva":
			if len(var) > 0:
				valorExp1, tipo = self.expressao_aditiva(node.child[0], "")
				valorExp2, tipoExp = self.expressao_multiplicativa(node.child[2], "")
				operadorAditivo = node.child[1].value
				
				escopoExp1 = self.verifica_escopo(valorExp1)
									
				expEsquerda = self.builder.load(self.tabelaSimbolos[escopoExp1][1])
				expDireita = ""
				if type(valorExp2) is str:
					escopoExp2 = self.verifica_escopo(valorExp2)
					expDireita = self.builder.load(self.tabelaSimbolos[escopoExp2][1])
				else:
					if tipoExp == "inteiro":
						allocaDireita = self.builder.alloca(ir.IntType(32), name="direta_"+var)
						storeDireita = self.builder.store(ir.Constant(ir.IntType(32), valorExp2), allocaDireita)
					else:
						allocaDireita = self.builder.alloca(ir.FloatType(), name="direta_"+var)
						storeDireita = self.builder.store(ir.Constant(ir.FloatType(), valorExp2), allocaDireita)

					expDireita = self.builder.load(allocaDireita)	
					#calcular expressao		
				resExp = self.calcula_expressao(expEsquerda, operadorAditivo, expDireita, self.tabelaSimbolos[self.verifica_escopo(var)][0])
				#splitResExp = str(resExp).split(" = ")
				
				#self.tabelaSimbolos[self.verifica_escopo(var)][1] = splitResExp[1]
				

				self.valoresRepita[self.verifica_escopo(var)] = [resExp, 0, 0, True, True]						
				self.escopoVar.append(self.verifica_escopo(var))
				
			else:
				valorExp1, tipo = self.expressao_aditiva(node.child[0], var)
				valorExp2, tipoExp = self.expressao_multiplicativa(node.child[2], var)
				operadorAditivo = node.child[1].value
				self.valoresExpressoes[valorExp1] = [valorExp2, tipoExp, operadorAditivo]
				return valorExp1, tipo		





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
		
					s = self.builder.store(ir.Constant(ir.IntType(32), valor), self.tabelaSimbolos[varCompleto][1])
					
					self.valores[varCompleto] = [valor]
					self.valoresStore[varCompleto] =[valor, s] 
			#		return self.builder.load(self.tabelaSimbolos[varCompleto][1])
	
				elif tipo == "flutuante":
					s = self.builder.store(ir.Constant(ir.FloatType(), valor), self.tabelaSimbolos[varCompleto][1])
					self.valores[varCompleto] = [valor]
					self.valoresStore[varCompleto] =[valor, s] 
	
			#		return self.builder.load(self.tabelaSimbolos[varCompleto][1])
				if self.escopoRepita == "repita":
					self.valoresRepita[varCompleto] = [valor, tipo, self.builder.load(self.tabelaSimbolos[varCompleto][1]), False, False]
					self.escopoVar.append(varCompleto)
					
			else:
				return valor, tipo #quando for retorna no codio
				

		elif node.child[0].type == "var":

			valorRecebido = node.child[0].value
			varCompleto = self.verifica_escopo(valorRecebido)
			tipo = self.tabelaSimbolos[varCompleto][3]
			if len(var) != 0:
				escopoVar = self.verifica_escopo(var)
			
				if varCompleto in self.tabelaSimbolos:
					if self.tabelaSimbolos[varCompleto][2]==True:
						if varCompleto in self.valores:
							valor = self.valores[varCompleto][0]
							if tipo == "inteiro":
								l = self.builder.load(self.tabelaSimbolos[varCompleto][1], escopoVar)
								self.builder.store(l, self.tabelaSimbolos[escopoVar][1])
								
							
							else:
								l = self.builder.load(self.tabelaSimbolos[varCompleto][1], escopoVar)
								self.builder.store(l, self.tabelaSimbolos[escopoVar][1])
			#	return self.builder.load(self.tabelaSimbolos[varCompleto][1])
				if self.escopoRepita == "repita":
					self.valoresRepita[varCompleto] = [valor, tipo, self.builder.load(self.tabelaSimbolos[varCompleto][1]), False, False]
					self.escopoVar.append(varCompleto)

			else:
				#retorna
				return valorRecebido, tipo

		elif node.child[0].type == "chamada_funcao":
			nomeFunc = node.child[0].value
			argsFun = self.lista_argumentos(node.child[0].child[0])
			func = self.modulo.get_global(nomeFunc)
			valores = []
			tipo = []
			for i in range(len(argsFun)):
				if argsFun[i][0] != "i":
					escopoArgs = self.verifica_escopo(argsFun[i][0])
					if argsFun[i][1] == "inteiro":
						valores.append(self.int_to_float(self.builder.load(self.tabelaSimbolos[escopoArgs][1])))
					
	
			#chamdaFun = self.builder.call(func, valores)


			for i in range(len(argsFun)):
				if argsFun[i][1] == "inteiro":
					valores[i] = self.builder.fptosi(valores[i], ir.IntType(32))
			chamadaFun = self.builder.call(func, valores)	
			return chamadaFun
			
			
	
	def lista_argumentos(self, node):
		args = []
		if len(node.child) == 1:
			args = self.expressao(node.child[0])
			return args
		else:
			args = []
			args.append(self.lista_argumentos(node.child[0]))
			args.append(self.expressao(node.child[1]))
			return args


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

#print(self.tabelaSimbolos[escopoValor][1])
		

	def retorna(self, node):
		expRetorna, tipo = self.expressao(node.child[0])
		if type(expRetorna) is str:
			#verificar se o retorno foi inicializado
			escopoExp = self.verifica_escopo(expRetorna)
			if self.tabelaSimbolos[escopoExp][2] == False:
				if escopoExp in self.valoresLeia:
					expRetorna1 = self.builder.load(self.tabelaSimbolos[escopoExp][1])
				elif escopoExp in self.valores:
							
					expRetorna1 = (self.builder.load(self.tabelaSimbolos[escopoExp][1]))
					#expRetorna1 = self.retorno_numero(self.valores[escopoExp], tipo)
				else:
					#retorna 0 
					expRetorna1 = self.retorno_numero(0, tipo)
				
			else:
				expRetorna1 = self.retorno_var(expRetorna, tipo)
		
		else:
			expRetorna1 = self.retorno_numero(expRetorna, tipo)
			
		#verificar se retorna expressao soma	
		if expRetorna in self.valoresExpressoes: 
			escopoExp = self.verifica_escopo(expRetorna)
			valor = self.valoresExpressoes[expRetorna][0]
			if type(valor) is str:
				if self.tabelaSimbolos[escopoExp][2] == False:				#retorna 0
					if escopoExp in self.valoresLeia:
						expRetorna2 = self.builder.load(self.tabelaSimbolos[escopoExp][1])
					else: 
						expRetorna2 = self.retorno_numero(0, tipo)
				else:			
					expRetorna2 = self.retorno_var(expRetorna, tipo)
			else:
				expRetorna2 = self.retorno_numero	(expRetorna, tipo)
			#operacao
			if self.valoresExpressoes[expRetorna][2] == "+":
				if tipo == "inteiro" and self.valoresExpressoes[expRetorna][1] == "inteiro":
					soma = self.builder.add(expRetorna2, expRetorna1, name="retornoSoma", flags=())
				self.builder.ret(soma)
						
		else:
			self.builder.ret(expRetorna1)


	def retorno_var(self, expRetorna, tipo):
#		nomeEscopo = self.escopo+"-"+expRetorna
#		if nomeEscopo not in self.valores:
#			nomeEscopo = "global-"+expRetorna

		nomeEscopo = self.verifica_escopo(expRetorna)
		
		if tipo == "inteiro":
			retorno = self.builder.alloca(ir.IntType(32), name='retorno')
			if nomeEscopo not in self.valores:
				expRetorna1 = (self.builder.load(self.tabelaSimbolos[nomeEscopo][1]))
				
			else:
				self.builder.store(ir.Constant(ir.IntType(32), self.valores[nomeEscopo][0]), retorno)
				expRetorna1 = self.builder.load(retorno, name='', align=4)
		elif tipo == "flutuante":
			retorno = self.builder.alloca(ir.FloatType(), name='retorno')
			self.builder.store(ir.Constant(ir.FloatType(), self.valores[nomeEscopo][0]), retorno)
			expRetorna1 = self.builder.load(retorno, name='', align=4)
		return expRetorna1	

	def retorno_numero(self, expRetorna, tipo):
		if tipo == "inteiro":
			expRetorna1 = ir.Constant(ir.IntType(32), expRetorna)
		elif tipo == "flutuante":
			expRetorna1 = ir.Constant(ir.FloatType(), expRetorna)
		return expRetorna1




	def verifica_condicional(self, node):
		expressao, tipo = self.expressao(node.child[0])
		escopoVar = self.verifica_escopo(expressao)
	
		if node.child[1].child[1].child[0].type == "expressao":
			varCorpoSe = node.child[1].child[1].child[0].child[0].child[0].value
			expressaoCorpoSe = self.expressao(node.child[1].child[1].child[0].child[0].child[1])
			escopoVarCorpoSe = self.verifica_escopo(varCorpoSe)
			self.monta_condicional(node, expressao, tipo, escopoVar, varCorpoSe, expressaoCorpoSe, escopoVarCorpoSe)

		if node.child[1].child[1].child[0].type == "se":
			
			self.verifica_condicional(node.child[1].child[1].child[0])


	def monta_condicional(self,node,  expressao, tipo, escopoVar, varCorpoSe, expressaoCorpoSe, escopoVarCorpoSe):
		
		blocoEntao = self.funcao.append_basic_block(name='entao')
		if len(node.child) ==3:
			blocoSenao = self.builder.append_basic_block('senao')

		blocoFim = self.funcao.append_basic_block(name='fim')
		
		if escopoVar in self.tabelaSimbolos:
			var_comp = self.builder.load(self.tabelaSimbolos[escopoVar][1], expressao+"_cmp", align=4)
			op = self.valoresExpressoes[expressao][2]
			valor_comp = self.valoresExpressoes[expressao][0]
			

			tipoValorComp = self.verifica_tipo(valor_comp)
			if tipoValorComp == "inteiro":
				comparaSe = self.builder.icmp_signed(op, var_comp, ir.Constant(ir.IntType(32), valor_comp), name="se_"+expressao)
				if len(node.child) == 3:
					self.builder.cbranch(comparaSe, blocoEntao, blocoSenao)
				else:
					self.builder.cbranch(comparaSe, blocoEntao, blocoFim)	
				self.builder.position_at_end(blocoEntao)
				self.builder.store(ir.Constant(ir.IntType(32), expressaoCorpoSe[0]), self.tabelaSimbolos[escopoVarCorpoSe][1])				
				self.valores[escopoVarCorpoSe] = expressaoCorpoSe[0]
				
				self.builder.branch(blocoFim)
				
				if len(node.child) ==3:
					varCorpoSenao = node.child[2].child[1].child[0].child[0].child[0].value
					expressaoCorpoSenao = self.expressao(node.child[2].child[1].child[0].child[0].child[1])
					escopoVarCorpoSenao = self.verifica_escopo(varCorpoSenao)
					
					self.builder.position_at_end(blocoSenao)
					self.builder.store(ir.Constant(ir.IntType(32), expressaoCorpoSenao[0]), self.tabelaSimbolos[escopoVarCorpoSenao][1])
					self.valores[escopoVarCorpoSenao] = expressaoCorpoSenao[0]
				
					self.builder.branch(blocoFim)
				self.builder.position_at_end(blocoFim)
		


	def float_to_int(self, num):
		return self.builder.fptosi(num, ir.IntType(32))

	def int_to_float(self, num):
		return self.builder.sitofp(num, ir.FloatType())



	def leia(self, node):
		valor = self.builder.call(self.leiaFlutuante, [], "leiaFlutuante")
		escopoNode = self.verifica_escopo(node.value)
		self.valoresLeia[escopoNode]=[True]
		
		if escopoNode in self.tabelaSimbolos:
			tipoNode = self.tabelaSimbolos[escopoNode][3]

			if tipoNode == "inteiro":
				self.builder.store(self.float_to_int(valor), self.tabelaSimbolos[escopoNode][1])
				return self.builder.load(self.tabelaSimbolos[escopoNode][1])
			elif tipoNode == "flutuante":
				self.builder.store(valor, self.tabelaSimbolos[escopoNode][1])
				return self.builder.load(self.tabelaSimbolos[escopoNode][1])



	def escreva(self, node):
		valor, tipo = self.expressao(node.child[0])
		escopoValor = self.verifica_escopo(valor)
		if tipo == "inteiro":
			valorExp = self.int_to_float(self.builder.load(self.tabelaSimbolos[escopoValor][1]))
			return self.builder.call(self.escrevaFlutuante, [valorExp])

		elif tipo == "flutuante":
			valorExp = self.builder.load(self.tabelaSimbolos[escopoValor])
			valorExp = self.float_to_int(valorExp)
			return self.builder.call(self.escrevaFlutuante, [valorExp])

		
		elif tipo == "flutuante":
			if self.tabelaSimbolos[escopoValor][2] == False:
				if escopoValor in self.valores:
					valorExp = self.int_to_float( ir.Constant(ir.IntType(32), self.valores[escopoValor]))
			else:

				valorExp = self.builder.load(self.tabelaSimbolos[escopoValor])
				valorExp = self.float_to_int(valorExp)

			return self.builder.call(self.escrevaFlutuante, [valorExp])		


	def calcula_expressao(self, expEsquerda, operador, expDireita, var):
		if operador == "+":
			return self.builder.add(expEsquerda, expDireita, name="add_"+var, flags=())
		
		elif operador == "-":
			return self.builder.sub(expEsquerda, expDireita, name="sub_"+var, flags=())

		elif operador == "*":
			return self.builder.mul(expEsquerda, expDireita, name="mul_"+var, flags=())
		
		else:
			return self.builder.mul(expEsquerda, expDireita, name="div_"+var, flags=())
		
		#return expressao


	def verifica_repeticao(self, node):
		self.escopoRepita = "repita"

		self.phi = True

		blocoRepita = self.builder.append_basic_block('repita')
		blocoFim = self.builder.append_basic_block('fim')
		self.builder.branch(blocoRepita)
		self.builder.position_at_end(blocoRepita)

		self.corpo_funcao(node.child[0])
		condParada = ""
		if node.child[1].type == "ate":
			self.escopoRepita = "ate"
			condParada = (self.expressao(node.child[1].child[0]))
				
		self.escopoRepita = None
		blocoRepita = self.builder.basic_block
		self.phi = True
		self.phi2 = True

		escopoCondParada = self.verifica_escopo(condParada[0])
		varComp = self.builder.load(self.tabelaSimbolos[escopoCondParada][1], condParada[0]+"_cmp", align=4)
		condicao = ""		
		if condParada[2] == "=":
			if(condParada[4] == "inteiro"):
				condicao = self.builder.icmp_signed('==', varComp, ir.Constant(ir.IntType(32), condParada[3]), name = 'Igualdade')
			elif condParada[4] == "flutuante":
				condicao = self.builder.icmp_signed('==', varComp, ir.Constant(ir.FloatType(), condParada[3]), name = 'Igualdade')
			
		self.builder.cbranch(condicao, blocoRepita, blocoFim)
		self.builder.position_at_end(blocoFim)
		self.phi = True
		self.phi2 = True
		
		loadValor  = []
		for i in range(0, len(self.valoresRepita)):
			escopoValor = self.escopoVar[i]
			if self.valoresRepita[self.escopoVar[i]][3] == False:				
				loadValor = self.valoresRepita[self.escopoVar[i]][2]
				
				if self.valoresRepita[self.escopoVar[i]][1] == "inteiro":
					phi = self.builder.phi(ir.IntType(32), 'repitaTemp')
				else:
					phi = self.builder.phi(ir.FloatType(), 'repitaTemp')

				phi.add_incoming(loadValor, blocoRepita)
				
			elif self.valoresRepita[self.escopoVar[i]][3] != False:			
				phi2 = self.builder.phi(ir.IntType(32), 'repitaTemp2') 
				#else:
				#	phi2 = self.builder.phi(ir.FloatType(), 'repitaTemp2')		
				phi2.add_incoming(self.valoresRepita[self.escopoVar[i]][0], blocoRepita)	
				
						
				
				
		self.phi = False
		self.phi2 = False
			

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
