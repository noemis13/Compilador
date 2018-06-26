
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALNEGACAOMENOR_IGUALMAIORMAIOR_IGUALMENORE_LOGICOOU_LOGICOleftSOMASUBleftMULTDIVISAODIVISAO MULT VIRGULA ATRIBUT MENOR MAIOR IGUAL MENOR_IGUAL MAIOR_IGUAL ABRE_PAR FECHA_PAR DOIS_PONTOS SOMA SUB DIFERENCA ABRE_COL FECHA_COL NOTACAO_CIENTIFICA ID E_LOGICO OU_LOGICO NEGACAO SENAO RETORNA SE FIM ESCREVA ATE REPITA ENTAO INTEIRO LEIA FLUTUANTE\n        programa : lista_declaracoes\n                     \n        lista_declaracoes : lista_declaracoes declaracao\n                          | declaracao\n                         | error\n        \n        declaracao : declaracao_variaveis\n                   | inicializacao_variaveis\n                   | declaracao_funcao\n        \n        declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n        \n        declaracao_variaveis : tipo DOIS_PONTOS error\n        \n        inicializacao_variaveis : atribuicao\n        \n        lista_variaveis : var VIRGULA lista_variaveis\n                        | var\n        \n        var : ID\n            | ID indice\n        \n        indice : indice ABRE_COL expressao FECHA_COL\n               | ABRE_COL expressao FECHA_COL\n        \n        tipo : INTEIRO\n\t     | FLUTUANTE\n        \n        declaracao_funcao : tipo cabecalho\n                          | cabecalho\n        \n        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM\n        \n        lista_parametros : lista_parametros VIRGULA parametro\n                         | parametro\n                         | vazio\n        \n        parametro : tipo DOIS_PONTOS ID\n        \n        parametro : parametro ABRE_COL FECHA_COL\n        \n        corpo : corpo acao\n              | vazio\n        \n        acao : expressao\n                    | declaracao_variaveis\n                    | se\n                    | repita\n                    | leia\n                    | escreva\n                    | retorna\n                    | error\n\n        \n            se : SE expressao ENTAO corpo FIM\n                | SE expressao ENTAO corpo SENAO corpo FIM\n        \n            repita : REPITA corpo ATE expressao\n        \n            atribuicao : var ATRIBUT expressao\n        \n            leia : LEIA ABRE_PAR ID FECHA_PAR\n        \n            escreva : ESCREVA ABRE_PAR expressao FECHA_PAR\n        \n            retorna : RETORNA ABRE_PAR expressao FECHA_PAR\n        \n            expressao : expressao_logica\n                        | atribuicao\n        \n            expressao_logica : expressao_simples\n                             | expressao_logica operador_logico expressao_simples\n        \n            expressao_simples : expressao_aditiva\n                              | expressao_simples operador_relacional expressao_aditiva\n        \n            expressao_aditiva : expressao_multiplicativa\n                                | expressao_aditiva operador_soma expressao_multiplicativa\n        \n           expressao_multiplicativa : expressao_unaria\n                           | expressao_multiplicativa operador_multiplicacao expressao_unaria\n\n        \n            expressao_unaria : fator\n                            | operador_soma fator\n        \n            operador_relacional : MENOR\n                                | MAIOR\n                                | IGUAL\n                                | DIFERENCA\n                                | MENOR_IGUAL\n                                | MAIOR_IGUAL\n                                | NEGACAO\n        \n            operador_logico : E_LOGICO\n                            | OU_LOGICO\n\n        \n            operador_soma : SOMA\n                          | SUB\n\n        \n            operador_multiplicacao : MULT\n                                   | DIVISAO\n        \n            fator : ABRE_COL expressao FECHA_COL\n                  | var\n                  | chamada_funcao\n                  | numero\n        \n            numero : INTEIRO\n                   | FLUTUANTE\n                   | NOTACAO_CIENTIFICA\n        \n            chamada_funcao : ID ABRE_PAR lista_argumentos FECHA_PAR\n        \n            lista_argumentos : lista_argumentos VIRGULA expressao\n                            | expressao\n                            | vazio\n        \n            vazio :\n        '
    
