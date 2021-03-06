# -*- coding: utf-8 -*-

import ply.yacc as yacc
from lexer import Lexica
import graphviz as gv
from graphviz import Digraph, Graph

g1 = Digraph('G', format='svg')

class Tree:
    def __init__(self, type_node, child=[], value=''):
        self.type = type_node
        self.child = child
        self.value = value

    def __str__(self):
        return self.type


########################
# Analisador Sintático #
########################

class Syntax:
    def __init__(self, code):
        lex = Lexica()
        self.tokens = lex.tokens
        self.precedence = (
            (('left', 'IGUAL', 'NEGACAO', 'MENOR_IGUAL', 'MAIOR', 'MAIOR_IGUAL', 'MENOR','E_LOGICO', 'OU_LOGICO'),
             ('left', 'SOMA', 'SUB'),
             ('left', 'MULT', 'DIVISAO'))
        )
        parser = yacc.yacc(debug=True, module=self, optimize=False)
        self.ast = parser.parse(code)

    def p_programa(self, p):
        '''
        programa : lista_declaracoes
                     '''
        p[0] = Tree('programa', [p[1]])
        g1.node('programa')
        g1.edge('programa','lista_declaracoes')

    def p_lista_declaracoes(self, p):
        '''
        lista_declaracoes : lista_declaracoes declaracao
                          | declaracao
                         | error
        '''
        if (len(p) == 3):
            p[0] = Tree('lista_declaracoes', [p[1], p[2]])
            g1.edge('lista_declaracoes', 'declaracao')
            g1.edge('declaracao', 'lista_declaracoes')
        elif (len(p) == 2):
            p[0] = Tree('lista_declaracoes', [p[1]])
            g1.edge('lista_declaracoes', 'declaracao')
        elif p.slice[1] == 'error' :
            print( "Erro: declaração incompleta! \n")


    def p_declaracao(self, p):
        '''
        declaracao : declaracao_variaveis
                   | inicializacao_variaveis
                   | declaracao_funcao
        '''
        p[0] = Tree('declaracao', [p[1]])

        if(str(p[1]) == 'declaracao_variaveis'):
            g1.edge('declaracao', 'declaracao_variaveis')
        elif(str(p[1]) == 'inicializacao_variaveis'):
           g1.edge('declaracao', 'inicializacao_variaveis')
        else:
           g1.edge('declaracao', 'declaracao_funcao')

    def p_declaracao_variaveis(self, p):
        '''
        declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis
        '''
        p[0] = Tree('declaracao_variaveis', [p[1], p[3]], p[2])
        g1.edge('declaracao_variaveis', 'tipo')
        g1.edge('declaracao_variaveis', 'lista_variaveis')
        
    def p_declaracao_variaveis_error(self, p):
        '''
        declaracao_variaveis : tipo DOIS_PONTOS error
        '''
        g1.edge('declaracao_variaveis', 'tipo')
        g1.edge('declaracao_variaveis', 'error')
        print("Erro: Declaração de variável incompleta. \n")


    def p_inicializacao_variaveis(self, p):
        '''
        inicializacao_variaveis : atribuicao
        '''
        p[0] = Tree('inicializacao_variaveis', [p[1]])
        g1.edge('inicializacao_variaveis', 'atribuicao')
        
    def p_lista_variaveis(self, p):
        '''
        lista_variaveis : var VIRGULA lista_variaveis
                        | var
        '''
        if (len(p) == 4):
            p[0] = Tree('lista_variaveis', [p[1], p[3]])
            g1.edge('lista_variaveis', 'var')
            g1.edge('lista_variaveis', 'lista_variaveis')
        elif (len(p) == 2):
            p[0] = Tree('lista_variaveis', [p[1]])
            g1.edge('lista_variaveis', 'var')
        # g1.edge('lista_variaveis', 'var')


    def p_var(self, p):
        '''
        var : ID
            | ID indice
        '''
        if (len(p) == 2):
            p[0] = Tree('var', [], p[1])
            g1.edge('var', p[1])
        elif (len(p) == 3):
            p[0] = Tree('var', [p[2]], p[1])
            g1.edge('var', 'indice')
            g1.edge('indice', p[1])
            
    def p_indice(self, p):
        '''
        indice : indice ABRE_COL expressao FECHA_COL
               | ABRE_COL expressao FECHA_COL
        '''
        if (len(p) == 5):
            p[0] = Tree('indice', [p[1], p[3]])
            g1.edge('indice', 'indice')
            g1.edge('indice', 'expressao')
        elif (len(p) == 4):
            p[0] = Tree('indice', [p[2]])
            g1.edge('indice', 'expressao')
        #g1.edge('indice', 'expressao')

 #   def p_indice_error(self, p):
 #       '''
 #       indice : indice ABRE_COL error FECHA_COL
 #               | ABRE_COL error FECHA_COL
