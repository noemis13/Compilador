from syntax import Syntax
from graphviz import Digraph

g = Digraph('G', format='svg')

class Semantica:
    def __init__(self, code):
        self.tabelaSimbolos = {}
        self.escopo = "global"
        self.tree = Syntax(code).ast 
        self.programa(self.tree)
        self.verificacoes(self.tabelaSimbolos)
        
    def verificacoes(self, tabelaSimbolos):
        #verificar se a função principal foi declarada
        nomePrincipal = "principal"
        nomeFuncao = "funcao"
        nomeVariavel = "variavel"
        nomeGlobal = "global"
        if nomePrincipal not in tabelaSimbolos.keys():
            print("Erro: FUnção 'principal' não declarada")
        
        for i, valor in tabelaSimbolos.items():
            #verificar se as funções são utilizadas
            if valor[0] == nomeFuncao:
                if i != nomePrincipal and valor[4] != 1:
                    print("Warning: Função '" + i + "' não utilizada")
            #verificar se as variaveis são utilzadas
            elif valor[0] == nomeVariavel:
                if valor[4] == 0:
                    nomeEscopo = i.split("-") 
                    print("Warning: Variável '" + valor[1] + "' não é utilizada, pertencente ao escopo'" + nomeEscopo[0] + "' ")    
    
    def programa(self, node):
        nodeFilho = node.child[0]
        self.lista_declaracoes(nodeFilho)


#     lista_declaracoes : lista_declaracoes declaracao
#                           | declaracao        
    def lista_declaracoes(self, node):
        valorNode = node.child[0]
        
        if len(node.child) !=1:
            if(valorNode != None):
                self.lista_declaracoes(valorNode)
            
            if(node.child[1] != None):
                valorNode = node.child[1]
                self.declaracao(valorNode)
        else:
            self.declaracao(valorNode)

        
    def declaracao(self, node):
        
        if node.child[0].type == "inicializacao_variaveis":
            #adicionar na arvore
            g.edge('declaracao', 'inicializacao_variaveis')
            
            noFilho = node.child[0].child[0] 
            #adicionar na arvore
            g.edge('inicializacao_variaveis', 'atribuicao')
       
            self.atribuicao(noFilho)
            

        elif node.child[0].type == "declaracao_variaveis":
            #adicionar na arvore
            g.edge('declaracao', 'declaracao_variaveis')

            self.declaracao_variaveis(node.child[0])
            
        else:
            tamNoFilho = len(node.child[0].child)
            if  tamNoFilho != 1:
                valorNoFilho = node.child[0].child[1].value 
                self.escopo = valorNoFilho
                
            else:
                valorNoFilho = node.child[0].child[0].value
                self.escopo = valorNoFilho
            
            self.declaracao_funcao(node.child[0])
            self.escopo = "global"
            
            #adicionar na arvore
            g.edge('declaracao', 'declaracao_funcao')


    def declaracao_variaveis(self, node):
        tamVar = len(node.child[1].child) 
        
        if tamVar != 1:
            #armazenar todas as variaveis na lista de variaveis
            nomeVar = self.lista_variaveis(node.child[1])
            
        else:
            nomeVar = node.child[1].child[0].value
            self.verifica_indice(node.child[1]) 
            
        tipoVar = node.child[0].value
        # se for uma lista de declaracoes
        print(nomeVar)
        if len(nomeVar) > 1:
            for i in nomeVar:
                self.verifica_declaracao_variaveis(i, tipoVar)
        else:
            self.verifica_declaracao_variaveis(nomeVar, tipoVar)


    def lista_variaveis(self, node):
        nomeVar = []
        if len(node.child) == 1:
            nomeVar.append(node.child[0].value)
        else:
            nomeVar = self.lista_variaveis(node.child[1])
            nomeVar.append(node.child[0].value)
        return nomeVar

    def verifica_indice(self, node):
        if len(node.child[0].child) == 1:
            self.indice(node.child[0].child[0])

    def indice(self, node):
        tipo = self.expressao(node.child[0])
        if node.child[0].value == "" or tipo != "inteiro":
            print("Erro: o índice do tipo '" + tipo + "' é inválido")


    def verifica_declaracao_variaveis(self, nomeVar, tipo):
        escopoVar = self.escopo + '-' + nomeVar
        escopoGlobalVar = "global-" + nomeVar
        
        if escopoVar in self.tabelaSimbolos.keys(): 
            if escopoGlobalVar in self.tabelaSimbolos.keys():
                print( "Warning: Variável '" + nomeVar + "' declarada anteriormente" )
            #verificar se a variavel não foi declarada em uma função
            for i, valor in tabelaSimbolos.items():
                print(valor[0])
               
        self.tabelaSimbolos[self.escopo + "-" + nomeVar] = ["variavel", nomeVar, False, tipo, 0]

        g.edge('declaracao_variaveis', nomeVar)


  
    def declaracao_funcao(self, node):
        tamNode = len(node.child)
        valorNode = node.child[0].value

        if tamNode == 1:
            self.tabelaSimbolos[valorNode] = ["funcao", valorNode, [], "void", 0]
            self.cabecalho(node.child[0])

        else:
            g.edge('tipo', valorNode)
            
            valorFilhoNode = node.child[1].value
            self.tabelaSimbolos[valorFilhoNode] = ["funcao", valorFilhoNode, [], valorNode, 0]
            self.cabecalho(node.child[1])

            #adicionar na arvore
            g.edge(valorFilhoNode, 'tipo')

          
         
#cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM     
    def cabecalho(self, node):
        parametros = self.lista_parametros(node.child[0])       
        self.tabelaSimbolos[node.value][2] = parametros

        tipoDoCorpo = self.corpo(node.child[1])
        tipFun = self.tabelaSimbolos[node.value][3]
        if tipoDoCorpo != tipFun:
            if tipoDoCorpo == None:
                tipoDoCorpo = "vazio";
            print("Warning: Função '" + node.value + "' retorna: '" + tipoDoCorpo + "' mas, deveria retornar '" + tipFun + "'")
        
        #adicionar na arvore
        g.edge('declaracao_funcao', node.value)
        g.edge(node.value, 'acao') 



    def lista_parametros(self, node):
        parametros = []
        if len(node.child) == 1:
            if node.child[0] == None:
                parametros = "void"
            else:
                parametros.append(self.parametro(node.child[0]))
        else:
            parametros = self.lista_parametros(node.child[0])
            par = self.parametro(node.child[1])
            if par != None:
                parametros.append(self.parametro(node.child[1]))
        return parametros


# parametro : tipo DOIS_PONTOS ID
#	  | parametro ABRE_COL FECHA_COL
    def parametro(self, node):
        self.tabelaSimbolos[self.escopo + "-" + node.value] = ["variavel", node.value, True, node.child[0].value, 0]
        
        return(node.child[0].value)



    def corpo(self, node):
        if node.child != None:
            if len(node.child) == 1:
                tipoCorpo = "void"
            else:
                self.corpo(node.child[0])
                tipoCorpo = self.acao(node.child[1])
                return tipoCorpo

    def acao(self, node):
        valorNode = node.child[0]

        if node.child[0].type == "expressao":
            g.edge('acao', 'expressao')
            return self.expressao(valorNode)
        
        elif node.child[0].type == "declaracao_variaveis":
            g.edge('acao', 'declaracao_variaveis')
            return self.declaracao_variaveis(valorNode)

        elif node.child[0].type == "leia":
            g.edge('acao', 'leia')
            return self.leia(valorNode)

        elif node.child[0].type == "escreva":
            g.edge('acao', 'escreva')
            return self.escreva(valorNode)

        elif node.child[0].type == "retorna":
            g.edge('acao', 'retorna')
            return self.retorna(valorNode)

    def leia(self, node):
        valorNode = node.value 
        
        g.edge('leia', valorNode)

        if valorNode not in self.tabelaSimbolos.keys():
            if "global-" + valorNode not in self.tabelaSimbolos.keys():
                print("Erro: Não foi declarada a '" + valorNode + "'")
        return "void"


    def escreva(self, node):
        g.edge('escreva', 'expressao')
        tExp = self.expressao(node.child[0])
        if tExp == "logico":
            print("Erro: expressao no 'escreva' não é válida")

        return "void"

    def retorna(self, node):
        g.edge('retorna', 'expressao')

        tExp = self.expressao(node.child[0])
        return tExp



    def atribuicao(self, node):
        valorNoFilho = node.child[0].value
        
        g.edge('atribuicao', valorNoFilho)

        nomeVar = self.escopo + "-" + valorNoFilho
        
        if nomeVar not in self.tabelaSimbolos.keys():
            nomeVar = "global" + "-" + valorNoFilho
            if nomeVar not in self.tabelaSimbolos.keys():
                print("Erro: A variável '" + valorNoFilho+ "' não foi declarada.")
        tipoRes = self.expressao(node.child[1])
        if nomeVar not in self.tabelaSimbolos:
            tipoVar = "tipo não declarado"
        else:
            tipoVar = self.tabelaSimbolos[nomeVar][3]
            self.tabelaSimbolos[nomeVar][2] = True
            self.tabelaSimbolos[nomeVar][4] = 1
        
        if tipoVar != tipoRes:
            if tipoRes is None:
                tipoRes = "void"        
            print("Warning: Coerção implícita do valor de '" + valorNoFilho + "'. O tipo esperado era: '" + tipoVar + "', tipo recebido foi: '" + tipoRes + "'")


    def expressao(self, node):
        if node.child[0].type == "atribuicao":
            g.edge('expressao', 'atribuicao')
            return self.atribuicao(node.child[0])
        elif node.child[0].type == "expressao_logica":
           return self.expressao_logica(node.child[0])
           
 
    def expressao_logica(self, node):
        tamNoFilho = len(node.child)
        noFilho = node.child[0]
        if tamNoFilho == 1:
            return self.expressao_simples(noFilho)
        
     
    def expressao_simples(self, node):
        tamNoFilho = len(node.child)
        noFilho = node.child[0]
        if tamNoFilho == 1:
            return self.expressao_aditiva(noFilho)
     
  
    def expressao_aditiva(self, node):
        tamNoFilho = len(node.child) 
        
        if tamNoFilho == 1:
            return self.expressao_multiplicativa(node.child[0])       
        else:
            tipoExpressao1 = self.expressao_aditiva(node.child[0])
            tipoExpressao2 = self.expressao_multiplicativa(node.child[2])
            op = self.op_soma(node.child[1])
        
            g.edge('expressao', op)
        
            if tipoExpressao1 == None:
                tipoExpressao1 = "tipo não declarado"
            if tipoExpressao2 == None:
                tipoExpressao2 = "tipo não delcarado"			
            
            if tipoExpressao1 != tipoExpressao2:
                print("Warning: Operação com tipos diferentes '" + tipoExpressao1 + "' e '" + tipoExpressao2 + "'")
                
 
    def expressao_multiplicativa(self, node):
        tamNoFilho = len(node.child)
        noFilho = node.child[0]
        if tamNoFilho == 1:
            return self.expressao_unaria(noFilho)
 

    def expressao_unaria(self, node):
        tamNoFilho = len(node.child)
        noFilho = node.child[0]
        if tamNoFilho == 1:
            g.edge('atribuicao', 'fator')
            return self.fator(noFilho)
 
 
    def fator(self, node):
        tipoNoFilho = node.child[0].type
        noFilho = node.child[0]
        valor = node.child[0].value
            
        if tipoNoFilho == "var":
             g.edge('fator', valor)
             tipoVar = self.verifica_var(noFilho)
             return tipoVar

        if tipoNoFilho == "chamada_funcao":
            tipoFunc = self.chamada_funcao(noFilho)
            return tipoFunc

        if tipoNoFilho == "numero":
            g.edge('fator', str(valor))

            if "." in repr(valor):
                tipoNum = "flutuante"
            else:
                tipoNum ="inteiro"
            return tipoNum

        else:
            return self.expressao(noFilho)

    def op_soma(self, node):
        operador = node.value
        return(operador)

    def verifica_var(self, node):
        nome = self.escopo + "-" + node.value
        apenasNome = node.value
        
        if nome not in self.tabelaSimbolos:
            nome = "global-" + node.value
            if nome not in self.tabelaSimbolos:
                print("Erro: Váriavel '" + node.value + "' não declarada")
            else:
                if self.tabelaSimbolos[nome][2] == False:
                    print("Erro: Váriavel '" + apenasNome + "' utilizada mas não inicializada.")  
      
        if nome in self.tabelaSimbolos:
            self.tabelaSimbolos[nome][4] = 1
            return self.tabelaSimbolos[nome][3]
 


    def verifica_fun(self, nomeFunc):
        if nomeFunc == "principal" and self.escopo != "principal":
            print("Erro: A função '" + self.escopo + "' realiza uma chamada não permitida para a função 'principal'")
        
        elif nomeFunc == "principal" and self.escopo == "principal":
            print("Erro: Chamada recursiva para a função 'principal'")

        #verificar se a funcao chamada foi declarada  
        if nomeFunc not in self.tabelaSimbolos.keys():
            if nomeFunc != "principal":
                print("Erro: Função '" + nomeFunc + "' não declarada")
     

    def chamada_funcao(self, node):
        nomeFunc = node.value
        self.verifica_fun(nomeFunc)

        if nomeFunc in self.tabelaSimbolos.keys():
            self.tabelaSimbolos[node.value][4] = 1

            argumentos = []
            argumentos.append(self.lista_argumentos(node.child[0]))
   
            if argumentos[0] == None:
                argumentos = []
            elif (not (type(argumentos[0]) is str)):
                argumentos = argumentos[0]
            
            argumentosEsperados = self.tabelaSimbolos[node.value][2]
            
            if type(argumentosEsperados) is str:
                argumentosEsperados = []

            tamEsperados = len(argumentosEsperados)
            tamRecebidos = len(argumentos)

            if tamRecebidos != tamEsperados:
            
                print("Erro: Na função '" + node.value + "' argumentos esperados era '" + str(tamEsperados) + "' quantidade de argumentos recebidos foi '" + str(tamRecebidos) + "'")
            
            return self.tabelaSimbolos[node.value][3]


    def lista_argumentos(self, node):
        tipoDaExpressao = []
            
        if len(node.child) == 1:
            if node.child[0] != None:
                if node.child[0].type == "expressao":
                    tipoDaExpressao = self.expressao(node.child[0])
                else:
                    tipoDaExpressao = []
        else:
            tipoDaExpressao = []
            tipoDaExpressao.append(self.lista_argumentos(node.child[0]))
            tipoDaExpressao.append(self.expressao(node.child[1]))
 
        return tipoDaExpressao


if __name__ == '__main__':
    import sys, io
    code = io.open(sys.argv[1], mode="r", encoding="utf-8")
    s = Semantica(code.read())
    filename = g.render(filename='img/asto')
    print("\n Tabela de tabelaSimbolos: ", s.tabelaSimbolos)
