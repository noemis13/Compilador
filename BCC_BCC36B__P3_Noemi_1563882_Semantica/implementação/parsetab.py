
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALNEGACAOMENOR_IGUALMAIORMAIOR_IGUALMENORE_LOGICOOU_LOGICOleftSOMASUBleftMULTDIVISAODIVISAO MULT VIRGULA ATRIBUT MENOR MAIOR IGUAL MENOR_IGUAL MAIOR_IGUAL ABRE_PAR FECHA_PAR DOIS_PONTOS SOMA SUB DIFERENCA ABRE_COL FECHA_COL NOTACAO_CIENTIFICA ID E_LOGICO OU_LOGICO NEGACAO SENAO FLUTUANTE LEIA ENTAO INTEIRO ATE FIM REPITA RETORNA SE ESCREVA\n        programa : lista_declaracoes\n                     \n        lista_declaracoes : lista_declaracoes declaracao\n                          | declaracao\n                         | error\n        \n        declaracao : declaracao_variaveis\n                   | inicializacao_variaveis\n                   | declaracao_funcao\n        \n        declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n        \n        declaracao_variaveis : tipo DOIS_PONTOS error\n        \n        inicializacao_variaveis : atribuicao\n        \n        lista_variaveis : var VIRGULA lista_variaveis\n                        | var\n        \n        var : ID\n            | ID indice\n        \n        indice : indice ABRE_COL expressao FECHA_COL\n               | ABRE_COL expressao FECHA_COL\n        \n        tipo : INTEIRO\n\t     | FLUTUANTE\n        \n        declaracao_funcao : tipo cabecalho\n                          | cabecalho\n        \n        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM\n        \n        lista_parametros : lista_parametros VIRGULA parametro\n                         | parametro\n                         | vazio\n        \n        parametro : tipo DOIS_PONTOS ID\n        \n        parametro : parametro ABRE_COL FECHA_COL\n        \n        corpo : corpo acao\n              | vazio\n        \n        acao : expressao\n                    | declaracao_variaveis\n                    | se\n                    | repita\n                    | leia\n                    | escreva\n                    | retorna\n                    | error\n\n        \n            se : SE expressao ENTAO corpo FIM\n                | SE expressao ENTAO corpo SENAO corpo FIM\n        \n            repita : REPITA corpo ATE expressao\n        \n            atribuicao : var ATRIBUT expressao\n        \n            leia : LEIA ABRE_PAR ID FECHA_PAR\n        \n            escreva : ESCREVA ABRE_PAR expressao FECHA_PAR\n        \n            retorna : RETORNA ABRE_PAR expressao FECHA_PAR\n        \n            expressao : expressao_logica\n                        | atribuicao\n        \n            expressao_logica : expressao_simples\n                             | expressao_logica operador_logico expressao_simples\n        \n            expressao_simples : expressao_aditiva\n                              | expressao_simples operador_relacional expressao_aditiva\n        \n            expressao_aditiva : expressao_multiplicativa\n                                | expressao_aditiva operador_soma expressao_multiplicativa\n        \n           expressao_multiplicativa : expressao_unaria\n                           | expressao_multiplicativa operador_multiplicacao expressao_unaria\n\n        \n            expressao_unaria : fator\n                            | operador_soma fator\n        \n            operador_relacional : MENOR\n                                | MAIOR\n                                | IGUAL\n                                | DIFERENCA\n                                | MENOR_IGUAL\n                                | MAIOR_IGUAL\n                                | NEGACAO\n        \n            operador_logico : E_LOGICO\n                            | OU_LOGICO\n\n        \n            operador_soma : SOMA\n                          | SUB\n\n        \n            operador_multiplicacao : MULT\n                                   | DIVISAO\n        \n            fator : ABRE_COL expressao FECHA_COL\n                  | var\n                  | chamada_funcao\n                  | numero\n        \n            numero : INTEIRO\n                   | FLUTUANTE\n                   | NOTACAO_CIENTIFICA\n        \n            chamada_funcao : ID ABRE_PAR lista_argumentos FECHA_PAR\n        \n            lista_argumentos : lista_argumentos VIRGULA expressao\n                            | expressao\n                            | vazio\n        \n            vazio :\n        '
    