_lr_action_items = {'SUB':([15,20,21,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,78,79,80,81,82,86,87,90,91,93,94,95,96,97,98,100,101,102,103,105,107,108,109,110,115,117,118,119,122,124,125,126,127,128,129,130,131,132,],[24,-14,24,-50,-66,-46,-70,-44,24,-40,-72,-73,-54,-52,24,-45,-75,-71,-13,-65,-74,-8,-9,-12,-13,24,-67,24,-68,-57,-62,-58,-56,24,-61,-60,-59,-70,-55,24,-64,-63,24,24,-16,-80,-53,24,-47,-51,-69,-11,-15,-28,24,-76,24,-33,-30,-36,-29,-73,-35,-32,24,-74,-31,-34,-27,-80,24,24,24,-80,24,24,-43,-41,-39,-42,-80,-37,24,-38,]),'MULT':([20,23,27,31,32,33,34,37,38,39,41,63,64,73,78,81,82,87,93,100,105,],[-14,52,-70,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,52,-69,-15,-76,-73,-74,]),'ATE':([20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,42,43,44,45,63,64,73,78,79,80,81,82,86,87,90,93,95,96,97,98,100,101,102,105,107,108,109,110,117,125,126,127,128,130,132,],[-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-8,-9,-12,-13,-70,-55,-16,-53,-49,-47,-51,-69,-11,-15,-28,-76,-33,-30,-36,-29,-73,-35,-32,-74,-31,-34,-27,-80,122,-43,-41,-39,-42,-37,-38,]),'$end':([1,3,4,5,6,7,9,10,11,16,19,20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,42,43,44,45,63,64,73,78,79,80,81,82,86,87,93,99,],[-7,-20,-4,-1,-5,-6,-10,0,-3,-2,-19,-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-8,-9,-12,-13,-70,-55,-16,-53,-49,-47,-51,-69,-11,-15,-76,-21,]),'ESCREVA':([20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,42,43,44,45,63,64,73,76,78,79,80,81,82,86,87,90,91,93,95,96,97,98,100,101,102,105,107,108,109,110,117,119,124,125,126,127,128,129,130,131,132,],[-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-8,-9,-12,-13,-70,-55,-16,-80,-53,-49,-47,-51,-69,-11,-15,-28,111,-76,-33,-30,-36,-29,-73,-35,-32,-74,-31,-34,-27,-80,111,-80,111,-43,-41,-39,-42,-80,-37,111,-38,]),'LEIA':([20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,42,43,44,45,63,64,73,76,78,79,80,81,82,86,87,90,91,93,95,96,97,98,100,101,102,105,107,108,109,110,117,119,124,125,126,127,128,129,130,131,132,],[-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-8,-9,-12,-13,-70,-55,-16,-80,-53,-49,-47,-51,-69,-11,-15,-28,106,-76,-33,-30,-36,-29,-73,-35,-32,-74,-31,-34,-27,-80,106,-80,106,-43,-41,-39,-42,-80,-37,106,-38,]),'MENOR_IGUAL':([20,23,25,27,29,31,32,33,34,37,38,39,41,63,64,73,78,79,80,81,82,87,93,100,105,],[-14,-50,61,-70,-48,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,-49,61,-51,-69,-15,-76,-73,-74,]),'MAIOR_IGUAL':([20,23,25,27,29,31,32,33,34,37,38,39,41,63,64,73,78,79,80,81,82,87,93,100,105,],[-14,-50,60,-70,-48,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,-49,60,-51,-69,-15,-76,-73,-74,]),'DIVISAO':([20,23,27,31,32,33,34,37,38,39,41,63,64,73,78,81,82,87,93,100,105,],[-14,54,-70,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,54,-69,-15,-76,-73,-74,]),'MAIOR':([20,23,25,27,29,31,32,33,34,37,38,39,41,63,64,73,78,79,80,81,82,87,93,100,105,],[-14,-50,55,-70,-48,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,-49,55,-51,-69,-15,-76,-73,-74,]),'DOIS_PONTOS':([8,12,13,49,100,105,112,],[-17,-18,17,74,-17,-18,17,]),'error':([0,17,20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,42,43,44,45,63,64,73,76,78,79,80,81,82,86,87,90,91,93,95,96,97,98,100,101,102,105,107,108,109,110,117,119,124,125,126,127,128,129,130,131,132,],[4,43,-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-8,-9,-12,-13,-70,-55,-16,-80,-53,-49,-47,-51,-69,-11,-15,-28,97,-76,-33,-30,-36,-29,-73,-35,-32,-74,-31,-34,-27,-80,97,-80,97,-43,-41,-39,-42,-80,-37,97,-38,]),'ATRIBUT':([2,14,20,27,39,73,87,],[15,-13,-14,15,-13,-16,-15,]),'NOTACAO_CIENTIFICA':([15,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,78,79,80,81,82,86,87,90,91,93,94,95,96,97,98,100,101,102,103,105,107,108,109,110,115,117,118,119,122,124,125,126,127,128,129,130,131,132,],[37,-14,37,-50,-66,-46,37,-70,-44,-48,-40,-72,-73,-54,-52,37,-45,-75,-71,-13,-65,-74,-8,-9,-12,-13,37,-67,37,-68,-57,-62,-58,-56,37,-61,-60,-59,-70,-55,37,-64,-63,37,37,-16,-80,-53,-49,-47,-51,-69,-11,-15,-28,37,-76,37,-33,-30,-36,-29,-73,-35,-32,37,-74,-31,-34,-27,-80,37,37,37,-80,37,37,-43,-41,-39,-42,-80,-37,37,-38,]),'OU_LOGICO':([20,23,25,27,28,29,31,32,33,34,37,38,39,41,63,64,73,78,79,80,81,82,87,93,100,105,],[-14,-50,-46,-70,66,-48,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,-49,-47,-51,-69,-15,-76,-73,-74,]),'INTEIRO':([0,1,3,4,5,6,7,9,11,15,16,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,80,81,82,86,87,90,91,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,115,117,118,119,122,124,125,126,127,128,129,130,131,132,],[8,-7,-20,-4,8,-5,-6,-10,-3,32,-2,-19,-14,32,8,-50,-66,-46,32,-70,-44,-48,-40,-72,-73,-54,-52,32,-45,-75,-71,-13,-65,-74,-8,-9,-12,-13,32,-67,32,-68,-57,-62,-58,-56,32,-61,-60,-59,-70,-55,32,-64,-63,32,32,-16,-80,8,-53,-49,-47,-51,-69,-11,-15,-28,100,-76,32,-33,-30,-36,-29,-21,-73,-35,-32,32,-74,-31,-34,-27,-80,32,100,32,-80,32,100,-43,-41,-39,-42,-80,-37,100,-38,]),'ABRE_PAR':([14,18,39,104,106,111,],[22,22,70,115,116,118,]),'NEGACAO':([20,23,25,27,29,31,32,33,34,37,38,39,41,63,64,73,78,79,80,81,82,87,93,100,105,],[-14,-50,56,-70,-48,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,-49,56,-51,-69,-15,-76,-73,-74,]),'ENTAO':([20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,63,64,73,78,79,80,81,82,87,93,114,],[-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-70,-55,-16,-53,-49,-47,-51,-69,-15,-76,119,]),'E_LOGICO':([20,23,25,27,28,29,31,32,33,34,37,38,39,41,63,64,73,78,79,80,81,82,87,93,100,105,],[-14,-50,-46,-70,67,-48,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,-49,-47,-51,-69,-15,-76,-73,-74,]),'IGUAL':([20,23,25,27,29,31,32,33,34,37,38,39,41,63,64,73,78,79,80,81,82,87,93,100,105,],[-14,-50,57,-70,-48,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,-49,57,-51,-69,-15,-76,-73,-74,]),'ABRE_COL':([14,15,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,78,79,80,81,82,86,87,88,89,90,91,92,93,94,95,96,97,98,100,101,102,103,105,107,108,109,110,115,117,118,119,122,124,125,126,127,128,129,130,131,132,],[21,35,46,35,-50,-66,-46,35,-70,-44,-48,-40,-72,-73,-54,-52,35,-45,-75,-71,21,-65,-74,-8,-9,-12,21,35,75,-67,35,-68,-57,-62,-58,-56,35,-61,-60,-59,-70,-55,35,-64,-63,35,35,-16,-80,-53,-49,-47,-51,-69,-11,-15,-25,-26,-28,35,75,-76,35,-33,-30,-36,-29,-73,-35,-32,35,-74,-31,-34,-27,-80,35,35,35,-80,35,35,-43,-41,-39,-42,-80,-37,35,-38,]),'SENAO':([20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,42,43,44,45,63,64,73,78,79,80,81,82,86,87,90,93,95,96,97,98,100,101,102,105,107,108,109,119,124,125,126,127,128,130,132,],[-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-8,-9,-12,-13,-70,-55,-16,-53,-49,-47,-51,-69,-11,-15,-28,-76,-33,-30,-36,-29,-73,-35,-32,-74,-31,-34,-27,-80,129,-43,-41,-39,-42,-37,-38,]),'MENOR':([20,23,25,27,29,31,32,33,34,37,38,39,41,63,64,73,78,79,80,81,82,87,93,100,105,],[-14,-50,58,-70,-48,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,-49,58,-51,-69,-15,-76,-73,-74,]),'FECHA_PAR':([20,22,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,48,50,51,63,64,70,73,78,79,80,81,82,83,84,85,87,88,89,92,93,113,120,121,123,],[-14,-80,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-24,-23,76,-70,-55,-80,-16,-53,-49,-47,-51,-69,93,-79,-78,-15,-25,-26,-22,-76,-77,125,126,128,]),'REPITA':([20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,42,43,44,45,63,64,73,76,78,79,80,81,82,86,87,90,91,93,95,96,97,98,100,101,102,105,107,108,109,110,117,119,124,125,126,127,128,129,130,131,132,],[-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-8,-9,-12,-13,-70,-55,-16,-80,-53,-49,-47,-51,-69,-11,-15,-28,110,-76,-33,-30,-36,-29,-73,-35,-32,-74,-31,-34,-27,-80,110,-80,110,-43,-41,-39,-42,-80,-37,110,-38,]),'FIM':([20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,42,43,44,45,63,64,73,76,78,79,80,81,82,86,87,90,91,93,95,96,97,98,100,101,102,105,107,108,109,119,124,125,126,127,128,129,130,131,132,],[-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-8,-9,-12,-13,-70,-55,-16,-80,-53,-49,-47,-51,-69,-11,-15,-28,99,-76,-33,-30,-36,-29,-73,-35,-32,-74,-31,-34,-27,-80,130,-43,-41,-39,-42,-80,-37,132,-38,]),'ID':([0,1,3,4,5,6,7,8,9,11,12,13,15,16,17,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,71,73,74,76,78,79,80,81,82,86,87,90,91,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,115,116,117,118,119,122,124,125,126,127,128,129,130,131,132,],[14,-7,-20,-4,14,-5,-6,-17,-10,-3,-18,18,39,-2,45,-19,-14,39,-50,-66,-46,39,-70,-44,-48,-40,-72,-73,-54,-52,39,-45,-75,-71,-13,-65,-74,-8,-9,-12,-13,39,-67,39,-68,-57,-62,-58,-56,39,-61,-60,-59,-70,-55,39,-64,-63,39,39,45,-16,88,-80,-53,-49,-47,-51,-69,-11,-15,-28,39,-76,39,-33,-30,-36,-29,-21,-73,-35,-32,39,-74,-31,-34,-27,-80,39,121,39,39,-80,39,39,-43,-41,-39,-42,-80,-37,39,-38,]),'FECHA_COL':([20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,47,63,64,69,72,73,75,78,79,80,81,82,87,93,],[-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,73,-70,-55,82,87,-16,89,-53,-49,-47,-51,-69,-15,-76,]),'SE':([20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,42,43,44,45,63,64,73,76,78,79,80,81,82,86,87,90,91,93,95,96,97,98,100,101,102,105,107,108,109,110,117,119,124,125,126,127,128,129,130,131,132,],[-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-8,-9,-12,-13,-70,-55,-16,-80,-53,-49,-47,-51,-69,-11,-15,-28,103,-76,-33,-30,-36,-29,-73,-35,-32,-74,-31,-34,-27,-80,103,-80,103,-43,-41,-39,-42,-80,-37,103,-38,]),'SOMA':([15,20,21,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,78,79,80,81,82,86,87,90,91,93,94,95,96,97,98,100,101,102,103,105,107,108,109,110,115,117,118,119,122,124,125,126,127,128,129,130,131,132,],[40,-14,40,-50,-66,-46,-70,-44,40,-40,-72,-73,-54,-52,40,-45,-75,-71,-13,-65,-74,-8,-9,-12,-13,40,-67,40,-68,-57,-62,-58,-56,40,-61,-60,-59,-70,-55,40,-64,-63,40,40,-16,-80,-53,40,-47,-51,-69,-11,-15,-28,40,-76,40,-33,-30,-36,-29,-73,-35,-32,40,-74,-31,-34,-27,-80,40,40,40,-80,40,40,-43,-41,-39,-42,-80,-37,40,-38,]),'DIFERENCA':([20,23,25,27,29,31,32,33,34,37,38,39,41,63,64,73,78,79,80,81,82,87,93,100,105,],[-14,-50,62,-70,-48,-72,-73,-54,-52,-75,-71,-13,-74,-70,-55,-16,-53,-49,62,-51,-69,-15,-76,-73,-74,]),'RETORNA':([20,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,42,43,44,45,63,64,73,76,78,79,80,81,82,86,87,90,91,93,95,96,97,98,100,101,102,105,107,108,109,110,117,119,124,125,126,127,128,129,130,131,132,],[-14,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,-8,-9,-12,-13,-70,-55,-16,-80,-53,-49,-47,-51,-69,-11,-15,-28,104,-76,-33,-30,-36,-29,-73,-35,-32,-74,-31,-34,-27,-80,104,-80,104,-43,-41,-39,-42,-80,-37,104,-38,]),'VIRGULA':([20,22,23,25,27,28,29,30,31,32,33,34,36,37,38,39,41,44,45,48,50,51,63,64,70,73,78,79,80,81,82,83,84,85,87,88,89,92,93,113,],[-14,-80,-50,-46,-70,-44,-48,-40,-72,-73,-54,-52,-45,-75,-71,-13,-74,71,-13,-24,-23,77,-70,-55,-80,-16,-53,-49,-47,-51,-69,94,-79,-78,-15,-25,-26,-22,-76,-77,]),'FLUTUANTE':([0,1,3,4,5,6,7,9,11,15,16,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,80,81,82,86,87,90,91,93,94,95,96,97,98,99,100,101,102,103,105,107,108,109,110,115,117,118,119,122,124,125,126,127,128,129,130,131,132,],[12,-7,-20,-4,12,-5,-6,-10,-3,41,-2,-19,-14,41,12,-50,-66,-46,41,-70,-44,-48,-40,-72,-73,-54,-52,41,-45,-75,-71,-13,-65,-74,-8,-9,-12,-13,41,-67,41,-68,-57,-62,-58,-56,41,-61,-60,-59,-70,-55,41,-64,-63,41,41,-16,-80,12,-53,-49,-47,-51,-69,-11,-15,-28,105,-76,41,-33,-30,-36,-29,-21,-73,-35,-32,41,-74,-31,-34,-27,-80,41,105,41,-80,41,105,-43,-41,-39,-42,-80,-37,105,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressao_multiplicativa':([15,21,35,46,59,65,68,70,91,94,103,115,117,118,122,124,131,],[23,23,23,23,23,23,81,23,23,23,23,23,23,23,23,23,23,]),'lista_argumentos':([70,],[83,]),'expressao_simples':([15,21,35,46,65,70,91,94,103,115,117,118,122,124,131,],[25,25,25,25,80,25,25,25,25,25,25,25,25,25,25,]),'operador_soma':([15,21,29,35,46,53,59,65,68,70,79,91,94,103,115,117,118,122,124,131,],[26,26,68,26,26,26,26,26,26,26,68,26,26,26,26,26,26,26,26,26,]),'vazio':([22,70,76,110,119,129,],[48,84,90,90,90,90,]),'escreva':([91,117,124,131,],[108,108,108,108,]),'operador_logico':([28,],[65,]),'se':([91,117,124,131,],[107,107,107,107,]),'leia':([91,117,124,131,],[95,95,95,95,]),'var':([0,5,15,17,21,26,35,46,53,59,65,68,70,71,91,94,103,115,117,118,122,124,131,],[2,2,27,44,27,63,27,27,63,63,63,63,27,44,27,27,27,27,27,27,27,27,27,]),'parametro':([22,77,],[50,92,]),'expressao_logica':([15,21,35,46,70,91,94,103,115,117,118,122,124,131,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'declaracao_variaveis':([0,5,91,117,124,131,],[6,6,96,96,96,96,]),'expressao_aditiva':([15,21,35,46,59,65,70,91,94,103,115,117,118,122,124,131,],[29,29,29,29,79,29,29,29,29,29,29,29,29,29,29,29,]),'cabecalho':([0,5,13,],[3,3,19,]),'lista_declaracoes':([0,],[5,]),'expressao':([15,21,35,46,70,91,94,103,115,117,118,122,124,131,],[30,47,69,72,85,98,113,114,120,98,123,127,98,98,]),'indice':([14,39,45,],[20,20,20,]),'inicializacao_variaveis':([0,5,],[7,7,]),'numero':([15,21,26,35,46,53,59,65,68,70,91,94,103,115,117,118,122,124,131,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'fator':([15,21,26,35,46,53,59,65,68,70,91,94,103,115,117,118,122,124,131,],[33,33,64,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'declaracao':([0,5,],[11,16,]),'corpo':([76,110,119,129,],[91,117,124,131,]),'expressao_unaria':([15,21,35,46,53,59,65,68,70,91,94,103,115,117,118,122,124,131,],[34,34,34,34,78,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'acao':([91,117,124,131,],[109,109,109,109,]),'operador_relacional':([25,80,],[59,59,]),'tipo':([0,5,22,77,91,117,124,131,],[13,13,49,49,112,112,112,112,]),'repita':([91,117,124,131,],[102,102,102,102,]),'programa':([0,],[10,]),'chamada_funcao':([15,21,26,35,46,53,59,65,68,70,91,94,103,115,117,118,122,124,131,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'lista_variaveis':([17,71,],[42,86,]),'lista_parametros':([22,],[51,]),'operador_multiplicacao':([23,81,],[53,53,]),'atribuicao':([0,5,15,21,35,46,70,91,94,103,115,117,118,122,124,131,],[9,9,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'retorna':([91,117,124,131,],[101,101,101,101,]),'declaracao_funcao':([0,5,],[1,1,]),}

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
