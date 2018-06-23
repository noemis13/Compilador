from llvmlite import ir
from semantica import *
import io

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
		self.printf = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), "printf_f")
		self.scanf = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), "scanf_f")
		

	def define_variaveis_auxiliares(self):
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
			print("fazer declaracao funcao")
		

	def declaracao_variaveis(self, node):
		var = node.child[1].child[0].value
		if self.escopo == "global":
			if self.tabelaSimbolos["global" + "-" + var][3]=="inteiro":
				self.tabelaSimbolos["global" + "-" + var][1] = ir.GlobalVariable(self.modulo, ir.IntType(32), "global-" + var)
			else:
				self.tabelaSimbolos["global" + "-" + var][1] = ir.GlobalVariable(self.modulo, ir.FloatType(), "global-" + var)					
		else:
			if self.tabelaSimbolos[self.escopo + "-" + var][3] == "inteiro":
				self.tabelaSimbolos[self.escopo + "-" + var][1] = self.builder.alloca(ir.IntType(32), self.escopo + "-" + var)

			else:
				self.tabelaSimbolos[self.escopo + "-" + var][3] = self.builder.alloca(ir.FloatType(), self.escopo + "-" + var)
		print(self.tabelaSimbolos)




	def salva_arquivo(self):
		arquivo = open('geracaoCodigo.ll', 'w')
		arquivo.write(str(self.modulo))
		arquivo.close()	
		print(self.modulo)
		

if __name__ == '__main__':
	import sys
	code = io.open(sys.argv[1], mode="r", encoding="utf-8")
	gen = Geracao(code)