#		| error FECHA_COL
#		| ABRE_COL error
#        	| indice error FECHA_COL
#		| indice ABRE_COL error
#		
 #       '''
#        print("Erro: Não foi declarado o tamanho ou faltou colchetes.\n" )

    def p_tipo(self, p):
        '''
        tipo : INTEIRO
	     | FLUTUANTE
        '''
        p[0] = Tree('tipo', [], p[1])
        g1.edge('tipo', p[1])
        
    def p_declaracao_funcao(self, p):
        '''
        declaracao_funcao : tipo cabecalho
                          | cabecalho
        '''
        if len(p) == 3:
            p[0] = Tree('declaracao_funcao', [p[1], p[2]])
            g1.edge('declaracao_funcao', 'tipo')
            g1.edge('declaracao_funcao', 'cabecalho')
        elif len(p) == 2:
            p[0] = Tree('declaracao_funcao', [p[1]])
            g1.edge('declaracao_funcao', 'cabecalho')

    def p_cabecalho(self, p):
        '''
        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM
        '''
        p[0] = Tree('cabecalho', [p[3], p[5]], p[1])
        g1.edge('cabecalho', p[1] )
        g1.edge(p[1], 'lista_parametros')
        g1.edge('lista_parametros', 'corpo')


#    def p_cabecalho_error(self, p):
#        '''
#        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo error
#        '''
#        print("Erro: Faltou a declaração 'fim' da função.\n" )


    def p_lista_parametros(self, p):
        '''
        lista_parametros : lista_parametros VIRGULA parametro
                         | parametro
                         | vazio
        '''
        if len(p) == 4:
            p[0] = Tree('lista_parametros', [p[1], p[3]])
            g1.edge('lista_parametros', 'parametro')
            g1.edge('lista_parametros', 'lista_parametros')
        elif len(p) == 2:
            p[0] = Tree('lista_parametros', [p[1]])
            g1.edge('lista_parametros', 'parametro')
        else:
            p[0] = Tree('vazio', [p[1]])
            g1.edge('lista_parametros', 'vazio')


    def p_parametro1(self, p):
        '''
        parametro : tipo DOIS_PONTOS ID
        '''
        p[0] = Tree('parametro', [p[1]], p[3])
        g1.edge('parametro', 'tipo')
        g1.edge('tipo', p[3])
       
    def p_parametro2(self, p):
        '''
        parametro : parametro ABRE_COL FECHA_COL
        '''
        p[0] = Tree('parametro', [p[1]])
        g1.edge('parametro', 'parametro')

    def p_corpo(self, p):
        '''
        corpo : corpo acao
              | vazio
        '''
        if len(p) == 3:
            p[0] = Tree('corpo', [p[1], p[2]])
            g1.edge('corpo', 'acao')
        elif len(p) == 2:
            p[0] = Tree('corpo', [p[1]])

    def p_acao(self, p):
        '''
        acao : expressao
                    | declaracao_variaveis
                    | se
                    | repita
                    | leia
                    | escreva
                    | retorna
                    | error

        '''
        p[0] = Tree('acao', [p[1]])
        g1.edge('acao', str(p[1]))       

    def p_se(self, p):
        '''
            se : SE expressao ENTAO corpo FIM
                | SE expressao ENTAO corpo SENAO corpo FIM
        '''
        if len(p) == 6:
            p[0] = Tree('se', [p[2], p[4]])
            g1.edge('se', 'expressao')
            g1.edge('expressao', 'corpo')
        elif len(p) == 8:
            p[0] = Tree('se', [p[2], p[4], p[6]])
            g1.edge('se', 'expressao')
            g1.edge('expressao', 'corpo')
            g1.edge('corpo', 'corpo')

