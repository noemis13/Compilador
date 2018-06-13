
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALNEGACAOMENOR_IGUALMAIORMAIOR_IGUALMENORE_LOGICOOU_LOGICOleftSOMASUBleftMULTDIVISAODIVISAO MULT VIRGULA ATRIBUT MENOR MAIOR IGUAL MENOR_IGUAL MAIOR_IGUAL ABRE_PAR FECHA_PAR DOIS_PONTOS SOMA SUB DIFERENCA ABRE_COL FECHA_COL NOTACAO_CIENTIFICA ID E_LOGICO OU_LOGICO NEGACAO LEIA ENTAO REPITA INTEIRO FLUTUANTE SENAO SE ESCREVA ATE FIM RETORNA\n        programa : lista_declaracoes\n                     \n        lista_declaracoes : lista_declaracoes declaracao\n                           | declaracao\n\t\t\t   | error\n        \n        declaracao : declaracao_variaveis\n                    | inicializacao_variaveis\n                    | declaracao_funcao\n        \n        declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n        \n        declaracao_variaveis : tipo DOIS_PONTOS error\n        \n        inicializacao_variaveis : atribuicao\n        \n        lista_variaveis : var VIRGULA lista_variaveis\n                        | var\n        \n        var : ID\n            | ID indice\n        \n        indice : indice ABRE_COL expressao FECHA_COL\n               | ABRE_COL expressao FECHA_COL\n        \n        tipo : INTEIRO\n\t     | FLUTUANTE\n        \n        declaracao_funcao : tipo cabecalho\n                        | cabecalho\n        \n        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM\n        \n        lista_parametros : lista_parametros VIRGULA parametro\n                            | parametro\n                            | vazio\n        \n        parametro : tipo DOIS_PONTOS ID\n        \n        parametro : parametro ABRE_COL FECHA_COL\n        \n        corpo : corpo acao\n                | vazio\n        \n        acao : expressao\n                    | declaracao_variaveis\n                    | se\n                    | repita\n                    | leia\n                    | escreva\n                    | retorna\n                    | error\n\n        \n            se : SE expressao ENTAO corpo FIM\n                | SE expressao ENTAO corpo SENAO corpo FIM\n        \n            repita : REPITA corpo ATE expressao\n        \n            atribuicao : var ATRIBUT expressao\n        \n            leia : LEIA ABRE_PAR ID FECHA_PAR\n        \n            escreva : ESCREVA ABRE_PAR expressao FECHA_PAR\n        \n            retorna : RETORNA ABRE_PAR expressao FECHA_PAR\n        \n            expressao : expressao_logica\n                        | atribuicao\n        \n            expressao_logica : expressao_simples\n                             | expressao_logica operador_logico expressao_simples\n        \n            expressao_simples : expressao_aditiva\n                              | expressao_simples operador_relacional expressao_aditiva\n        \n            expressao_aditiva : expressao_multiplicativa\n                                | expressao_aditiva operador_soma expressao_multiplicativa\n        \n           expressao_multiplicativa : expressao_unaria\n                           | expressao_multiplicativa operador_multiplicacao expressao_unaria\n\n        \n\n            expressao_unaria : fator\n                            | operador_soma fator\n\n        \n            operador_relacional : MENOR\n                                | MAIOR\n                                | IGUAL\n                                | DIFERENCA\n                                | MENOR_IGUAL\n                                | MAIOR_IGUAL\n                                | NEGACAO\n        \n            operador_logico : E_LOGICO\n                            | OU_LOGICO\n\n        \n            operador_soma : SOMA\n                          | SUB\n\n        \n            operador_multiplicacao : MULT\n                                    | DIVISAO\n        \n            fator : ABRE_COL  expressao FECHA_COL\n                    | var\n                    | chamada_funcao\n                    | numero\n        \n            numero : INTEIRO\n                    | FLUTUANTE\n                    | NOTACAO_CIENTIFICA\n        \n            chamada_funcao : ID ABRE_PAR lista_argumentos FECHA_PAR\n        \n            lista_argumentos : lista_argumentos VIRGULA expressao\n                            | expressao\n                            | vazio\n        \n            vazio :\n        '
    
