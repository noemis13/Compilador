
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALNEGACAOMENOR_IGUALMAIORMAIOR_IGUALMENORE_LOGICOOU_LOGICOleftSOMASUBleftMULTDIVISAODIVISAO MULT VIRGULA ATRIBUT MENOR MAIOR IGUAL MENOR_IGUAL MAIOR_IGUAL ABRE_PAR FECHA_PAR DOIS_PONTOS SOMA SUB DIFERENCA ABRE_COL FECHA_COL NOTACAO_CIENTIFICA ID E_LOGICO OU_LOGICO NEGACAO LEIA INTEIRO ESCREVA SENAO ATE REPITA ENTAO SE RETORNA FIM FLUTUANTE\n        programa : lista_declaracoes\n                     \n        lista_declaracoes : lista_declaracoes declaracao\n                           | declaracao\n\t\t\t   | error\n        \n        declaracao : declaracao_variaveis\n                    | inicializacao_variaveis\n                    | declaracao_funcao\n        \n        declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n        \n        inicializacao_variaveis : atribuicao\n        \n        lista_variaveis : var VIRGULA lista_variaveis\n                        | var\n        \n        var : ID\n            | ID indice\n        \n        indice : indice ABRE_COL expressao FECHA_COL\n               | ABRE_COL expressao FECHA_COL\n        \n        tipo : INTEIRO\n\t     | FLUTUANTE\n        \n        declaracao_funcao : tipo cabecalho\n                        | cabecalho\n        \n        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM\n        \n        lista_parametros : lista_parametros VIRGULA lista_parametros\n                            | parametro\n                            | vazio\n        \n        parametro : tipo DOIS_PONTOS ID\n\t\t  | parametro ABRE_COL FECHA_COL\n        \n        corpo : corpo acao\n                | vazio\n        \n        acao : expressao\n                    | declaracao_variaveis\n                    | se\n                    | repita\n                    | leia\n                    | escreva\n                    | retorna\n                    | error\n\n        \n            se : SE expressao ENTAO corpo FIM\n                | SE expressao ENTAO corpo SENAO corpo FIM\n        \n            repita : REPITA corpo ATE expressao\n        \n            atribuicao : var ATRIBUT expressao\n        \n            leia : LEIA ABRE_PAR ID FECHA_PAR\n        \n            escreva : ESCREVA ABRE_PAR expressao FECHA_PAR\n        \n            retorna : RETORNA ABRE_PAR expressao FECHA_PAR\n        \n            expressao : expressao_logica\n                        | atribuicao\n        \n            expressao_logica : expressao_simples\n                             | expressao_logica operador_logico expressao_simples\n        \n            expressao_simples : expressao_aditiva\n                                | expressao_simples operador_relacional expressao_aditiva\n        \n            expressao_aditiva : expressao_multiplicativa\n                                | expressao_aditiva operador_multiplicacao expressao_unaria\n        \n           expressao_multiplicativa : expressao_unaria\n                           | expressao_multiplicativa operador_multiplicacao expressao_unaria\n\n        \n\n            expressao_unaria : fator\n                            | operador_soma fator\n\n        \n            operador_relacional : MENOR\n                                | MAIOR\n                                | IGUAL\n                                | DIFERENCA\n                                | MENOR_IGUAL\n                                | MAIOR_IGUAL\n                                | NEGACAO\n        \n            operador_logico : E_LOGICO\n                            | OU_LOGICO\n\n        \n            operador_soma : SOMA\n                          | SUB\n\n        \n            operador_multiplicacao : MULT\n                                    | DIVISAO\n        \n            fator : ABRE_COL  expressao FECHA_COL\n                    | var\n                    | chamada_funcao\n                    | numero\n        \n            numero : INTEIRO\n                    | FLUTUANTE\n                    | NOTACAO_CIENTIFICA\n        \n            chamada_funcao : ID ABRE_PAR lista_argumentos FECHA_PAR\n        \n            lista_argumentos : lista_argumentos VIRGULA expressao\n                            | expressao\n                            | vazio\n        \n            vazio :\n        '
    
