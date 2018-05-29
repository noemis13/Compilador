from syntax import Syntax
from ply import yacc
import pprint


class Semantica:
    def __init__(self, code):
        self.simbolos = {}
        self.escopo = "global"
        self.tree = Syntax(code).ast
        self.programa(self.tree)
#        self.check_main(self.simbolos)
        #self.check_utilizadas(self.simbolos)
        #self.check_functions(self.simbolos)
    
    def raiz(self):
        if(self.tree.type == "programa_principal"):
            self.scope = "principal"
            self.principal(self.tree.child[0])
            self.scope = "global"
        if(self.tree.type == "programa_funcao"):
            self.func_loop(self.tree.child[0])
            self.principal(self.tree.child[1])
        if(self.tree.type == "programa_varglobal"):
            self.declara_var(self.tree.child[0])
            self.programa(self.tree.child[1])

    
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
        if (node.child[0].type == "declaracao_variaveis"):
            self.declaracao_variaveis(node.child[0])
        elif (node.child[0].type == "inicializacao_variaveis"):
            self.inicializacao_variaveis(node.child[0])
        #else:
        #    if (len(node.child[0].child) == 1):
        #        self.escopo = node.child[0].child[0].value
        #    else:
        #        self.escopo = node.child[0].child[1].value

         #   self.declaracao_funcao(node.child[0])
         #   self.escopo = "global"



    #declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis
    def declaracao_variaveis(self, node):
        self.lista_variaveis(node.child[1])
        return "void"



    def lista_variaveis(self, node):
        ret_args = []
        
        if (len(node.child) == 1):
            if (len(node.child[0].child) == 1):
                self.indice(node.child[0].child[0])
                #ret_args.append(node.child[0].value + self.indice(node.child[0].child[0]))
              
            #else:
            #    ret_args.append(node.child[0].value)
            #return ret_args
        #else:
         #   ret_args = self.lista_variaveis(node.child[0])
          #  if (len(node.child[1].child) == 1):
           #     ret_args.append(node.child[1].value + self.indice(node.child[1].child[0]))
            #else:
            #    ret_args.append(node.child[1].value)
            #return ret_args 


    def var(self, node):
        nome = self.escopo + "-" + node.value
        if (len(node.child) == 1):
            if (nome not in self.simbolos):
                nome = "global-" + node.value
                if (nome not in self.simbolos):
                    print("Erro: A váriavel '" + node.value + "' não foi declarada")
                    exit(1)

            if (self.simbolos[nome][3] == False):
                print("Erro: váriavel '" + nome + "' não foi inicializada")
                #				exit(1)
            var = self.indice(node.child[0])
            self.simbolos[nome][4] = self.simbolos[nome][4] + var
            self.simbolos[nome][2] = True
            return self.simbolos[nome][4]

        else:
            if (nome not in self.simbolos):
                nome = "global-" + node.value
                if (nome not in self.simbolos):
                    print("Erro: A váriavel '" + node.value + "' não foi declarada")
                    exit(1)
            if (self.simbolos[nome][3] == False):
                print("Erro: A váriavel '" + nome + "' não foi inicializada.")
                exit(1)

            self.simbolos[nome][2] = True
            return self.simbolos[nome][4]



    def indice(self, node):
        if (len(node.child) == 1):
            tipo = self.expressao(node.child[0])
            print(tipo)  
        #    if (node.child[0].value == "" or tipo != "inteiro"):
        #        print("Erro: index invalido, permitido somente inteiro")
        #    return ("[]")
        #else:
        #    variavel = self.indice(node.child[0])
        #    tipo = self.expressao(node.child[1])
        #    if (tipo != "inteiro"):
        #        print("Erro: index invalido, permitido sómente inteiro")
                #				exit(1)
        #    return ("[]" + variavel)
 

    def expressao(self, node):
        if (node.child[0].type == "expressao_logica"):
           return self.expressao_logica(node.child[0])
        else:
            #return self.atribuicao(node.child[0])
            print("atribuicao")

    def expressao_logica(self, node):
        if (len(node.child)==1):
            return self.expressao_simples(node.child[0])
        else:
            print("else")
            tipo1 = self.expressao_logica(node.child[0])
            self.operador_logico(node.child[1])
            return "logico"

    def expressao_simples(self, node):
        if len(node.child) == 1:
            return self.expressao_aditiva(node.child[0])
        else:
            tipo1 = self.expressao_simples(node.child[0])
            self.operador_relacional(node.child[1])
            tipo2 = self.expressao_aditiva(node.child[2])
            if (tipo1 != tipo2):
                print("Warning: Operação com tipos diferentes '" + tipo1 + "' e '" + tipo2)
            return "simples"


    def expressao_aditiva(self, node):
        if (len(node.child) == 1):
            return self.expressao_multiplicativa(node.child[0])
        else:
            tipo1 = self.expressao_aditiva(node.child[0])
            self.operador_soma(node.child[1])
            tipo2 = self.expressao_multiplicativa(node.child[2])

            if (tipo1 != tipo2):
                print("Warning: Operação com tipos diferentes '" + tipo1 + "' e '" + tipo2)
            if ((tipo1 == "flutuante") or (tipo2 == "flutuante")):
                return "flutuante"
            else:
                return "inteiro"

    def expressao_multiplicativa(self, node):
        if (len(node.child) == 1):
            return self.expressao_unaria(node.child[0])
        else:
            tipo1 = self.expressao_multiplicativa(node.child[0])
            self.operador_multiplicacao(node.child[1])
            tipo2 = self.expressao_unaria(node.child[2])
            if (tipo1 != tipo2):
                print("Warning: Operação com tipos diferentes '" + tipo1 + "' e '" + tipo2)
            if ((tipo1 == "flutuante") or (tipo2 == "flutuante")):
                return "flutuante"
            else:
                return "inteiro"

    def expressao_unaria(self, node):
        if (len(node.child) == 1):
            return self.fator(node.child[0])
        else:
            if(node.child[0].type == "operador_soma"):
                self.operador_soma(node.child[0])
                print("operador_soma")
            else:
               self.operador_negacao(node.child[0])  
            return self.fator(node.child[1])
 
    def operador_logico(self, node):
        return None


    def operador_relacional(self, node):
        return None

    def operador_soma(self, node):
        return None

    def operador_begacao(self, node):
        return None

    def operador_multiplicacao(self, node):
        return None

    def fator(self, node):
        if (node.child[0].type == "var"):
             return self.var(node.child[0])
        #if (node.child[0].type == "chamada_funcao"):
        #    return self.chamada_funcao(node.child[0])
        if (node.child[0].type == "numero"):
            return self.numero(node.child[0])
        #else:
        #    return self.expressao(node.child[0])

 
    def numero(self, node):
        string = repr(node.value)
        if "." in string:
            return "flutuante"
        else:
            return "inteiro"



if __name__ == '__main__':
    import sys, io
    code = io.open(sys.argv[1], mode="r", encoding="utf-8")
    s = Semantica(code.read())
    pprint.pprint(s.simbolos, depth=3, width=300)