#    def p_se_error(self, p):
#        '''
#            se : SE expressao error corpo FIM
#               | error SENAO corpo FIM
#        '''
#        if len(p) == 6:
#            print("A expressão 'então' não foi definida.\n")
#        elif len(p) == 5:
#            print("Erro: Não foi definido a condição 'se'. \n")


    def p_repita(self, p):
        '''
            repita : REPITA corpo ate
        '''
        p[0] = Tree('repita', [p[2], p[3]])
        g1.edge('repita', 'corpo')
        g1.edge('corpo', 'expressao')

    def p_ate(self, p):
        ''' 
            ate : ATE expressao
        '''
        p[0] = Tree('ate', [p[2]])
        

#    def p_repita_error(self, p):
#        '''
#            repita : REPITA corpo error
#        '''
#        print ("Erro: Definições do laço REPITA incompletas! \n")


    def p_atribuicao(self, p):
        '''
            atribuicao : var ATRIBUT expressao
        '''
        if len(p):
            p[0] = Tree('atribuicao', [p[1], p[3]])
            g1.edge('atribuicao', 'var')
            g1.edge('var', 'expressao')

    def p_leia(self, p):
        '''
            leia : LEIA ABRE_PAR ID FECHA_PAR
        '''
        p[0] = Tree('leia', [], p[3])
        g1.edge('leia', p[3])

    def p_escreva(self, p):
        '''
            escreva : ESCREVA ABRE_PAR expressao FECHA_PAR
        '''
        p[0] = Tree('escreva', [p[3]])
        g1.edge('escreva', 'expressao')       
 
    def p_retorna(self, p):
        '''
            retorna : RETORNA ABRE_PAR expressao FECHA_PAR
        '''
        p[0] = Tree('retorna', [p[3]])
        g1.edge('retorna', 'expressao') 

    def p_expressao(self, p):
        '''
            expressao : expressao_logica
                        | atribuicao
        '''
        p[0] = Tree('expressao', [p[1]])
        g1.edge('expressao', str(p[1]))        

    def p_expressao_logica(self, p):
    	'''
            expressao_logica : expressao_simples
                             | expressao_logica operador_logico expressao_simples
        '''
    	if len(p) == 2:
            p[0] = Tree('expressao_logica', [p[1]])
            g1.edge('expressao_logica', 'expressao_simples')
    	elif len(p) == 4:
            p[0] = Tree('expressao_logica', [p[1], p[2], p[3]])
            g1.edge('expressao_logica', 'operador_logico')
            g1.edge('operador_logico', 'expressao_simples')


    def p_expressao_simples(self, p):
        '''
            expressao_simples : expressao_aditiva
                              | expressao_simples operador_relacional expressao_aditiva
        '''
        if len(p) == 2:
            p[0] = Tree('expressao_simples', [p[1]])
            g1.edge('expressao_simples', 'expressao_aditiva')
        elif len(p) == 4:
            p[0] = Tree('expressao_simples', [p[1], p[2], p[3]])
            g1.edge('expressao_simples', 'operador_relacional')
            g1.edge('operador_relacional', 'expressao_aditiva')

    def p_expressao_aditiva(self, p):
        '''
            expressao_aditiva : expressao_multiplicativa
                                | expressao_aditiva operador_soma expressao_multiplicativa
        '''
        if len(p) == 2:
            p[0] = Tree('expressao_aditiva', [p[1]])
            g1.edge('expressao_aditiva', 'expressao_multiplicativa')
        elif len(p) == 4:
            p[0] = Tree('expressao_aditiva', [p[1], p[2], p[3]])
            g1.edge('expressao_aditiva', 'operador_soma')
            g1.edge('operador_soma', 'expressao_multiplicativa')

    def p_expressao_multiplicativa(self, p):
        '''
           expressao_multiplicativa : expressao_unaria
                           | expressao_multiplicativa operador_multiplicacao expressao_unaria

        '''
        if len(p) == 2:
            p[0] = Tree('expressao_multiplicativa', [p[1]])
            g1.edge('expressao_multiplicativa', 'expressao_unaria')
        elif len(p) == 4:
            p[0] = Tree('expressao_multiplicativa', [p[1], p[2], p[3]])
            g1.edge('expressao_multiplicativa', 'operador_multiplicacao')
            g1.edge('operador_multiplicao', 'expressao_unaria')

    def p_expressao_unaria(self, p):
        '''
            expressao_unaria : fator
                            | operador_soma fator
        '''
        if len(p) == 2:
            p[0] = Tree('expressao_unaria', [p[1]])
            g1.edge('expressao_unaria', 'fator')
        else:
            p[0] = Tree('expressao_unaria', [p[1], p[2]])
            g1.edge('expressao_unaria', 'operador_soma')
            g1.edge('operador_soma', 'fator')

    def p_operador_relacional(self, p):
        '''
            operador_relacional : MENOR
                                | MAIOR
                                | IGUAL
                                | DIFERENCA
                                | MENOR_IGUAL
                                | MAIOR_IGUAL
                                | NEGACAO
        '''
        p[0] = Tree('operador_relacional', [], p[1])
        g1.edge('operador_relacional', p[1])

    def p_operador_logico(self, p):
        '''
            operador_logico : E_LOGICO
                            | OU_LOGICO

        '''
        p[0] = Tree('operador_logico', [], p[1])
        g1.edge('operador_logico', p[1])
  

    def p_operador_soma(self, p):
        '''
            operador_soma : SOMA
                          | SUB

        '''
        p[0] = Tree('operador_soma', [], p[1])
        g1.edge('operador_soma', p[1])

