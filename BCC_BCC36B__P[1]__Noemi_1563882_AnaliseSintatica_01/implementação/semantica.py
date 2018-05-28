from syntax import Syntax
from ply import yacc
import pprint


class Semantica:
    def __init__(self, code):
        self.simbolos = {}
        self.escopo = "global"
        self.tree = Syntax(code).ast
        self.programa(self.tree)
        #self.check_main(self.simbolos)
        #self.check_utilizadas(self.simbolos)
        #self.check_functions(self.simbolos)
    
    def raiz(self):
        if(self.tree.type == "programa_principal"):
            self.scope = "principal"
            self.principal(self.tree.child[0])
            self.scope = "global"
    
    def programa(self, node):
        self.lista_declaracoes(node.child[0])

    def lista_declaracoes(self, node):
        if (len(node.child) == 1):
            self.declaracao(node.child[0])
        else:
            if(node.child[0] != None):
            	self.lista_declaracoes(node.child[0])
            self.declaracao(node.child[1])

    def declaracao(self, node):
        print("entrou")
        #if (node.child[0].type == "declaracao_variaveis"):
            #self.declaracao_variaveis(node.child[0])
        #    print("declaracao variaveis") 
        #elif (node.child[0].type == "inicializacao_variaveis"):
            #self.inicializacao_variaveis(node.child[0])
        #    print("inicializacao")
        #else:
         #   if (len(node.child[0].child) == 1):
         #       self.escopo = node.child[0].child[0].value
         #   else:
          #      self.escopo = node.child[0].child[1].value

            #self.declaracao_funcao(node.child[0])
          #  print("declaracao funcao")
          #  self.escopo = "global"

              
        

if __name__ == '__main__':
    import sys, io
    code = io.open(sys.argv[1], mode="r", encoding="utf-8")
    s = Semantica(code.read())
    pprint.pprint(s.simbolos, depth=3, width=300)