_lr_action_items = {'DIFERENCA':([18,27,29,31,32,33,34,35,36,37,42,44,45,65,74,75,83,84,88,89,90,91,93,105,111,],[-14,-72,-73,-48,-54,-13,-70,-75,-71,-50,66,-52,-74,-16,-55,-70,-69,-51,-53,66,-49,-15,-74,-73,-76,]),'MENOR':([18,27,29,31,32,33,34,35,36,37,42,44,45,65,74,75,83,84,88,89,90,91,93,105,111,],[-14,-72,-73,-48,-54,-13,-70,-75,-71,-50,72,-52,-74,-16,-55,-70,-69,-51,-53,72,-49,-15,-74,-73,-76,]),'ESCREVA':([18,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,49,50,51,52,65,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,110,111,117,121,124,125,126,127,128,129,130,131,132,],[-14,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,-8,-12,-9,-80,-16,-55,-70,-28,106,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,-80,-76,106,-80,-41,-42,106,-43,-39,-80,-37,106,-38,]),'ABRE_COL':([5,17,18,19,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,80,81,82,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,107,110,111,112,114,116,117,121,123,124,125,126,127,128,129,130,131,132,],[17,28,46,28,55,-72,28,-73,-45,-48,-54,17,-70,-75,-71,-50,-44,-66,-65,-46,28,-52,-74,28,-40,17,-8,-12,-9,-80,28,28,-68,-67,28,-64,-63,28,-16,-59,28,-57,-60,-58,-62,-56,-61,-55,-70,-28,28,55,-25,-26,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,28,-80,-76,28,28,28,28,-80,28,-41,-42,28,-43,-39,-80,-37,28,-38,]),'INTEIRO':([0,2,3,4,7,8,9,10,13,15,16,17,18,19,22,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,107,110,111,112,114,116,117,121,123,124,125,126,127,128,129,130,131,132,],[1,-10,1,-20,-4,-5,-6,-7,-3,-2,1,29,-14,29,-19,-72,29,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-66,-65,-46,29,-52,-74,29,-40,-13,-8,-12,-9,-80,1,29,29,-68,-67,29,-64,-63,29,-16,-59,29,-57,-60,-58,-62,-56,-61,-55,-70,-28,105,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-21,-29,-35,-27,-31,-32,-73,29,-80,-76,29,29,29,105,-80,29,-41,-42,105,-43,-39,-80,-37,105,-38,]),'FLUTUANTE':([0,2,3,4,7,8,9,10,13,15,16,17,18,19,22,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,107,110,111,112,114,116,117,121,123,124,125,126,127,128,129,130,131,132,],[12,-10,12,-20,-4,-5,-6,-7,-3,-2,12,45,-14,45,-19,-72,45,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-66,-65,-46,45,-52,-74,45,-40,-13,-8,-12,-9,-80,12,45,45,-68,-67,45,-64,-63,45,-16,-59,45,-57,-60,-58,-62,-56,-61,-55,-70,-28,93,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-21,-29,-35,-27,-31,-32,-73,45,-80,-76,45,45,45,93,-80,45,-41,-42,93,-43,-39,-80,-37,93,-38,]),'NEGACAO':([18,27,29,31,32,33,34,35,36,37,42,44,45,65,74,75,83,84,88,89,90,91,93,105,111,],[-14,-72,-73,-48,-54,-13,-70,-75,-71,-50,71,-52,-74,-16,-55,-70,-69,-51,-53,71,-49,-15,-74,-73,-76,]),'E_LOGICO':([18,27,29,31,32,33,34,35,36,37,38,42,44,45,65,74,75,83,84,88,89,90,91,93,105,111,],[-14,-72,-73,-48,-54,-13,-70,-75,-71,-50,63,-46,-52,-74,-16,-55,-70,-69,-51,-53,-47,-49,-15,-74,-73,-76,]),'VIRGULA':([16,18,23,24,26,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,50,58,65,74,75,80,81,82,83,84,85,86,87,88,89,90,91,111,118,],[-80,-14,-24,53,-23,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,77,-80,-16,-55,-70,-22,-25,-26,-69,-51,112,-78,-79,-53,-47,-49,-15,-76,-77,]),'ID':([0,1,2,3,4,7,8,9,10,12,13,14,15,17,18,19,21,22,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,54,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,77,78,79,83,84,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,107,110,111,112,113,114,116,117,121,123,124,125,126,127,128,129,130,131,132,],[5,-17,-10,5,-20,-4,-5,-6,-7,-18,-3,20,-2,33,-14,33,48,-19,-72,33,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-66,-65,-46,33,-52,-74,33,-40,-13,-8,-12,-9,-80,81,33,33,-68,-67,33,-64,-63,33,-16,-59,33,-57,-60,-58,-62,-56,-61,-55,-70,48,-28,33,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-21,-29,-35,-27,-31,-32,-73,33,-80,-76,33,119,33,33,33,-80,33,-41,-42,33,-43,-39,-80,-37,33,-38,]),'SENAO':([18,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,49,50,51,65,74,75,78,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,111,121,124,125,126,127,128,130,132,],[-14,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,-8,-12,-9,-16,-55,-70,-28,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,-76,-80,-41,-42,129,-43,-39,-37,-38,]),'OU_LOGICO':([18,27,29,31,32,33,34,35,36,37,38,42,44,45,65,74,75,83,84,88,89,90,91,93,105,111,],[-14,-72,-73,-48,-54,-13,-70,-75,-71,-50,62,-46,-52,-74,-16,-55,-70,-69,-51,-53,-47,-49,-15,-74,-73,-76,]),'ATRIBUT':([5,6,18,33,34,65,91,],[-13,19,-14,-13,19,-16,-15,]),'MENOR_IGUAL':([18,27,29,31,32,33,34,35,36,37,42,44,45,65,74,75,83,84,88,89,90,91,93,105,111,],[-14,-72,-73,-48,-54,-13,-70,-75,-71,-50,69,-52,-74,-16,-55,-70,-69,-51,-53,69,-49,-15,-74,-73,-76,]),'IGUAL':([18,27,29,31,32,33,34,35,36,37,42,44,45,65,74,75,83,84,88,89,90,91,93,105,111,],[-14,-72,-73,-48,-54,-13,-70,-75,-71,-50,70,-52,-74,-16,-55,-70,-69,-51,-53,70,-49,-15,-74,-73,-76,]),'NOTACAO_CIENTIFICA':([17,18,19,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,107,110,111,112,114,116,117,121,123,124,125,126,127,128,129,130,131,132,],[35,-14,35,-72,35,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-66,-65,-46,35,-52,-74,35,-40,-13,-8,-12,-9,-80,35,35,-68,-67,35,-64,-63,35,-16,-59,35,-57,-60,-58,-62,-56,-61,-55,-70,-28,35,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,35,-80,-76,35,35,35,35,-80,35,-41,-42,35,-43,-39,-80,-37,35,-38,]),'LEIA':([18,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,49,50,51,52,65,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,110,111,117,121,124,125,126,127,128,129,130,131,132,],[-14,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,-8,-12,-9,-80,-16,-55,-70,-28,104,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,-80,-76,104,-80,-41,-42,104,-43,-39,-80,-37,104,-38,]),'DOIS_PONTOS':([1,12,14,25,93,105,108,],[-17,-18,21,54,-18,-17,21,]),'FECHA_COL':([18,27,29,30,31,32,33,34,35,36,37,38,40,42,44,45,47,55,56,65,74,75,76,83,84,88,89,90,91,111,],[-14,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,65,-46,-52,-74,-40,82,83,-16,-55,-70,91,-69,-51,-53,-47,-49,-15,-76,]),'ATE':([18,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,49,50,51,65,74,75,78,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,110,111,117,124,125,127,128,130,132,],[-14,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,-8,-12,-9,-16,-55,-70,-28,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,-80,-76,123,-41,-42,-43,-39,-37,-38,]),'SE':([18,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,49,50,51,52,65,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,110,111,117,121,124,125,126,127,128,129,130,131,132,],[-14,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,-8,-12,-9,-80,-16,-55,-70,-28,107,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,-80,-76,107,-80,-41,-42,107,-43,-39,-80,-37,107,-38,]),'FECHA_PAR':([16,18,23,24,26,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,58,65,74,75,80,81,82,83,84,85,86,87,88,89,90,91,111,118,119,120,122,],[-80,-14,-24,52,-23,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-80,-16,-55,-70,-22,-25,-26,-69,-51,111,-78,-79,-53,-47,-49,-15,-76,-77,124,125,127,]),'FIM':([18,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,49,50,51,52,65,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,111,121,124,125,126,127,128,129,130,131,132,],[-14,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,-8,-12,-9,-80,-16,-55,-70,-28,98,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,-76,-80,-41,-42,130,-43,-39,-80,-37,132,-38,]),'SUB':([17,18,19,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,44,45,46,47,48,49,50,51,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,107,110,111,112,114,116,117,121,123,124,125,126,127,128,129,130,131,132,],[39,-14,39,-72,39,-73,-45,39,-54,-13,-70,-75,-71,-50,-44,-66,-65,-46,-52,-74,39,-40,-13,-8,-12,-9,-80,39,39,-68,-67,39,-64,-63,39,-16,-59,39,-57,-60,-58,-62,-56,-61,-55,-70,-28,39,-69,-51,-53,-47,39,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,39,-80,-76,39,39,39,39,-80,39,-41,-42,39,-43,-39,-80,-37,39,-38,]),'SOMA':([17,18,19,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,44,45,46,47,48,49,50,51,52,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,107,110,111,112,114,116,117,121,123,124,125,126,127,128,129,130,131,132,],[41,-14,41,-72,41,-73,-45,41,-54,-13,-70,-75,-71,-50,-44,-66,-65,-46,-52,-74,41,-40,-13,-8,-12,-9,-80,41,41,-68,-67,41,-64,-63,41,-16,-59,41,-57,-60,-58,-62,-56,-61,-55,-70,-28,41,-69,-51,-53,-47,41,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,41,-80,-76,41,41,41,41,-80,41,-41,-42,41,-43,-39,-80,-37,41,-38,]),'ABRE_PAR':([5,20,33,104,106,109,],[16,16,58,113,114,116,]),'error':([0,18,21,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,49,50,51,52,65,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,110,111,117,121,124,125,126,127,128,129,130,131,132,],[7,-14,51,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,-8,-12,-9,-80,-16,-55,-70,-28,94,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,-80,-76,94,-80,-41,-42,94,-43,-39,-80,-37,94,-38,]),'DIVISAO':([18,27,29,32,33,34,35,36,37,44,45,65,74,75,83,84,88,91,93,105,111,],[-14,-72,-73,-54,-13,-70,-75,-71,59,-52,-74,-16,-55,-70,-69,59,-53,-15,-74,-73,-76,]),'$end':([2,3,4,7,8,9,10,11,13,15,18,22,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,49,50,51,65,74,75,83,84,88,89,90,91,92,98,111,],[-10,-1,-20,-4,-5,-6,-7,0,-3,-2,-14,-19,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,-8,-12,-9,-16,-55,-70,-69,-51,-53,-47,-49,-15,-11,-21,-76,]),'ENTAO':([18,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,65,74,75,83,84,88,89,90,91,111,115,],[-14,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-16,-55,-70,-69,-51,-53,-47,-49,-15,-76,121,]),'MAIOR_IGUAL':([18,27,29,31,32,33,34,35,36,37,42,44,45,65,74,75,83,84,88,89,90,91,93,105,111,],[-14,-72,-73,-48,-54,-13,-70,-75,-71,-50,73,-52,-74,-16,-55,-70,-69,-51,-53,73,-49,-15,-74,-73,-76,]),'MULT':([18,27,29,32,33,34,35,36,37,44,45,65,74,75,83,84,88,91,93,105,111,],[-14,-72,-73,-54,-13,-70,-75,-71,60,-52,-74,-16,-55,-70,-69,60,-53,-15,-74,-73,-76,]),'MAIOR':([18,27,29,31,32,33,34,35,36,37,42,44,45,65,74,75,83,84,88,89,90,91,93,105,111,],[-14,-72,-73,-48,-54,-13,-70,-75,-71,-50,68,-52,-74,-16,-55,-70,-69,-51,-53,68,-49,-15,-74,-73,-76,]),'RETORNA':([18,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,49,50,51,52,65,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,110,111,117,121,124,125,126,127,128,129,130,131,132,],[-14,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,-8,-12,-9,-80,-16,-55,-70,-28,109,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,-80,-76,109,-80,-41,-42,109,-43,-39,-80,-37,109,-38,]),'REPITA':([18,27,29,30,31,32,33,34,35,36,37,38,42,44,45,47,48,49,50,51,52,65,74,75,78,79,83,84,88,89,90,91,92,93,94,95,96,97,99,100,101,102,103,105,110,111,117,121,124,125,126,127,128,129,130,131,132,],[-14,-72,-73,-45,-48,-54,-13,-70,-75,-71,-50,-44,-46,-52,-74,-40,-13,-8,-12,-9,-80,-16,-55,-70,-28,110,-69,-51,-53,-47,-49,-15,-11,-74,-36,-30,-34,-33,-29,-35,-27,-31,-32,-73,-80,-76,110,-80,-41,-42,110,-43,-39,-80,-37,110,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'repita':([79,117,126,131,],[103,103,103,103,]),'retorna':([79,117,126,131,],[100,100,100,100,]),'numero':([17,19,28,43,46,57,58,61,64,67,79,107,112,114,116,117,123,126,131,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'declaracao_funcao':([0,3,],[10,10,]),'atribuicao':([0,3,17,19,28,46,58,79,107,112,114,116,117,123,126,131,],[2,2,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'se':([79,117,126,131,],[102,102,102,102,]),'expressao_aditiva':([17,19,28,46,58,64,67,79,107,112,114,116,117,123,126,131,],[31,31,31,31,31,31,90,31,31,31,31,31,31,31,31,31,]),'cabecalho':([0,3,14,],[4,4,22,]),'fator':([17,19,28,43,46,57,58,61,64,67,79,107,112,114,116,117,123,126,131,],[32,32,32,74,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'declaracao_variaveis':([0,3,79,117,126,131,],[8,8,95,95,95,95,]),'operador_relacional':([42,89,],[67,67,]),'lista_variaveis':([21,77,],[49,92,]),'corpo':([52,110,121,129,],[79,117,126,131,]),'var':([0,3,17,19,21,28,43,46,57,58,61,64,67,77,79,107,112,114,116,117,123,126,131,],[6,6,34,34,50,34,75,34,75,34,75,75,75,50,34,34,34,34,34,34,34,34,34,]),'lista_declaracoes':([0,],[3,]),'lista_argumentos':([58,],[85,]),'chamada_funcao':([17,19,28,43,46,57,58,61,64,67,79,107,112,114,116,117,123,126,131,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'expressao_multiplicativa':([17,19,28,46,57,58,64,67,79,107,112,114,116,117,123,126,131,],[37,37,37,37,84,37,37,37,37,37,37,37,37,37,37,37,37,]),'escreva':([79,117,126,131,],[96,96,96,96,]),'operador_soma':([17,19,28,31,46,57,58,61,64,67,79,90,107,112,114,116,117,123,126,131,],[43,43,43,57,43,43,43,43,43,43,43,57,43,43,43,43,43,43,43,43,]),'inicializacao_variaveis':([0,3,],[9,9,]),'acao':([79,117,126,131,],[101,101,101,101,]),'operador_multiplicacao':([37,84,],[61,61,]),'expressao':([17,19,28,46,58,79,107,112,114,116,117,123,126,131,],[40,47,56,76,86,99,115,118,120,122,99,128,99,99,]),'vazio':([16,52,58,110,121,129,],[23,78,87,78,78,78,]),'programa':([0,],[11,]),'indice':([5,33,48,],[18,18,18,]),'expressao_simples':([17,19,28,46,58,64,79,107,112,114,116,117,123,126,131,],[42,42,42,42,42,89,42,42,42,42,42,42,42,42,42,]),'expressao_logica':([17,19,28,46,58,79,107,112,114,116,117,123,126,131,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'declaracao':([0,3,],[13,15,]),'operador_logico':([38,],[64,]),'lista_parametros':([16,],[24,]),'leia':([79,117,126,131,],[97,97,97,97,]),'expressao_unaria':([17,19,28,46,57,58,61,64,67,79,107,112,114,116,117,123,126,131,],[44,44,44,44,44,44,88,44,44,44,44,44,44,44,44,44,44,44,]),'tipo':([0,3,16,53,79,117,126,131,],[14,14,25,25,108,108,108,108,]),'parametro':([16,53,],[26,80,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','syntax.py',35),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','syntax.py',41),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','syntax.py',42),
  ('lista_declaracoes -> error','lista_declaracoes',1,'p_lista_declaracoes','syntax.py',43),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','syntax.py',55),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','syntax.py',56),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','syntax.py',57),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','syntax.py',63),
  ('declaracao_variaveis -> tipo DOIS_PONTOS error','declaracao_variaveis',3,'p_declaracao_variaveis_error','syntax.py',69),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','syntax.py',76),
  ('lista_variaveis -> var VIRGULA lista_variaveis','lista_variaveis',3,'p_lista_variaveis','syntax.py',82),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','syntax.py',83),
  ('var -> ID','var',1,'p_var','syntax.py',92),
  ('var -> ID indice','var',2,'p_var','syntax.py',93),
  ('indice -> indice ABRE_COL expressao FECHA_COL','indice',4,'p_indice','syntax.py',102),
  ('indice -> ABRE_COL expressao FECHA_COL','indice',3,'p_indice','syntax.py',103),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','syntax.py',124),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo','syntax.py',125),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','syntax.py',131),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','syntax.py',132),
  ('cabecalho -> ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM','cabecalho',6,'p_cabecalho','syntax.py',141),
  ('lista_parametros -> lista_parametros VIRGULA parametro','lista_parametros',3,'p_lista_parametros','syntax.py',155),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','syntax.py',156),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','syntax.py',157),
  ('parametro -> tipo DOIS_PONTOS ID','parametro',3,'p_parametro1','syntax.py',166),
  ('parametro -> parametro ABRE_COL FECHA_COL','parametro',3,'p_parametro2','syntax.py',172),
  ('corpo -> corpo acao','corpo',2,'p_corpo','syntax.py',178),
  ('corpo -> vazio','corpo',1,'p_corpo','syntax.py',179),
  ('acao -> expressao','acao',1,'p_acao','syntax.py',188),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','syntax.py',189),
  ('acao -> se','acao',1,'p_acao','syntax.py',190),
  ('acao -> repita','acao',1,'p_acao','syntax.py',191),
  ('acao -> leia','acao',1,'p_acao','syntax.py',192),
  ('acao -> escreva','acao',1,'p_acao','syntax.py',193),
  ('acao -> retorna','acao',1,'p_acao','syntax.py',194),
  ('acao -> error','acao',1,'p_acao','syntax.py',195),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','syntax.py',202),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','syntax.py',203),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','syntax.py',223),
  ('atribuicao -> var ATRIBUT expressao','atribuicao',3,'p_atribuicao','syntax.py',236),
  ('leia -> LEIA ABRE_PAR ID FECHA_PAR','leia',4,'p_leia','syntax.py',243),
  ('escreva -> ESCREVA ABRE_PAR expressao FECHA_PAR','escreva',4,'p_escreva','syntax.py',249),
  ('retorna -> RETORNA ABRE_PAR expressao FECHA_PAR','retorna',4,'p_retorna','syntax.py',255),
  ('expressao -> expressao_logica','expressao',1,'p_expressao','syntax.py',261),
  ('expressao -> atribuicao','expressao',1,'p_expressao','syntax.py',262),
  ('expressao_logica -> expressao_simples','expressao_logica',1,'p_expressao_logica','syntax.py',269),
  ('expressao_logica -> expressao_logica operador_logico expressao_simples','expressao_logica',3,'p_expressao_logica','syntax.py',270),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','syntax.py',280),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','syntax.py',281),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','syntax.py',290),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','syntax.py',291),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','syntax.py',300),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','syntax.py',301),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','syntax.py',312),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','syntax.py',313),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','syntax.py',323),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','syntax.py',324),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',325),
  ('operador_relacional -> DIFERENCA','operador_relacional',1,'p_operador_relacional','syntax.py',326),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',327),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',328),
  ('operador_relacional -> NEGACAO','operador_relacional',1,'p_operador_relacional','syntax.py',329),
  ('operador_logico -> E_LOGICO','operador_logico',1,'p_operador_logico','syntax.py',335),
  ('operador_logico -> OU_LOGICO','operador_logico',1,'p_operador_logico','syntax.py',336),
  ('operador_soma -> SOMA','operador_soma',1,'p_operador_soma','syntax.py',344),
  ('operador_soma -> SUB','operador_soma',1,'p_operador_soma','syntax.py',345),
  ('operador_multiplicacao -> MULT','operador_multiplicacao',1,'p_operador_multiplicacao','syntax.py',359),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','syntax.py',360),
  ('fator -> ABRE_COL expressao FECHA_COL','fator',3,'p_fator','syntax.py',366),
  ('fator -> var','fator',1,'p_fator','syntax.py',367),
  ('fator -> chamada_funcao','fator',1,'p_fator','syntax.py',368),
  ('fator -> numero','fator',1,'p_fator','syntax.py',369),
  ('numero -> INTEIRO','numero',1,'p_numero','syntax.py',378),
  ('numero -> FLUTUANTE','numero',1,'p_numero','syntax.py',379),
  ('numero -> NOTACAO_CIENTIFICA','numero',1,'p_numero','syntax.py',380),
  ('chamada_funcao -> ID ABRE_PAR lista_argumentos FECHA_PAR','chamada_funcao',4,'p_chamada_funcao','syntax.py',386),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','syntax.py',392),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','syntax.py',393),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','syntax.py',394),
  ('vazio -> <empty>','vazio',0,'p_vazio','syntax.py',403),
]