#   def p_operador_negacao(self, p):
#        '''
#            operador_negacao : NEGACAO
#        '''
#        p[0] = Tree('operador_negacao', [], p[1])
 
    def p_operador_multiplicacao(self, p):
        '''
            operador_multiplicacao : MULT
                                   | DIVISAO
        '''
        p[0] = Tree('operador_multiplicacao', [], p[1])
        g1.edge('operador_multiplicacao', p[1])

    def p_fator(self, p):
        '''
            fator : ABRE_COL expressao FECHA_COL
                  | var
                  | chamada_funcao
                  | numero
        '''
        if len(p) == 4:
            p[0] = Tree('fator', [p[2]])
            g1.edge('fator', 'expressao')
        else:
            p[0] = Tree('fator', [p[1]])
            g1.edge('fator', str(p[1]))
            
    def p_numero(self, p):
        '''
            numero : INTEIRO
                   | FLUTUANTE
                   | NOTACAO_CIENTIFICA
        '''
        p[0] = Tree('numero', [], p[1])
        g1.edge('numero', str(p[1]))

    def p_chamada_funcao(self, p):
        '''
            chamada_funcao : ID ABRE_PAR lista_argumentos FECHA_PAR
        '''
        p[0] = Tree('chamada_funcao', [p[3]], p[1])
        g1.edge('chamada_funcao', p[1])
        g1.edge(p[1], 'lista_argumentos')

    def p_lista_argumentos(self, p):
        '''
            lista_argumentos : lista_argumentos VIRGULA expressao
                            | expressao
                            | vazio
        '''
        if len(p) == 4:
            p[0] = Tree('lista_argumentos', [p[1], p[3]])
        else:
            p[0] = Tree('lista_argumentos', [p[1]])
        g1.edge('lista_argumentos', 'expressao')


    def p_vazio(self, p):
        '''
            vazio :
        '''
        #g1.node('vazio')

    def p_error(self, p):
        print(p)
        if p:
            print("Erro sintático: '%s', linha %d" % (p.value, p.lineno))
            exit(1)
        else:
            yacc.restart()
            print('Erro sintático: definições incompletas!')
            exit(1)


def prinTree(node, level=" "):
    if node != None and node.child != None:
        print("%s %s %s" % (level, node.type, node.value))
        for son in node.child:
            if (node.child != None):
                prinTree(son, level + " ")

if __name__ == '__main__':
    import io, sys
    lexemas = io.open(sys.argv[1], mode="r", encoding="utf-8")
    arvore = Syntax(lexemas.read())
    prinTree(arvore.ast)
    #print("\narvore abstrata\n")
    #print(g1.source)
    filename = g1.render(filename='img/asa')

    lexemas.close()