_lr_action_items = {'FLUTUANTE':([0,1,3,7,8,10,12,13,14,15,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,75,77,78,79,80,81,85,87,88,91,92,93,94,95,97,98,99,100,101,102,103,104,105,106,109,110,113,115,116,119,120,123,124,125,126,127,128,129,130,131,],[2,-7,2,-6,-19,-4,-3,-9,-5,-2,-18,26,2,26,-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-64,-45,-69,26,-39,-74,-12,-70,-53,-49,26,-44,-65,26,-62,26,-63,-66,-67,26,26,-60,-56,-55,-61,-59,-57,-58,26,26,-54,-69,2,-79,-15,-10,-46,-50,-48,-68,-52,100,-27,-14,26,-75,-28,-20,-32,26,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,26,100,26,-79,26,-42,100,-38,-41,-40,-36,-79,100,-37,]),'ABRE_PAR':([9,16,38,96,108,111,],[20,20,67,113,116,117,]),'REPITA':([22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,72,75,77,78,79,80,81,85,87,88,91,93,94,97,99,100,101,102,103,104,105,106,109,110,115,119,123,124,125,126,127,128,129,130,131,],[-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,101,-27,-14,-75,-28,-32,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,101,-79,-42,101,-38,-41,-40,-36,-79,101,-37,]),'SE':([22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,72,75,77,78,79,80,81,85,87,88,91,93,94,97,99,100,101,102,103,104,105,106,109,110,115,119,123,124,125,126,127,128,129,130,131,],[-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,98,-27,-14,-75,-28,-32,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,98,-79,-42,98,-38,-41,-40,-36,-79,98,-37,]),'FECHA_COL':([22,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,49,66,69,70,73,75,76,78,79,80,81,85,91,93,],[-13,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,75,81,-54,-69,89,-15,91,-46,-50,-48,-68,-52,-14,-75,]),'MULT':([22,26,28,29,30,31,34,37,38,39,40,41,69,70,75,79,80,81,85,91,93,100,106,],[-13,-73,55,-71,-72,-51,-69,-74,-12,-70,-53,55,-54,-69,-15,-50,55,-68,-52,-14,-75,-73,-72,]),'DIFERENCA':([22,26,28,29,30,31,33,34,37,38,39,40,41,69,70,75,78,79,80,81,85,91,93,100,106,],[-13,-73,-47,-71,-72,-51,65,-69,-74,-12,-70,-53,-49,-54,-69,-15,65,-50,-48,-68,-52,-14,-75,-73,-72,]),'ATRIBUT':([6,9,22,34,38,75,91,],[19,-12,-13,19,-12,-15,-14,]),'IGUAL':([22,26,28,29,30,31,33,34,37,38,39,40,41,69,70,75,78,79,80,81,85,91,93,100,106,],[-13,-73,-47,-71,-72,-51,64,-69,-74,-12,-70,-53,-49,-54,-69,-15,64,-50,-48,-68,-52,-14,-75,-73,-72,]),'NEGACAO':([22,26,28,29,30,31,33,34,37,38,39,40,41,69,70,75,78,79,80,81,85,91,93,100,106,],[-13,-73,-47,-71,-72,-51,62,-69,-74,-12,-70,-53,-49,-54,-69,-15,62,-50,-48,-68,-52,-14,-75,-73,-72,]),'DIVISAO':([22,26,28,29,30,31,34,37,38,39,40,41,69,70,75,79,80,81,85,91,93,100,106,],[-13,-73,56,-71,-72,-51,-69,-74,-12,-70,-53,56,-54,-69,-15,-50,56,-68,-52,-14,-75,-73,-72,]),'ENTAO':([22,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,75,78,79,80,81,85,91,93,114,],[-13,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-15,-46,-50,-48,-68,-52,-14,-75,119,]),'INTEIRO':([0,1,3,7,8,10,12,13,14,15,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,72,75,77,78,79,80,81,85,87,88,91,92,93,94,95,97,98,99,100,101,102,103,104,105,106,109,110,113,115,116,119,120,123,124,125,126,127,128,129,130,131,],[4,-7,4,-6,-19,-4,-3,-9,-5,-2,-18,30,4,30,-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-64,-45,-69,30,-39,-74,-12,-70,-53,-49,30,-44,-65,30,-62,30,-63,-66,-67,30,30,-60,-56,-55,-61,-59,-57,-58,30,30,-54,-69,4,-79,-15,-10,-46,-50,-48,-68,-52,106,-27,-14,30,-75,-28,-20,-32,30,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,30,106,30,-79,30,-42,106,-38,-41,-40,-36,-79,106,-37,]),'FIM':([22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,72,75,77,78,79,80,81,85,87,88,91,93,94,97,99,100,102,103,104,105,106,109,110,119,123,124,125,126,127,128,129,130,131,],[-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,95,-27,-14,-75,-28,-32,-29,-73,-33,-31,-34,-30,-72,-26,-35,-79,-42,128,-38,-41,-40,-36,-79,131,-37,]),'MENOR_IGUAL':([22,26,28,29,30,31,33,34,37,38,39,40,41,69,70,75,78,79,80,81,85,91,93,100,106,],[-13,-73,-47,-71,-72,-51,63,-69,-74,-12,-70,-53,-49,-54,-69,-15,63,-50,-48,-68,-52,-14,-75,-73,-72,]),'DOIS_PONTOS':([2,4,5,48,100,106,107,],[-17,-16,17,74,-17,-16,17,]),'SENAO':([22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,75,77,78,79,80,81,85,88,91,93,94,97,99,100,102,103,104,105,106,109,110,119,123,124,125,126,127,128,131,],[-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-15,-10,-46,-50,-48,-68,-52,-27,-14,-75,-28,-32,-29,-73,-33,-31,-34,-30,-72,-26,-35,-79,-42,129,-38,-41,-40,-36,-37,]),'SOMA':([19,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,43,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,72,75,77,78,79,80,81,85,87,88,91,92,93,94,97,98,99,100,101,102,103,104,105,106,109,110,113,115,116,119,120,123,124,125,126,127,128,129,130,131,],[32,32,-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,32,-39,-74,-12,-70,-53,-49,-44,32,-62,32,-63,-66,-67,32,32,-60,-56,-55,-61,-59,-57,-58,32,32,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,32,-27,-14,32,-75,-28,-32,32,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,32,32,32,-79,32,-42,32,-38,-41,-40,-36,-79,32,-37,]),'RETORNA':([22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,72,75,77,78,79,80,81,85,87,88,91,93,94,97,99,100,101,102,103,104,105,106,109,110,115,119,123,124,125,126,127,128,129,130,131,],[-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,96,-27,-14,-75,-28,-32,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,96,-79,-42,96,-38,-41,-40,-36,-79,96,-37,]),'MAIOR':([22,26,28,29,30,31,33,34,37,38,39,40,41,69,70,75,78,79,80,81,85,91,93,100,106,],[-13,-73,-47,-71,-72,-51,60,-69,-74,-12,-70,-53,-49,-54,-69,-15,60,-50,-48,-68,-52,-14,-75,-73,-72,]),'OU_LOGICO':([22,26,27,28,29,30,31,33,34,37,38,39,40,41,69,70,75,78,79,80,81,85,91,93,100,106,],[-13,-73,54,-47,-71,-72,-51,-45,-69,-74,-12,-70,-53,-49,-54,-69,-15,-46,-50,-48,-68,-52,-14,-75,-73,-72,]),'E_LOGICO':([22,26,27,28,29,30,31,33,34,37,38,39,40,41,69,70,75,78,79,80,81,85,91,93,100,106,],[-13,-73,52,-47,-71,-72,-51,-45,-69,-74,-12,-70,-53,-49,-54,-69,-15,-46,-50,-48,-68,-52,-14,-75,-73,-72,]),'$end':([1,3,7,8,10,11,12,13,14,15,18,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,75,77,78,79,80,81,85,91,93,95,],[-7,-1,-6,-19,-4,0,-3,-9,-5,-2,-18,-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-15,-10,-46,-50,-48,-68,-52,-14,-75,-20,]),'ABRE_COL':([9,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,72,75,77,78,79,80,81,85,87,88,89,90,91,92,93,94,97,98,99,100,101,102,103,104,105,106,109,110,113,115,116,119,120,123,124,125,126,127,128,129,130,131,],[21,35,35,50,21,-8,-11,-73,-43,-47,-71,-72,-51,-64,-45,-69,35,-39,-74,21,-70,-53,-49,35,-44,-65,73,35,-62,35,-63,-66,-67,35,35,-60,-56,-55,-61,-59,-57,-58,35,35,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,35,-27,-25,-24,-14,35,-75,-28,-32,35,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,35,35,35,-79,35,-42,35,-38,-41,-40,-36,-79,35,-37,]),'VIRGULA':([20,22,23,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,45,46,47,67,69,70,71,75,78,79,80,81,82,83,84,85,86,89,90,91,93,112,],[-79,-13,-12,51,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,71,-22,-23,-79,-54,-69,-79,-15,-46,-50,-48,-68,-77,-78,92,-52,71,-25,-24,-14,-75,-76,]),'MENOR':([22,26,28,29,30,31,33,34,37,38,39,40,41,69,70,75,78,79,80,81,85,91,93,100,106,],[-13,-73,-47,-71,-72,-51,61,-69,-74,-12,-70,-53,-49,-54,-69,-15,61,-50,-48,-68,-52,-14,-75,-73,-72,]),'ATE':([22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,75,77,78,79,80,81,85,88,91,93,94,97,99,100,101,102,103,104,105,106,109,110,115,123,125,126,127,128,131,],[-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-15,-10,-46,-50,-48,-68,-52,-27,-14,-75,-28,-32,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,120,-42,-38,-41,-40,-36,-37,]),'ESCREVA':([22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,72,75,77,78,79,80,81,85,87,88,91,93,94,97,99,100,101,102,103,104,105,106,109,110,115,119,123,124,125,126,127,128,129,130,131,],[-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,108,-27,-14,-75,-28,-32,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,108,-79,-42,108,-38,-41,-40,-36,-79,108,-37,]),'FECHA_PAR':([20,22,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,45,46,47,67,69,70,71,75,78,79,80,81,82,83,84,85,86,89,90,91,93,112,118,121,122,],[-79,-13,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,72,-22,-23,-79,-54,-69,-79,-15,-46,-50,-48,-68,-77,-78,93,-52,-21,-25,-24,-14,-75,-76,123,126,127,]),'NOTACAO_CIENTIFICA':([19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,72,75,77,78,79,80,81,85,87,88,91,92,93,94,97,98,99,100,101,102,103,104,105,106,109,110,113,115,116,119,120,123,124,125,126,127,128,129,130,131,],[37,37,-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-64,-45,-69,37,-39,-74,-12,-70,-53,-49,37,-44,-65,37,-62,37,-63,-66,-67,37,37,-60,-56,-55,-61,-59,-57,-58,37,37,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,37,-27,-14,37,-75,-28,-32,37,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,37,37,37,-79,37,-42,37,-38,-41,-40,-36,-79,37,-37,]),'ID':([0,1,2,3,4,5,7,8,10,12,13,14,15,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,72,74,75,77,78,79,80,81,85,87,88,91,92,93,94,95,97,98,99,100,101,102,103,104,105,106,109,110,113,115,116,117,119,120,123,124,125,126,127,128,129,130,131,],[9,-7,-17,9,-16,16,-6,-19,-4,-3,-9,-5,-2,23,-18,38,38,-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-64,-45,-69,38,-39,-74,-12,-70,-53,-49,38,-44,-65,38,23,-62,38,-63,-66,-67,38,38,-60,-56,-55,-61,-59,-57,-58,38,38,-54,-69,-79,90,-15,-10,-46,-50,-48,-68,-52,38,-27,-14,38,-75,-28,-20,-32,38,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,38,38,38,122,-79,38,-42,38,-38,-41,-40,-36,-79,38,-37,]),'MAIOR_IGUAL':([22,26,28,29,30,31,33,34,37,38,39,40,41,69,70,75,78,79,80,81,85,91,93,100,106,],[-13,-73,-47,-71,-72,-51,59,-69,-74,-12,-70,-53,-49,-54,-69,-15,59,-50,-48,-68,-52,-14,-75,-73,-72,]),'error':([0,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,72,75,77,78,79,80,81,85,87,88,91,93,94,97,99,100,101,102,103,104,105,106,109,110,115,119,123,124,125,126,127,128,129,130,131,],[10,-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,110,-27,-14,-75,-28,-32,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,110,-79,-42,110,-38,-41,-40,-36,-79,110,-37,]),'LEIA':([22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,43,69,70,72,75,77,78,79,80,81,85,87,88,91,93,94,97,99,100,101,102,103,104,105,106,109,110,115,119,123,124,125,126,127,128,129,130,131,],[-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,-39,-74,-12,-70,-53,-49,-44,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,111,-27,-14,-75,-28,-32,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,111,-79,-42,111,-38,-41,-40,-36,-79,111,-37,]),'SUB':([19,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,43,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,72,75,77,78,79,80,81,85,87,88,91,92,93,94,97,98,99,100,101,102,103,104,105,106,109,110,113,115,116,119,120,123,124,125,126,127,128,129,130,131,],[44,44,-13,-12,-8,-11,-73,-43,-47,-71,-72,-51,-45,-69,44,-39,-74,-12,-70,-53,-49,-44,44,-62,44,-63,-66,-67,44,44,-60,-56,-55,-61,-59,-57,-58,44,44,-54,-69,-79,-15,-10,-46,-50,-48,-68,-52,44,-27,-14,44,-75,-28,-32,44,-29,-73,-79,-33,-31,-34,-30,-72,-26,-35,44,44,44,-79,44,-42,44,-38,-41,-40,-36,-79,44,-37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracao_funcao':([0,3,],[1,1,]),'se':([87,115,124,130,],[105,105,105,105,]),'operador_multiplicacao':([28,41,80,],[57,68,57,]),'vazio':([20,67,71,72,101,119,129,],[47,83,47,88,88,88,88,]),'expressao_logica':([19,21,35,50,67,87,92,98,113,115,116,120,124,130,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'indice':([9,23,38,],[22,22,22,]),'expressao_multiplicativa':([19,21,35,50,53,58,67,87,92,98,113,115,116,120,124,130,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'retorna':([87,115,124,130,],[104,104,104,104,]),'escreva':([87,115,124,130,],[102,102,102,102,]),'expressao_aditiva':([19,21,35,50,53,58,67,87,92,98,113,115,116,120,124,130,],[28,28,28,28,28,80,28,28,28,28,28,28,28,28,28,28,]),'lista_declaracoes':([0,],[3,]),'numero':([19,21,35,42,50,53,57,58,67,68,87,92,98,113,115,116,120,124,130,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'expressao_unaria':([19,21,35,50,53,57,58,67,68,87,92,98,113,115,116,120,124,130,],[31,31,31,31,31,79,31,31,85,31,31,31,31,31,31,31,31,31,]),'cabecalho':([0,3,5,],[8,8,18,]),'corpo':([72,101,119,129,],[87,115,124,130,]),'tipo':([0,3,20,71,87,115,124,130,],[5,5,48,48,107,107,107,107,]),'lista_argumentos':([67,],[84,]),'declaracao':([0,3,],[12,15,]),'var':([0,3,17,19,21,35,42,50,51,53,57,58,67,68,87,92,98,113,115,116,120,124,130,],[6,6,25,34,34,34,70,34,25,70,70,70,34,70,34,34,34,34,34,34,34,34,34,]),'inicializacao_variaveis':([0,3,],[7,7,]),'parametro':([20,71,],[46,46,]),'expressao':([19,21,35,50,67,87,92,98,113,115,116,120,124,130,],[36,49,66,76,82,94,112,114,118,94,121,125,94,94,]),'acao':([87,115,124,130,],[109,109,109,109,]),'expressao_simples':([19,21,35,50,53,67,87,92,98,113,115,116,120,124,130,],[33,33,33,33,78,33,33,33,33,33,33,33,33,33,33,]),'repita':([87,115,124,130,],[103,103,103,103,]),'chamada_funcao':([19,21,35,42,50,53,57,58,67,68,87,92,98,113,115,116,120,124,130,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'operador_logico':([27,],[53,]),'operador_relacional':([33,78,],[58,58,]),'fator':([19,21,35,42,50,53,57,58,67,68,87,92,98,113,115,116,120,124,130,],[40,40,40,69,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'programa':([0,],[11,]),'lista_parametros':([20,71,],[45,86,]),'operador_soma':([19,21,35,50,53,57,58,67,68,87,92,98,113,115,116,120,124,130,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'lista_variaveis':([17,51,],[24,77,]),'atribuicao':([0,3,19,21,35,50,67,87,92,98,113,115,116,120,124,130,],[13,13,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'declaracao_variaveis':([0,3,87,115,124,130,],[14,14,99,99,99,99,]),'leia':([87,115,124,130,],[97,97,97,97,]),}

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
  ('lista_parametros -> lista_parametros VIRGULA lista_parametros','lista_parametros',3,'p_lista_parametros','syntax.py',155),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','syntax.py',156),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','syntax.py',157),
  ('parametro -> tipo DOIS_PONTOS ID','parametro',3,'p_parametro','syntax.py',166),
  ('parametro -> parametro ABRE_COL FECHA_COL','parametro',3,'p_parametro','syntax.py',167),
  ('corpo -> corpo acao','corpo',2,'p_corpo','syntax.py',176),
  ('corpo -> vazio','corpo',1,'p_corpo','syntax.py',177),
  ('acao -> expressao','acao',1,'p_acao','syntax.py',186),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','syntax.py',187),
  ('acao -> se','acao',1,'p_acao','syntax.py',188),
  ('acao -> repita','acao',1,'p_acao','syntax.py',189),
  ('acao -> leia','acao',1,'p_acao','syntax.py',190),
  ('acao -> escreva','acao',1,'p_acao','syntax.py',191),
  ('acao -> retorna','acao',1,'p_acao','syntax.py',192),
  ('acao -> error','acao',1,'p_acao','syntax.py',193),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','syntax.py',200),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','syntax.py',201),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','syntax.py',221),
  ('atribuicao -> var ATRIBUT expressao','atribuicao',3,'p_atribuicao','syntax.py',234),
  ('leia -> LEIA ABRE_PAR ID FECHA_PAR','leia',4,'p_leia','syntax.py',241),
  ('escreva -> ESCREVA ABRE_PAR expressao FECHA_PAR','escreva',4,'p_escreva','syntax.py',247),
  ('retorna -> RETORNA ABRE_PAR expressao FECHA_PAR','retorna',4,'p_retorna','syntax.py',253),
  ('expressao -> expressao_logica','expressao',1,'p_expressao','syntax.py',259),
  ('expressao -> atribuicao','expressao',1,'p_expressao','syntax.py',260),
  ('expressao_logica -> expressao_simples','expressao_logica',1,'p_expressao_logica','syntax.py',267),
  ('expressao_logica -> expressao_logica operador_logico expressao_simples','expressao_logica',3,'p_expressao_logica','syntax.py',268),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','syntax.py',278),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','syntax.py',279),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','syntax.py',288),
  ('expressao_aditiva -> expressao_aditiva operador_multiplicacao expressao_unaria','expressao_aditiva',3,'p_expressao_aditiva','syntax.py',289),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','syntax.py',298),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','syntax.py',299),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','syntax.py',310),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','syntax.py',311),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','syntax.py',321),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','syntax.py',322),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',323),
  ('operador_relacional -> DIFERENCA','operador_relacional',1,'p_operador_relacional','syntax.py',324),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',325),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',326),
  ('operador_relacional -> NEGACAO','operador_relacional',1,'p_operador_relacional','syntax.py',327),
  ('operador_logico -> E_LOGICO','operador_logico',1,'p_operador_logico','syntax.py',333),
  ('operador_logico -> OU_LOGICO','operador_logico',1,'p_operador_logico','syntax.py',334),
  ('operador_soma -> SOMA','operador_soma',1,'p_operador_soma','syntax.py',342),
  ('operador_soma -> SUB','operador_soma',1,'p_operador_soma','syntax.py',343),
  ('operador_multiplicacao -> MULT','operador_multiplicacao',1,'p_operador_multiplicacao','syntax.py',357),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','syntax.py',358),
  ('fator -> ABRE_COL expressao FECHA_COL','fator',3,'p_fator','syntax.py',364),
  ('fator -> var','fator',1,'p_fator','syntax.py',365),
  ('fator -> chamada_funcao','fator',1,'p_fator','syntax.py',366),
  ('fator -> numero','fator',1,'p_fator','syntax.py',367),
  ('numero -> INTEIRO','numero',1,'p_numero','syntax.py',376),
  ('numero -> FLUTUANTE','numero',1,'p_numero','syntax.py',377),
  ('numero -> NOTACAO_CIENTIFICA','numero',1,'p_numero','syntax.py',378),
  ('chamada_funcao -> ID ABRE_PAR lista_argumentos FECHA_PAR','chamada_funcao',4,'p_chamada_funcao','syntax.py',384),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','syntax.py',390),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','syntax.py',391),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','syntax.py',392),
  ('vazio -> <empty>','vazio',0,'p_vazio','syntax.py',401),
]
