from syntax import Syntax
from ply import yacc
from graphviz import Digraph

g = Digraph('G', format='svg')

class Semantica:
    def __init__(self, code):
        self.tabelaSimbolos = {}
        self.escopo = "global"
        #pegar a arovre abstrata
        self.tree = Syntax(code).ast 
        self.programa(self.tree)
 
        self.verifica_main(self.tabelaSimbolos)
        self.verifica_variaveis(self.tabelaSimbolos)
        self.verifica_funcoes(self.tabelaSimbolos)
 
    #verificações iniciais
    def verifica_main(self, tabelaSimbolos):
        if ("principal" not in tabelaSimbolos.keys()):
            print("Erro: A função principal não foi declarada")
            
    def verifica_variaveis(self, tabelaSimbolos):
       for i, valor in tabelaSimbolos.items():
           if valor[0] == "variavel" and valor[2] == False:
           	valorEscopo = i.split("-")
           	if valorEscopo != "golbal":
           		print("Warning: A variável '" + valor[1] +"' do  '" + valorEscopo[0] + "' não é utilizada")
           	else:
           		print("Warning: A variável '" + valor[1] +"' não é utilizada")
  

    def verifica_funcoes(self, tabelaSimbolos):
       for i, valor in tabelaSimbolos.items():
             if valor[0] == 'funcao':
                 if i != 'principal' and valor[5] !=1:
                     print("Warning: A função '"+ i +"' não é utilizada")

       
    def raiz(self):
        if(self.tree.type == "programa_principal"):
            self.scope = "principal"
            self.principal(self.tree.child[0])
            self.scope = "global"
    
    def programa(self, node):
        self.lista_declaracoes(node.child[0])

#     lista_declaracoes : lista_declaracoes declaracao
#                           | declaracao        
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
            #adicionar na arvore
            g.edge('declaracao', 'declaracao_variaveis')
        elif (node.child[0].type == "inicializacao_variaveis"):
            #adicionar na arvore
            g.edge('declaracao', 'inicializacao_variaveis')
            self.inicializacao_variaveis(node.child[0])
        else:
            if (len(node.child[0].child) == 1):
                self.escopo = node.child[0].child[0].value
            else:
                self.escopo = node.child[0].child[1].value
            self.declaracao_funcao(node.child[0])
            self.escopo = "global"
            
            #adicionar na arvore
            g.edge('declaracao', 'declaracao_funcao')


    #declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis
    def declaracao_variaveis(self, node):
        tipo = node.child[0].value
        nome = ""
        contBreak = 0
        for valorVar in self.lista_variaveis(node.child[1]):
            
            if ("[" in valorVar):
                nome = valorVar.split('[')[0]
                valorVar = nome
            if ( (self.escopo + '-' + valorVar in self.tabelaSimbolos.keys()) or ("global-" + valorVar in self.tabelaSimbolos.keys()) ):
                if contBreak == 1:
                    contBreak = 0
                    print( "Warning: A variável '" + valorVar + "' já foi declarada anteriormente." )
                
            if (valorVar in self.tabelaSimbolos.keys()):
                print("Erro: Já existe uma função com o nome '" + valorVar + "'")
            self.tabelaSimbolos[self.escopo + "-" + valorVar] = ["variavel", valorVar, False, False, tipo, 0]
            g.edge('declaracao_variaveis', valorVar)
        return "void"


    def inicializacao_variaveis(self, node):
        self.atribuicao(node.child[0])
        #adicionar na arvore
        g.edge('inicializacao_variaveis', 'atribuicao')

    def lista_variaveis(self, node):
        nomeVar = []
        
        if (len(node.child) == 1):
            if (len(node.child[0].child) == 1):
                nomeVar.append(node.child[0].value + self.indice(node.child[0].child[0]))
            else:
                nomeVar.append(node.child[0].value)
            return nomeVar

        else:
            nomeVar = self.lista_variaveis(node.child[1])
            nomeVar.append(node.child[0].value)
            return nomeVar
        

    def var(self, node):
        nome = self.escopo + "-" + node.value
        apenasNome = node.value
                
        if (len(node.child) == 1):
            #verificar declaracao da variavel
                
            if (nome not in self.tabelaSimbolos):
                nome = "global-" + node.value
                if (nome not in self.tabelaSimbolos):
                    print("Erro: A váriavel '" + node.value + "' não foi declarada")
            else:
                if (self.tabelaSimbolos[nome][3] == False):
                   print("Erro: váriavel '" + nome + "' não foi inicializada")
                var = self.indice(node.child[0])
                self.tabelaSimbolos[nome][4] = self.tabelaSimbolos[nome][4] + var
                self.tabelaSimbolos[nome][2] = True
                return self.tabelaSimbolos[nome][4]

        else:
            if (nome not in self.tabelaSimbolos):
                nome = "global-" + node.value
                if (nome not in self.tabelaSimbolos):
                    print("Erro: A váriavel '" + node.value + "' não foi declarada")
                else:
                    if (self.tabelaSimbolos[nome][3] == False):
                        print("Erro: A váriavel '" + apenasNome + "' não foi inicializada.")  
            else:
                if (self.tabelaSimbolos[nome][3] == False):
                    print("Erro: A váriavel '" + apenasNome + "' não foi inicializada.")
            if (nome in self.tabelaSimbolos):
                self.tabelaSimbolos[nome][2] = True
                return self.tabelaSimbolos[nome][4]



    def indice(self, node):
        if (len(node.child) == 1):
            tipo = self.expressao(node.child[0])
            if (node.child[0].value == "" or tipo != "inteiro"):
                print("Erro: index inválido, permitido somente inteiro")
            return ("[]")
        else:
            variavel = self.indice(node.child[0])
            tipo = self.expressao(node.child[1])
            if (tipo != "inteiro"):
                print("Erro: index inválido, permitido somente inteiro")
            return ("[]" + variavel)
        g.edge('indice', 'expressao')
        


    def tipo(self, node):
        
        if (node.value == "inteiro" or node.value == "flutuante"):
            g.edge('tipo', node.value)
            return node.value
        else:
            print("Erro: Somente tipos inteiros e flutuantes são aceitos. Tipo entrado: " + node.value)

    def declaracao_funcao(self, node):
        if (len(node.child) == 1):
            tipo = "void"
            self.tabelaSimbolos[node.child[0].value] = ["funcao", node.child[0].value, [], False, tipo, 0]
            self.cabecalho(node.child[0])
        else:
            tipo = self.tipo(node.child[0])
            self.tabelaSimbolos[node.child[1].value] = ["funcao", node.child[1].value, [], False, tipo, 0]
            self.cabecalho(node.child[1])
            #adicionar na arvore
            g.edge(node.child[1].value, 'tipo')
            
#cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM     
    def cabecalho(self, node):
        lista_par = self.lista_parametros(node.child[0])
        self.tabelaSimbolos[node.value][2] = lista_par

        tipo_corpo = self.corpo(node.child[1])
        tipo_fun = self.tabelaSimbolos[node.value][4]
        if tipo_corpo == None:
            tipo_corpo = "vazio";
            
        if tipo_corpo != tipo_fun:
            if (node.value == "principal"):
                print("Warning: a função '" + node.value + "' deveria retornar: '" + tipo_fun + "' mas retorna '" + tipo_corpo + "'")
            else:
                print("Erro: a função '" + node.value + "' deveria retornar: '" + tipo_fun + "' mas retorna '" + tipo_corpo + "'")
        
        #adicionar na arvore
        g.edge('declaracao_funcao', node.value)
        g.edge(node.value, 'acao') 

  # lista_parametros : lista_parametros VIRGULA lista_parametros
  #                          | parametro
  #                          | vazio
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
            par = self.parametro(node.child[1])
            if par != None:
                lista_param.append(self.parametro(node.child[1]))
            return lista_param

# parametro : tipo DOIS_PONTOS ID
#	  | parametro ABRE_COL FECHA_COL

    def parametro(self, node):
        if (node.child[0].type == "parametro"):
            return self.parametro(node.child[0]) + "[]"
        else:
            self.tabelaSimbolos[self.escopo + "-" + node.value] = ["variavel", node.value, False, True, node.child[0].value, 0]
            return(node.child[0].value)


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
            g.edge('acao', 'expressao')
            return self.expressao(node.child[0])
        elif (node.child[0].type == "declaracao_variaveis"):
            g.edge('acao', 'declaracao_variaveis')
            return self.declaracao_variaveis(node.child[0])
        elif (node.child[0].type == "se"):
            g.edge('acao', 'se')
            return self.se(node.child[0])
        elif (node.child[0].type == "repita"):
            g.edge('acao', 'repita')
            return self.repita(node.child[0])
        elif (node.child[0].type == "leia"):
            g.edge('acao', 'leia')
            return self.leia(node.child[0])
        elif (node.child[0].type == "escreva"):
            g.edge('acao', 'escreva')
            return self.escreva(node.child[0])
        elif (node.child[0].type == "retorna"):
            g.edge('acao', 'retorna')
            return self.retorna(node.child[0])

    def se(self, node):
        tipo_se = self.expressao(node.child[0])

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
        g.edge('se', 'expressao')
 
    def repita(self, node):
        tipo_repita = self.expressao(node.child[1])
        g.edge('repita', 'expressao')
        return self.corpo(node.child[0])


    def atribuicao(self, node):
        g.edge('atribuicao', node.child[0].value)

        nome = self.escopo + "-" + node.child[0].value
        if (self.escopo + "-" + node.child[0].value not in self.tabelaSimbolos.keys()):
            nome = "global" + "-" + node.child[0].value
            if ("global" + "-" + node.child[0].value not in self.tabelaSimbolos.keys()):
                print("Erro: A variável '" + node.child[0].value + "' não foi declarada.")
        if nome not in self.tabelaSimbolos:
            tipo_esperado = "tipo não declarado"
        else:
            tipo_esperado = self.tabelaSimbolos[nome][4]
        tipo_recebido = self.expressao(node.child[1])
        
        if nome in self.tabelaSimbolos:
            #variavel iincializada e delcarada
            self.tabelaSimbolos[nome][2] = True
            self.tabelaSimbolos[nome][3] = True
        if tipo_recebido is None:
             tipo_recebido = "void"        

        if (tipo_esperado != tipo_recebido):
            print("Warning: Coerção implícita de tipos! Tipo esperado da variável '" + node.child[0].value + "' é: " + tipo_esperado + ", tipo recebido: " + tipo_recebido)
        return "void"

    def leia(self, node):
        g.edge('leia', node.value)
        if node.value not in self.tabelaSimbolos.keys():
            if "global-" + node.value not in self.tabelaSimbolos.keys():
                print("Erro: " + node.value + " não declarada")
        return "void"

    def escreva(self, node):
        g.edge('escreva', 'expressao')
        tipo_exp = self.expressao(node.child[0])

        if tipo_exp == "logico":
            print("Erro: expressao inválida!")

        return "void"

    def retorna(self, node):
        g.edge('retorna', 'expressao')
        tipo_exp = self.expressao(node.child[0])

        if (tipo_exp == "logico"):
            print("Erro: expressao inválida!")
        return tipo_exp


    def expressao(self, node):
        if (node.child[0].type == "expressao_logica"):
           return self.expressao_logica(node.child[0])
        else:
            g.edge('expressao', 'atribuicao')
            return self.atribuicao(node.child[0])
            
    def expressao_logica(self, node):
        if (len(node.child)==1):
            return self.expressao_simples(node.child[0])
        else:
            tipo1 = self.expressao_logica(node.child[0])
            op = self.operador_logico(node.child[1])
            
            g.edge('expressao', op)
            
            return "logico"

    def expressao_simples(self, node):
        
        if len(node.child) == 1:
            return self.expressao_aditiva(node.child[0])
        else:
            tipo1 = self.expressao_simples(node.child[0])
            op = self.operador_relacional(node.child[1])
            tipo2 = self.expressao_aditiva(node.child[2])
            
            if tipo1 == None:
                tipo1 = "tipo não declarado"
            if tipo2 == None:
                tipo2 = "tipo não delcarado"			

            if (tipo1 != tipo2):
                print("Warning: Operação com tipos diferentes '" + tipo1 + "' e '" + tipo2)
            g.edge('expressao', op)
        
            return "simples"

    def expressao_aditiva(self, node):
        if (len(node.child) == 1):
            return self.expressao_multiplicativa(node.child[0])
        else:
            tipo1 = self.expressao_aditiva(node.child[0])
            op = self.operador_soma(node.child[1])
            tipo2 = self.expressao_multiplicativa(node.child[2])
            g.edge('expressao', op)
        
            if tipo1 == None:
                tipo1 = "tipo não declarado"
            if tipo2 == None:
                tipo2 = "tipo não delcarado"			
            
            if (tipo1 != tipo2):
                print("Warning: Operação com tipos diferentes '" + tipo1 + "' e '" + tipo2 + "'")
            if (tipo1 == "flutuante") or (tipo2 == "flutuante"):
                return "flutuante"
            elif(tipo1 == "inteiro") or (tipo2 == "inteiro"):
                return "inteiro"
            else:
                return "void"

    def expressao_multiplicativa(self, node):
        if (len(node.child) == 1):
            return self.expressao_unaria(node.child[0])
        else:
            tipo1 = self.expressao_multiplicativa(node.child[0])
            op = self.operador_multiplicacao(node.child[1])
            tipo2 = self.expressao_unaria(node.child[2])
            g.edge('expressao', op)
        
            if tipo1 == None:
                tipo1 = "tipo não declarado"
            if tipo2 == None:
                tipo2 = "tipo não delcarado"			

            if (tipo1 != tipo2):
                print("Warning: Operação com tipos diferentes '" + tipo1 + "' e '" + tipo2)
            elif(tipo1 == "inteiro") or (tipo2 == "inteiro"):
                return "interio"
            else:
                return "void"

    def expressao_unaria(self, node):
        if (len(node.child) == 1):
            g.edge('atribuicao', 'fator')
            return self.fator(node.child[0])
        else:
            if(node.child[0].type == "operador_soma"):
                op = self.operador_soma(node.child[0])
            else:
               op = self.operador_negacao(node.child[0])
            g.edge('expressao', op)
            g.edge(op, 'fator')        
            return self.fator(node.child[1])
 
    def operador_logico(self, node):
        return node.value

    def operador_relacional(self, node):
        return node.value

    def operador_soma(self, node):
        return node.value

    def operador_negacao(self, node):
        return node.value

    def operador_multiplicacao(self, node):
        return node.value

    def fator(self, node):
        if (node.child[0].type == "var"):
             g.edge('fator', node.child[0].value)
             return self.var(node.child[0])
        if (node.child[0].type == "chamada_funcao"):
            return self.chamada_funcao(node.child[0])
        if (node.child[0].type == "numero"):
            g.edge('fator', str(node.child[0].value))
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
        #verificações da funcao principal
        #chamada recursiva
        if (node.value == "principal" and self.escopo == "principal"):
            print("Erro: Chamada recursiva para a função 'principal'")
        #chamada não permitida
        if (node.value == "principal" and self.escopo != "principal"):
            print("Erro: A função '" + self.escopo + "' realiza uma chamada não permitida para a função 'principal'")

        #verificar se a funcao chamada foi declarada  
        if (node.value not in self.tabelaSimbolos.keys()):
            if node.value != "principal":
                print("Erro: Função '" + node.value + "' não foi declarada")
       #verificar os numero de argumentos esperados da funcao
        else:
            self.tabelaSimbolos[node.value][5] = 1
            argslista = []
            argslista.append(self.lista_argumentos(node.child[0]))
            
            if (argslista[0] == None):
                argslista = []
            elif (not (type(argslista[0]) is str)):
                argslista = argslista[0]
            args_esperados = self.tabelaSimbolos[node.value][2]

            if (type(args_esperados) is str):
                args_esperados = []
            if (len(argslista) != len(args_esperados)):
                lesperados = (len(args_esperados))
                lrecebidos = (len(argslista))
                print("Erro: Numero de argumentos esperados em '" + node.value + "': " + str(lesperados) + ", quantidade de argumentos recebidos: " + str(lrecebidos))
            
            #verificar os tipos de argumentos recebidos na chamada da função
            for i in range(len(argslista)):
                if (argslista[i] != args_esperados[i]):
                    print("Erro: Função '" + node.value+ "'. Argumento " + str(i) + ", tipo esperado '" + args_esperados[i] + "', tipo recebido '" + argslista[i] + "'")
            self.tabelaSimbolos[node.value][3] = True
            return self.tabelaSimbolos[node.value][4]


    def lista_argumentos(self, node):
        if len(node.child) == 1:
            if (node.child[0] == None):
                return
            if (node.child[0].type == "expressao"):
                exp = self.expressao(node.child[0])
                return(exp)
            else:
                return []
        else:
            tipoExp = []
            tipoExp.append(self.lista_argumentos(node.child[0]))
            tipoExp.append(self.expressao(node.child[1]))
            return tipoExp


if __name__ == '__main__':
    import sys, io
    code = io.open(sys.argv[1], mode="r", encoding="utf-8")
    s = Semantica(code.read())
    filename = g.render(filename='img/asto')
    print("\n Tabela de tabelaSimbolos: ", s.tabelaSimbolos)
