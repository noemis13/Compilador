from ast import AST
from ply import yacc
from lexer import tokens


def __init__(self, type_node, child=[], value=None):
        self.type = type_node
        self.child = child
        self.value = value

    def __str__(self, level = 0):
        ret = "| "*level + repr(self.type)+"\n"
        for child in self.child:
#            print("Passou \n")
#            contador = contador + 1
            ret += child.__str__(level + 1)
	return ret

