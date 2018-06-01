from syntax import Syntax
from ply import yacc
import pprint


class Semantica:
    def __init__(self, code):
        self.simbolos = {}
        self.escopo = "global"
        self.tree = Syntax(code).ast
        self.programa(self.tree)
        self.check_main(self.simbolos)
        self.check_var_utilizadas(self.simbolos)
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
            if(node.child[1] != None):
                self.declaracao(node.child[1])

    def declaracao(self, node):
        if (node.child[0].type == "declaracao_variaveis"):
            self.declaracao_variaveis(node.child[0])
        elif (node.child[0].type == "inicializacao_variaveis"):
            self.inicializacao_variaveis(node.child[0])
        else:
            if (len(node.child[0].child) == 1):
                self.escopo = node.child[0].child[0].value
            else:
                self.escopo = node.child[0].child[1].value
            self.declaracao_funcao(node.child[0])
            self.escopo = "global"



    #declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis
    # Warning: Verificar se a variavel ja foi declarada
    # Warning: verificar se variavel declarada foi tuilziada
    #Warning: coerção
    def declaracao_variaveis(self, node):
        tipo = node.child[0].type
        arr_name = ""

        for son in self.lista_variaveis(node.child[1]):
            if ("[" in son):
                arr_name = son.split('[')[0]
                son = arr_name
            if ( (self.escopo + '-' + son in self.simbolos.keys()) or ("global-" + son in self.simbolos.keys()) ):
                print( "Warning: A variável '" + son + "' já foi declarada anteriormente." )
                #exit(1)
            if (son in self.simbolos.keys()):
                print("Erro: Já existe uma função com o nome '" + son + "'")
                #exit(1)
            self.simbolos[self.escopo + "-" + son] = ["variavel", son, False, False, tipo, 0]
        return "void"


    def inicializacao_variaveis(self, node):
        self.atribuicao(node.child[0])

    def lista_variaveis(self, node):
        ret_args = []

        if (len(node.child) == 1):
            if (len(node.child[0].child) == 1):
                ret_args.append(node.child[0].value + self.indice(node.child[0].child[0]))
            else:
                ret_args.append(node.child[0].value)
            return ret_args
        else:
            ret_args = self.lista_variaveis(node.child[0])
            if (len(node.child[1].child) == 1):
                ret_args.append(node.child[1].value + self.indice(node.child[1].child[0]))
            else:
                ret_args.append(node.child[1].value)
            return ret_args
        

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
            if (node.child[0].value == "" or tipo != "inteiro"):
                print("Erro: index invalido, permitido somente inteiro")
            return ("[]")
        else:
            variavel = self.indice(node.child[0])
            tipo = self.expressao(node.child[1])
            if (tipo != "inteiro"):
                print("Erro: index invalido, permitido sómente inteiro")
                #				exit(1)
            return ("[]" + variavel)


    def tipo(self, node):
        if (node.type == "inteiro" or node.type == "flutuante"):
            return node.type
        else:
            print("Erro: Somente tipos inteiros e flutuantes são aceitos. Tipo entrado: " + node.type)

    def declaracao_funcao(self, node):
        if (len(node.child) == 1):
            tipo = "void"
            if node.child[0].value in self.simbolos.keys():
                print("Erro: Função " + node.child[0].value + " já foi declarada.")
                exit(1)
            elif "global-" + node.child[0].value in self.simbolos.keys():
                print("Erro: Uso duplicado do nome '" + node.child[0].value + "'")
                exit(1)
            self.simbolos[node.child[0].value] = ["funcao", node.child[0].value, [], False, tipo, 0]
            self.cabecalho(node.child[0])
        else:
            tipo = self.tipo(node.child[0])
            self.simbolos[node.child[1].value] = ["funcao", node.child[1].value, [], False, tipo, 0]
            self.cabecalho(node.child[1])

    def cabecalho(self, node):
        lista_par = self.lista_parametros(node.child[0])

        self.simbolos[node.value][2] = lista_par
        tipo_corpo = self.corpo(node.child[1])
        tipo_fun = self.simbolos[node.value][4]
        if tipo_corpo != tipo_fun:
            if (node.value == "principal"):
                print(
                    "Warning: a função '" + node.value + "' deveria retornar: '" + tipo_fun + "' mas retorna '" + tipo_corpo + "'")
            else:
                print(
                    "Erro: a função '" + node.value + "' deveria retornar: '" + tipo_fun + "' mas retorna '" + tipo_corpo + "'")
                #				exit(1)



    def lista_parametros(self, node):
        lista_param = []
        if (len(node.child) == 1):
            if (node.child[0] == None):
                return self.vazio(node.child[0])
            else:
                lista_param.append(self.parametro(node.child[0]))
                return lista_param
        else:
            lista_param = self.lista_parametros(node.child[0])
            lista_param.append(self.parametro(node.child[1]))
            return lista_param


    def parametro(self, node):
        if (node.child[0].type == "parametro"):
            return self.parametro(node.child[0]) + "[]"
        else:
            self.simbolos[self.escopo + "-" + node.value] = ["variavel", node.value, False, False, node.child[0].type, 0]
            return self.tipo(node.child[0])


    def vazio(self, node):
        return "void"

    def corpo(self, node):
        if (node.child != None):
            if (len(node.child) == 1):
                return self.vazio(node.child[0])
            else:
                tipo1c = self.corpo(node.child[0])
                tipo2c = self.acao(node.child[1])
                if (tipo2c != None):
                    return tipo2c

    def acao(self, node):
        tipo_ret_acao = "void"
        if (node.child[0].type == "expressao"):
            return self.expressao(node.child[0])
        elif (node.child[0].type == "declaracao_variaveis"):
            return self.declaracao_variaveis(node.child[0])
        elif (node.child[0].type == "se"):
            return self.se(node.child[0])
        elif (node.child[0].type == "repita"):
            return self.repita(node.child[0])
        elif (node.child[0].type == "leia"):
            return self.leia(node.child[0])
        elif (node.child[0].type == "escreva"):
            return self.escreva(node.child[0])
        elif (node.child[0].type == "retorna"):
            return self.retorna(node.child[0])

    def se(self, node):
        tipo_se = self.expressao(node.child[0])
        if tipo_se != "logico":
            print("Erro: Era esperado uma expressão logica para a condição, foi dado uma expressão do tipo: " + tipo_se)
            exit(1)

        if (len(node.child) == 2):
            return self.corpo(node.child[1])
        else:
            tipo_c1 = self.corpo(node.child[1])
            tipo_c2 = self.corpo(node.child[2])
            if tipo_c1 != tipo_c2:
                if (tipo_c1 == "void"):
                    return tipo_c2
                else:
                    return tipo_c1
            return tipo_c1
 
    def repita(self, node):
        tipo_se = self.expressao(node.child[1])
        if tipo_se != "logico":
            print("Erro: Espera-se uma expressão logica para o SE, foi dado: " + tipo_se)
            exit(1)

        return self.corpo(node.child[0])

    def atribuicao(self, node):
        nome = self.escopo + "-" + node.child[0].value
        if (self.escopo + "-" + node.child[0].value not in self.simbolos.keys()):
            nome = "global" + "-" + node.child[0].value
            if ("global" + "-" + node.child[0].value not in self.simbolos.keys()):
                print("Erro: A variável '" + node.child[0].value + "' não foi declarada.")
                exit(1)
        tipo_esperado = self.simbolos[nome][4]
        tipo_recebido = self.expressao(node.child[1])
        self.simbolos[nome][2] = True
        self.simbolos[nome][3] = True
        if (tipo_esperado != tipo_recebido):
            print(
                "Warning: Coerção implícita de tipos! Tipo esperado: " + tipo_esperado + ", tipo recebido: " + tipo_recebido + ".")
        return "void"

    def leia(self, node):
        if self.scope + "-" + node.value not in self.simbolos.keys():
            if "global-" + node.value not in self.simbolos.keys():
                print("Erro: " + node.value + " não declarada")
                exit(1)
        return "void"

    def escreva(self, node):
        tipo_exp = self.expressao(node.child[0])

        if tipo_exp == "logico":
            print("Erro: expressao inválida!")

        return "void"

    def retorna(self, node):
        tipo_exp = self.expressao(node.child[0])

        if (tipo_exp == "logico"):
            print("Erro: expressao inválida!")
        return tipo_exp


    def expressao(self, node):
        if (node.child[0].type == "expressao_logica"):
           return self.expressao_logica(node.child[0])
        else:
            return self.atribuicao(node.child[0])
            print("atribuicao")

    def expressao_logica(self, node):
        if (len(node.child)==1):
            return self.expressao_simples(node.child[0])
        else:
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
        if (node.child[0].type == "chamada_funcao"):
            return self.chamada_funcao(node.child[0])
        if (node.child[0].type == "numero"):
            return self.numero(node.child[0])
        else:
            return self.expressao(node.child[0])

 
    def numero(self, node):
        string = repr(node.value)
        if "." in string:
            return "flutuante"
        else:
            return "inteiro"


    def chamada_funcao(self, node):
        if (node.value == "principal" and self.escopo == "principal"):
            print("Erro: Chamada recursiva para a função principal")
            exit(1)
        if (node.value == "principal" and self.escopo != "principal"):
            print("Erro: A função '" + self.escopo + "' realiza uma chamada para a função principal.")
            exit(1)
        if node.value not in self.simbolos.keys():
            print("Erro: Função " + node.value + " não declarada")
            exit(1)
        self.simbolos[node.value][5] = 1
        argslista = []
        argslista.append(self.lista_argumentos(node.child[0]))
        if (argslista[0] == None):
            argslista = []
        elif (not (type(argslista[0]) is str)):
            argslista = argslista[0]

        args_esperados = self.simbolos[node.value][2]
        if (type(args_esperados) is str):
            args_esperados = []
        if (len(argslista) != len(args_esperados)):
            lesperados = (len(args_esperados))
            lrecebidos = (len(argslista))
            print("Erro: Numero de argumentos esperados em '" + node.value + "': " + str(
                lesperados) + ", quantidade de argumentos recebidos: " + str(lrecebidos))
            exit(1)

        for i in range(len(argslista)):
            if (argslista[i] != args_esperados[i]):
                print("Erro: Argumento " + str(i) + ", tipo esperado " + args_esperados[i] + ", tipo recebido " +
                      argslista[i])
                exit(1)
        self.simbolos[node.value][3] = True
        return self.simbolos[node.value][4]


    def lista_argumentos(self, node):
        if (len(node.child) == 1):
            if (node.child[0] == None):
                return
            if (node.child[0].type == "expressao"):
                return (self.expressao(node.child[0]))
            else:
                return []
        else:
            ret_args = []
            ret_args.append(self.lista_argumentos(node.child[0]))
            if (not (type(ret_args[0]) is str)):
                ret_args = ret_args[0]

            ret_args.append(self.expressao(node.child[1]))
            return ret_args

#######################################################################
#################### CHECK #############################################

    def check_main(self, simbolos):
        if ("principal" not in simbolos.keys()):
            print("Erro: função principal não declarada")
            #exit(1)

    def check_var_utilizadas(self, simbolos):
        for k, v in simbolos.items():
            if (v[0] == "variavel"):
                if (v[2] == False):
                    escopo = k.split("-")
                    if (escopo[0] != "global"):
                        print("Warning: Variavel '" + v[1] + "' da função '" + escopo[0] + "' nunca é utilizada")
                    else:
                        print("Warning: Variavel '" + v[1] + "' nunca é utilizada")



if __name__ == '__main__':
    import sys, io
    code = io.open(sys.argv[1], mode="r", encoding="utf-8")
    s = Semantica(code.read())
    pprint.pprint(s.simbolos, depth=3, width=300)