_lr_action_items = {'ATE':([19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,43,44,45,57,58,77,78,79,80,81,82,86,87,91,94,96,97,98,100,102,103,104,105,106,108,110,111,117,125,126,127,128,130,132,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-12,-9,-13,-8,-55,-70,-16,-51,-53,-69,-47,-49,-11,-15,-28,-76,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,122,-42,-43,-39,-41,-37,-38,]),'RETORNA':([19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,43,44,45,57,58,76,77,78,79,80,81,82,86,87,91,92,94,96,97,98,100,102,103,104,105,106,108,110,111,117,119,124,125,126,127,128,129,130,131,132,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-12,-9,-13,-8,-55,-70,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,101,-76,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,101,-80,101,-42,-43,-39,-41,-80,-37,101,-38,]),'E_LOGICO':([19,23,24,25,26,28,29,31,32,33,35,37,40,41,57,58,77,78,79,80,81,82,87,94,102,105,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,60,-46,-13,-75,-52,-55,-70,-16,-51,-53,-69,-47,-49,-15,-76,-74,-73,]),'SE':([19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,43,44,45,57,58,76,77,78,79,80,81,82,86,87,91,92,94,96,97,98,100,102,103,104,105,106,108,110,111,117,119,124,125,126,127,128,129,130,131,132,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-12,-9,-13,-8,-55,-70,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,95,-76,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,95,-80,95,-42,-43,-39,-41,-80,-37,95,-38,]),'DIVISAO':([19,24,25,26,28,29,31,32,37,40,41,57,58,77,78,79,80,87,94,102,105,],[-14,-54,-72,53,-70,-74,-73,-71,-13,-75,-52,-55,-70,-16,53,-53,-69,-15,-76,-74,-73,]),'ESCREVA':([19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,43,44,45,57,58,76,77,78,79,80,81,82,86,87,91,92,94,96,97,98,100,102,103,104,105,106,108,110,111,117,119,124,125,126,127,128,129,130,131,132,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-12,-9,-13,-8,-55,-70,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,99,-76,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,99,-80,99,-42,-43,-39,-41,-80,-37,99,-38,]),'ABRE_COL':([12,15,19,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,49,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,76,77,78,79,80,81,82,86,87,88,89,90,91,92,93,94,95,96,97,98,100,102,103,104,105,106,108,110,111,115,116,117,119,122,124,125,126,127,128,129,130,131,132,],[21,27,46,27,-48,-54,-72,-50,27,-70,-74,27,-73,-71,-44,-65,-46,-66,21,-45,-40,-75,-52,-12,-9,21,-8,27,74,27,-68,27,-67,-55,-70,-64,-63,27,-59,27,-62,-56,-57,-60,-61,-58,27,-80,-16,-51,-53,-69,-47,-49,-11,-15,-25,-26,74,-28,27,27,-76,27,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,27,27,27,-80,27,27,-42,-43,-39,-41,-80,-37,27,-38,]),'MENOR_IGUAL':([19,23,24,25,26,28,29,31,32,35,37,40,41,57,58,77,78,79,80,81,82,87,94,102,105,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,67,-13,-75,-52,-55,-70,-16,-51,-53,-69,67,-49,-15,-76,-74,-73,]),'FLUTUANTE':([0,1,4,5,8,10,11,13,14,15,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,75,76,77,78,79,80,81,82,86,87,91,92,93,94,95,96,97,98,100,102,103,104,105,106,108,110,111,112,115,116,117,119,122,124,125,126,127,128,129,130,131,132,],[7,-5,-20,-4,-3,-7,-6,-10,7,29,-19,-14,7,29,-2,-48,-54,-72,-50,29,-70,-74,29,-73,-71,-44,-65,-46,-66,-13,-45,-40,-75,-52,-12,-9,-13,-8,29,29,-68,29,-67,-55,-70,-64,-63,29,-59,29,-62,-56,-57,-60,-61,-58,29,7,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,102,29,-76,29,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,-21,29,29,102,-80,29,102,-42,-43,-39,-41,-80,-37,102,-38,]),'SENAO':([19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,43,44,45,57,58,77,78,79,80,81,82,86,87,91,94,96,97,98,100,102,103,104,105,108,110,111,119,124,125,126,127,128,130,132,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-12,-9,-13,-8,-55,-70,-16,-51,-53,-69,-47,-49,-11,-15,-28,-76,-27,-30,-31,-33,-74,-32,-36,-73,-34,-35,-29,-80,129,-42,-43,-39,-41,-37,-38,]),'$end':([1,2,4,5,8,10,11,13,14,17,19,22,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,43,44,45,57,58,77,78,79,80,81,82,86,87,94,112,],[-5,0,-20,-4,-3,-7,-6,-10,-1,-19,-14,-2,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-12,-9,-13,-8,-55,-70,-16,-51,-53,-69,-47,-49,-11,-15,-76,-21,]),'DOIS_PONTOS':([6,7,9,47,102,105,109,],[-17,-18,16,73,-18,-17,16,]),'NEGACAO':([19,23,24,25,26,28,29,31,32,35,37,40,41,57,58,77,78,79,80,81,82,87,94,102,105,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,64,-13,-75,-52,-55,-70,-16,-51,-53,-69,64,-49,-15,-76,-74,-73,]),'error':([0,16,19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,43,44,45,57,58,76,77,78,79,80,81,82,86,87,91,92,94,96,97,98,100,102,103,104,105,106,108,110,111,117,119,124,125,126,127,128,129,130,131,132,],[5,43,-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-12,-9,-13,-8,-55,-70,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,104,-76,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,104,-80,104,-42,-43,-39,-41,-80,-37,104,-38,]),'INTEIRO':([0,1,4,5,8,10,11,13,14,15,17,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,75,76,77,78,79,80,81,82,86,87,91,92,93,94,95,96,97,98,100,102,103,104,105,106,108,110,111,112,115,116,117,119,122,124,125,126,127,128,129,130,131,132,],[6,-5,-20,-4,-3,-7,-6,-10,6,31,-19,-14,6,31,-2,-48,-54,-72,-50,31,-70,-74,31,-73,-71,-44,-65,-46,-66,-13,-45,-40,-75,-52,-12,-9,-13,-8,31,31,-68,31,-67,-55,-70,-64,-63,31,-59,31,-62,-56,-57,-60,-61,-58,31,6,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,105,31,-76,31,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,-21,31,31,105,-80,31,105,-42,-43,-39,-41,-80,-37,105,-38,]),'REPITA':([19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,43,44,45,57,58,76,77,78,79,80,81,82,86,87,91,92,94,96,97,98,100,102,103,104,105,106,108,110,111,117,119,124,125,126,127,128,129,130,131,132,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-12,-9,-13,-8,-55,-70,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,106,-76,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,106,-80,106,-42,-43,-39,-41,-80,-37,106,-38,]),'LEIA':([19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,43,44,45,57,58,76,77,78,79,80,81,82,86,87,91,92,94,96,97,98,100,102,103,104,105,106,108,110,111,117,119,124,125,126,127,128,129,130,131,132,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-12,-9,-13,-8,-55,-70,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,107,-76,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,107,-80,107,-42,-43,-39,-41,-80,-37,107,-38,]),'MAIOR_IGUAL':([19,23,24,25,26,28,29,31,32,35,37,40,41,57,58,77,78,79,80,81,82,87,94,102,105,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,68,-13,-75,-52,-55,-70,-16,-51,-53,-69,68,-49,-15,-76,-74,-73,]),'SOMA':([15,19,21,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,76,77,78,79,80,81,82,86,87,91,92,93,94,95,96,97,98,100,102,103,104,105,106,108,110,111,115,116,117,119,122,124,125,126,127,128,129,130,131,132,],[34,-14,34,34,-54,-72,-50,34,-70,-74,-73,-71,-44,-65,-46,-66,-13,-45,-40,-75,-52,-12,-9,-13,-8,34,34,-68,34,-67,-55,-70,-64,-63,34,-59,34,-62,-56,-57,-60,-61,-58,34,-80,-16,-51,-53,-69,-47,34,-11,-15,-28,34,34,-76,34,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,34,34,34,-80,34,34,-42,-43,-39,-41,-80,-37,34,-38,]),'ENTAO':([19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,57,58,77,78,79,80,81,82,87,94,114,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-55,-70,-16,-51,-53,-69,-47,-49,-15,-76,119,]),'IGUAL':([19,23,24,25,26,28,29,31,32,35,37,40,41,57,58,77,78,79,80,81,82,87,94,102,105,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,69,-13,-75,-52,-55,-70,-16,-51,-53,-69,69,-49,-15,-76,-74,-73,]),'SUB':([15,19,21,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,76,77,78,79,80,81,82,86,87,91,92,93,94,95,96,97,98,100,102,103,104,105,106,108,110,111,115,116,117,119,122,124,125,126,127,128,129,130,131,132,],[36,-14,36,36,-54,-72,-50,36,-70,-74,-73,-71,-44,-65,-46,-66,-13,-45,-40,-75,-52,-12,-9,-13,-8,36,36,-68,36,-67,-55,-70,-64,-63,36,-59,36,-62,-56,-57,-60,-61,-58,36,-80,-16,-51,-53,-69,-47,36,-11,-15,-28,36,36,-76,36,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,36,36,36,-80,36,36,-42,-43,-39,-41,-80,-37,36,-38,]),'MENOR':([19,23,24,25,26,28,29,31,32,35,37,40,41,57,58,77,78,79,80,81,82,87,94,102,105,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,65,-13,-75,-52,-55,-70,-16,-51,-53,-69,65,-49,-15,-76,-74,-73,]),'MAIOR':([19,23,24,25,26,28,29,31,32,35,37,40,41,57,58,77,78,79,80,81,82,87,94,102,105,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,66,-13,-75,-52,-55,-70,-16,-51,-53,-69,66,-49,-15,-76,-74,-73,]),'ABRE_PAR':([12,18,37,99,101,107,],[20,20,70,115,116,118,]),'FECHA_PAR':([19,20,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,48,49,50,57,58,70,77,78,79,80,81,82,83,84,85,87,88,89,90,94,113,120,121,123,],[-14,-80,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-24,-23,76,-55,-70,-80,-16,-51,-53,-69,-47,-49,-79,94,-78,-15,-25,-26,-22,-76,-77,125,126,128,]),'ID':([0,1,4,5,6,7,8,9,10,11,13,14,15,16,17,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,76,77,78,79,80,81,82,86,87,91,92,93,94,95,96,97,98,100,102,103,104,105,106,108,110,111,112,115,116,117,118,119,122,124,125,126,127,128,129,130,131,132,],[12,-5,-20,-4,-17,-18,-3,18,-7,-6,-10,12,37,44,-19,-14,37,-2,-48,-54,-72,-50,37,-70,-74,37,-73,-71,-44,-65,-46,-66,-13,-45,-40,-75,-52,-12,-9,-13,-8,37,37,-68,37,-67,-55,-70,-64,-63,37,-59,37,-62,-56,-57,-60,-61,-58,37,44,88,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,37,37,-76,37,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,-21,37,37,37,123,-80,37,37,-42,-43,-39,-41,-80,-37,37,-38,]),'VIRGULA':([19,20,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,44,48,49,50,57,58,70,77,78,79,80,81,82,83,84,85,87,88,89,90,94,113,],[-14,-80,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,71,-13,-24,-23,75,-55,-70,-80,-16,-51,-53,-69,-47,-49,-79,93,-78,-15,-25,-26,-22,-76,-77,]),'DIFERENCA':([19,23,24,25,26,28,29,31,32,35,37,40,41,57,58,77,78,79,80,81,82,87,94,102,105,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,62,-13,-75,-52,-55,-70,-16,-51,-53,-69,62,-49,-15,-76,-74,-73,]),'FECHA_COL':([19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,51,56,57,58,72,74,77,78,79,80,81,82,87,94,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,77,80,-55,-70,87,89,-16,-51,-53,-69,-47,-49,-15,-76,]),'NOTACAO_CIENTIFICA':([15,19,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,57,58,59,60,61,62,63,64,65,66,67,68,69,70,76,77,78,79,80,81,82,86,87,91,92,93,94,95,96,97,98,100,102,103,104,105,106,108,110,111,115,116,117,119,122,124,125,126,127,128,129,130,131,132,],[40,-14,40,-48,-54,-72,-50,40,-70,-74,40,-73,-71,-44,-65,-46,-66,-13,-45,-40,-75,-52,-12,-9,-13,-8,40,40,-68,40,-67,-55,-70,-64,-63,40,-59,40,-62,-56,-57,-60,-61,-58,40,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,40,40,-76,40,-27,-30,-31,-33,-74,-32,-36,-73,-80,-34,-35,-29,40,40,40,-80,40,40,-42,-43,-39,-41,-80,-37,40,-38,]),'ATRIBUT':([3,12,19,28,37,77,87,],[15,-13,-14,15,-13,-16,-15,]),'OU_LOGICO':([19,23,24,25,26,28,29,31,32,33,35,37,40,41,57,58,77,78,79,80,81,82,87,94,102,105,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,59,-46,-13,-75,-52,-55,-70,-16,-51,-53,-69,-47,-49,-15,-76,-74,-73,]),'MULT':([19,24,25,26,28,29,31,32,37,40,41,57,58,77,78,79,80,87,94,102,105,],[-14,-54,-72,55,-70,-74,-73,-71,-13,-75,-52,-55,-70,-16,55,-53,-69,-15,-76,-74,-73,]),'FIM':([19,23,24,25,26,28,29,31,32,33,35,37,38,39,40,41,42,43,44,45,57,58,76,77,78,79,80,81,82,86,87,91,92,94,96,97,98,100,102,103,104,105,108,110,111,119,124,125,126,127,128,129,130,131,132,],[-14,-48,-54,-72,-50,-70,-74,-73,-71,-44,-46,-13,-45,-40,-75,-52,-12,-9,-13,-8,-55,-70,-80,-16,-51,-53,-69,-47,-49,-11,-15,-28,112,-76,-27,-30,-31,-33,-74,-32,-36,-73,-34,-35,-29,-80,130,-42,-43,-39,-41,-80,-37,132,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'corpo':([76,106,119,129,],[92,117,124,131,]),'operador_relacional':([35,81,],[63,63,]),'expressao_aditiva':([15,21,27,46,61,63,70,92,93,95,115,116,117,122,124,131,],[23,23,23,23,23,82,23,23,23,23,23,23,23,23,23,23,]),'acao':([92,117,124,131,],[96,96,96,96,]),'declaracao_variaveis':([0,14,92,117,124,131,],[1,1,97,97,97,97,]),'numero':([15,21,27,30,46,52,54,61,63,70,92,93,95,115,116,117,122,124,131,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'programa':([0,],[2,]),'expressao_multiplicativa':([15,21,27,46,52,61,63,70,92,93,95,115,116,117,122,124,131,],[26,26,26,26,78,26,26,26,26,26,26,26,26,26,26,26,26,]),'var':([0,14,15,16,21,27,30,46,52,54,61,63,70,71,92,93,95,115,116,117,122,124,131,],[3,3,28,42,28,28,58,28,58,58,58,58,28,42,28,28,28,28,28,28,28,28,28,]),'vazio':([20,70,76,106,119,129,],[48,83,91,91,91,91,]),'cabecalho':([0,9,14,],[4,17,4,]),'operador_soma':([15,21,23,27,46,52,54,61,63,70,82,92,93,95,115,116,117,122,124,131,],[30,30,52,30,30,30,30,30,30,30,52,30,30,30,30,30,30,30,30,30,]),'lista_parametros':([20,],[50,]),'repita':([92,117,124,131,],[103,103,103,103,]),'lista_variaveis':([16,71,],[45,86,]),'indice':([12,37,44,],[19,19,19,]),'operador_multiplicacao':([26,78,],[54,54,]),'chamada_funcao':([15,21,27,30,46,52,54,61,63,70,92,93,95,115,116,117,122,124,131,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'operador_logico':([33,],[61,]),'expressao_logica':([15,21,27,46,70,92,93,95,115,116,117,122,124,131,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'escreva':([92,117,124,131,],[108,108,108,108,]),'expressao_simples':([15,21,27,46,61,70,92,93,95,115,116,117,122,124,131,],[35,35,35,35,81,35,35,35,35,35,35,35,35,35,35,]),'leia':([92,117,124,131,],[100,100,100,100,]),'declaracao':([0,14,],[8,22,]),'tipo':([0,14,20,75,92,117,124,131,],[9,9,47,47,109,109,109,109,]),'retorna':([92,117,124,131,],[110,110,110,110,]),'se':([92,117,124,131,],[98,98,98,98,]),'declaracao_funcao':([0,14,],[10,10,]),'inicializacao_variaveis':([0,14,],[11,11,]),'lista_argumentos':([70,],[84,]),'fator':([15,21,27,30,46,52,54,61,63,70,92,93,95,115,116,117,122,124,131,],[24,24,24,57,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'atribuicao':([0,14,15,21,27,46,70,92,93,95,115,116,117,122,124,131,],[13,13,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'parametro':([20,75,],[49,90,]),'expressao':([15,21,27,46,70,92,93,95,115,116,117,122,124,131,],[39,51,56,72,85,111,113,114,120,121,111,127,111,111,]),'lista_declaracoes':([0,],[14,]),'expressao_unaria':([15,21,27,46,52,54,61,63,70,92,93,95,115,116,117,122,124,131,],[41,41,41,41,41,79,41,41,41,41,41,41,41,41,41,41,41,41,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','syntax.py',38),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','syntax.py',46),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','syntax.py',47),
  ('lista_declaracoes -> error','lista_declaracoes',1,'p_lista_declaracoes','syntax.py',48),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','syntax.py',63),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','syntax.py',64),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','syntax.py',65),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','syntax.py',78),
  ('declaracao_variaveis -> tipo DOIS_PONTOS error','declaracao_variaveis',3,'p_declaracao_variaveis_error','syntax.py',86),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','syntax.py',95),
  ('lista_variaveis -> var VIRGULA lista_variaveis','lista_variaveis',3,'p_lista_variaveis','syntax.py',102),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','syntax.py',103),
  ('var -> ID','var',1,'p_var','syntax.py',117),
  ('var -> ID indice','var',2,'p_var','syntax.py',118),
  ('indice -> indice ABRE_COL expressao FECHA_COL','indice',4,'p_indice','syntax.py',130),
  ('indice -> ABRE_COL expressao FECHA_COL','indice',3,'p_indice','syntax.py',131),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','syntax.py',156),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo','syntax.py',157),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','syntax.py',164),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','syntax.py',165),
  ('cabecalho -> ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM','cabecalho',6,'p_cabecalho','syntax.py',177),
  ('lista_parametros -> lista_parametros VIRGULA parametro','lista_parametros',3,'p_lista_parametros','syntax.py',194),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','syntax.py',195),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','syntax.py',196),
  ('parametro -> tipo DOIS_PONTOS ID','parametro',3,'p_parametro1','syntax.py',212),
  ('parametro -> parametro ABRE_COL FECHA_COL','parametro',3,'p_parametro2','syntax.py',220),
  ('corpo -> corpo acao','corpo',2,'p_corpo','syntax.py',227),
  ('corpo -> vazio','corpo',1,'p_corpo','syntax.py',228),
  ('acao -> expressao','acao',1,'p_acao','syntax.py',238),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','syntax.py',239),
  ('acao -> se','acao',1,'p_acao','syntax.py',240),
  ('acao -> repita','acao',1,'p_acao','syntax.py',241),
  ('acao -> leia','acao',1,'p_acao','syntax.py',242),
  ('acao -> escreva','acao',1,'p_acao','syntax.py',243),
  ('acao -> retorna','acao',1,'p_acao','syntax.py',244),
  ('acao -> error','acao',1,'p_acao','syntax.py',245),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','syntax.py',253),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','syntax.py',254),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','syntax.py',279),
  ('atribuicao -> var ATRIBUT expressao','atribuicao',3,'p_atribuicao','syntax.py',294),
  ('leia -> LEIA ABRE_PAR ID FECHA_PAR','leia',4,'p_leia','syntax.py',303),
  ('escreva -> ESCREVA ABRE_PAR expressao FECHA_PAR','escreva',4,'p_escreva','syntax.py',310),
  ('retorna -> RETORNA ABRE_PAR expressao FECHA_PAR','retorna',4,'p_retorna','syntax.py',317),
  ('expressao -> expressao_logica','expressao',1,'p_expressao','syntax.py',324),
  ('expressao -> atribuicao','expressao',1,'p_expressao','syntax.py',325),
  ('expressao_logica -> expressao_simples','expressao_logica',1,'p_expressao_logica','syntax.py',332),
  ('expressao_logica -> expressao_logica operador_logico expressao_simples','expressao_logica',3,'p_expressao_logica','syntax.py',333),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','syntax.py',346),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','syntax.py',347),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','syntax.py',359),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','syntax.py',360),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','syntax.py',372),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','syntax.py',373),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','syntax.py',386),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','syntax.py',387),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','syntax.py',399),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','syntax.py',400),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',401),
  ('operador_relacional -> DIFERENCA','operador_relacional',1,'p_operador_relacional','syntax.py',402),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',403),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',404),
  ('operador_relacional -> NEGACAO','operador_relacional',1,'p_operador_relacional','syntax.py',405),
  ('operador_logico -> E_LOGICO','operador_logico',1,'p_operador_logico','syntax.py',412),
  ('operador_logico -> OU_LOGICO','operador_logico',1,'p_operador_logico','syntax.py',413),
  ('operador_soma -> SOMA','operador_soma',1,'p_operador_soma','syntax.py',422),
  ('operador_soma -> SUB','operador_soma',1,'p_operador_soma','syntax.py',423),
  ('operador_multiplicacao -> MULT','operador_multiplicacao',1,'p_operador_multiplicacao','syntax.py',437),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','syntax.py',438),
  ('fator -> ABRE_COL expressao FECHA_COL','fator',3,'p_fator','syntax.py',445),
  ('fator -> var','fator',1,'p_fator','syntax.py',446),
  ('fator -> chamada_funcao','fator',1,'p_fator','syntax.py',447),
  ('fator -> numero','fator',1,'p_fator','syntax.py',448),
  ('numero -> INTEIRO','numero',1,'p_numero','syntax.py',459),
  ('numero -> FLUTUANTE','numero',1,'p_numero','syntax.py',460),
  ('numero -> NOTACAO_CIENTIFICA','numero',1,'p_numero','syntax.py',461),
  ('chamada_funcao -> ID ABRE_PAR lista_argumentos FECHA_PAR','chamada_funcao',4,'p_chamada_funcao','syntax.py',468),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','syntax.py',476),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','syntax.py',477),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','syntax.py',478),
  ('vazio -> <empty>','vazio',0,'p_vazio','syntax.py',489),
]
