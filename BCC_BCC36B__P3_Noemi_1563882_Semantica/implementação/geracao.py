from llvmlite import ir
from semantica import *

class Geracao():
	def __init__(self, code, optz=True, debug=True):
		s = Semantica(code.read())
		self.tree = s.tree
		self.tabelaSimbolos = s.tabelaSimbolos
		self.cria_modulo()
		self.le_arvore(self.tree)

	def cria_modulo(self):
		self.modulo = ir.Module("ModuloLLVMLITE")
		self.printf = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), "printf_f")
		#self.scanf = ir.Function(self.modulo, ir.FunctionType(ir.FloatType(), [ir.FloatType()]), "scanf_f")
		#print(str(self.modulo))

	def le_arvore(self, node):
		print(node)
		
		

if __name__ == '__main__':
	import sys, io
	code = io.open(sys.argv[1], mode="r", encoding="utf-8")
	gen = Geracao(code)
