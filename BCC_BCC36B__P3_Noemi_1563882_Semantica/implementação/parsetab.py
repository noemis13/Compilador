
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftIGUALNEGACAOMENOR_IGUALMAIORMAIOR_IGUALMENORE_LOGICOOU_LOGICOleftSOMASUBleftMULTDIVISAODIVISAO MULT VIRGULA ATRIBUT MENOR MAIOR IGUAL MENOR_IGUAL MAIOR_IGUAL ABRE_PAR FECHA_PAR DOIS_PONTOS SOMA SUB DIFERENCA ABRE_COL FECHA_COL NOTACAO_CIENTIFICA ID E_LOGICO OU_LOGICO NEGACAO LEIA ESCREVA SENAO FLUTUANTE ATE ENTAO INTEIRO FIM RETORNA REPITA SE\n        programa : lista_declaracoes\n                     \n        lista_declaracoes : lista_declaracoes declaracao\n                          | declaracao\n                         | error\n        \n        declaracao : declaracao_variaveis\n                   | inicializacao_variaveis\n                   | declaracao_funcao\n        \n        declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n        \n        declaracao_variaveis : tipo DOIS_PONTOS error\n        \n        inicializacao_variaveis : atribuicao\n        \n        lista_variaveis : var VIRGULA lista_variaveis\n                        | var\n        \n        var : ID\n            | ID indice\n        \n        indice : indice ABRE_COL expressao FECHA_COL\n               | ABRE_COL expressao FECHA_COL\n        \n        tipo : INTEIRO\n\t     | FLUTUANTE\n        \n        declaracao_funcao : tipo cabecalho\n                          | cabecalho\n        \n        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM\n        \n        lista_parametros : lista_parametros VIRGULA parametro\n                         | parametro\n                         | vazio\n        \n        parametro : tipo DOIS_PONTOS ID\n        \n        parametro : parametro ABRE_COL FECHA_COL\n        \n        corpo : corpo acao\n              | vazio\n        \n        acao : expressao\n                    | declaracao_variaveis\n                    | se\n                    | repita\n                    | leia\n                    | escreva\n                    | retorna\n                    | error\n\n        \n            se : SE expressao ENTAO corpo FIM\n                | SE expressao ENTAO corpo SENAO corpo FIM\n        \n            repita : REPITA corpo ate\n         \n            ate : ATE expressao\n        \n            atribuicao : var ATRIBUT expressao\n        \n            leia : LEIA ABRE_PAR ID FECHA_PAR\n        \n            escreva : ESCREVA ABRE_PAR expressao FECHA_PAR\n        \n            retorna : RETORNA ABRE_PAR expressao FECHA_PAR\n        \n            expressao : expressao_logica\n                        | atribuicao\n        \n            expressao_logica : expressao_simples\n                             | expressao_logica operador_logico expressao_simples\n        \n            expressao_simples : expressao_aditiva\n                              | expressao_simples operador_relacional expressao_aditiva\n        \n            expressao_aditiva : expressao_multiplicativa\n                                | expressao_aditiva operador_soma expressao_multiplicativa\n        \n           expressao_multiplicativa : expressao_unaria\n                           | expressao_multiplicativa operador_multiplicacao expressao_unaria\n\n        \n            expressao_unaria : fator\n                            | operador_soma fator\n        \n            operador_relacional : MENOR\n                                | MAIOR\n                                | IGUAL\n                                | DIFERENCA\n                                | MENOR_IGUAL\n                                | MAIOR_IGUAL\n                                | NEGACAO\n        \n            operador_logico : E_LOGICO\n                            | OU_LOGICO\n\n        \n            operador_soma : SOMA\n                          | SUB\n\n        \n            operador_multiplicacao : MULT\n                                   | DIVISAO\n        \n            fator : ABRE_COL expressao FECHA_COL\n                  | var\n                  | chamada_funcao\n                  | numero\n        \n            numero : INTEIRO\n                   | FLUTUANTE\n                   | NOTACAO_CIENTIFICA\n        \n            chamada_funcao : ID ABRE_PAR lista_argumentos FECHA_PAR\n        \n            lista_argumentos : lista_argumentos VIRGULA expressao\n                            | expressao\n                            | vazio\n        \n            vazio :\n        '
    
_lr_action_items = {'MAIOR_IGUAL':([17,23,24,25,26,28,29,32,33,34,36,37,41,66,67,76,78,82,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,53,-76,-53,-55,-13,-74,-49,-51,-71,-56,-16,-50,53,-52,-70,-54,-15,-77,-74,-75,]),'RETORNA':([17,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,48,49,50,51,66,67,73,76,78,82,83,84,85,86,88,89,92,94,97,98,100,101,103,105,106,107,108,109,110,112,118,121,124,125,126,127,128,129,130,131,132,133,],[-14,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-9,-8,-12,-13,-71,-56,-81,-16,-50,-48,-52,-70,-54,-15,-28,95,-11,-77,-30,-29,-35,-34,-74,-36,-75,-81,-27,-31,-33,-32,95,-81,-39,-44,-42,95,-43,-40,-37,-81,95,-38,]),'MULT':([17,23,24,25,26,29,32,33,34,36,41,66,67,76,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,-76,-53,-55,-13,-74,70,-71,-56,-16,70,-70,-54,-15,-77,-74,-75,]),'MENOR':([17,23,24,25,26,28,29,32,33,34,36,37,41,66,67,76,78,82,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,55,-76,-53,-55,-13,-74,-49,-51,-71,-56,-16,-50,55,-52,-70,-54,-15,-77,-74,-75,]),'DOIS_PONTOS':([5,12,13,46,103,106,111,],[-18,-17,20,75,-17,-18,20,]),'NEGACAO':([17,23,24,25,26,28,29,32,33,34,36,37,41,66,67,76,78,82,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,56,-76,-53,-55,-13,-74,-49,-51,-71,-56,-16,-50,56,-52,-70,-54,-15,-77,-74,-75,]),'FLUTUANTE':([0,1,2,4,6,7,10,11,14,15,16,17,18,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,72,73,76,78,82,83,84,85,86,88,89,92,93,94,97,98,99,100,101,102,103,105,106,107,108,109,110,112,114,117,118,121,123,124,125,126,127,128,129,130,131,132,133,],[5,-4,-5,-3,-10,5,-20,-6,-7,25,-2,-14,5,25,-19,-71,-72,-75,-73,-41,-47,-76,-67,-46,-53,-55,-13,-45,-74,-49,25,25,-66,-51,25,-9,-8,-12,-13,-59,-62,-61,-57,-63,25,-60,-58,25,-64,25,-65,25,-71,-56,-69,25,-68,5,-81,-16,-50,-48,-52,-70,-54,-15,-28,106,-11,25,-77,-30,-29,-21,-35,-34,25,-74,-36,-75,-81,-27,-31,-33,-32,25,25,106,-81,25,-39,-44,-42,106,-43,-40,-37,-81,106,-38,]),'DIFERENCA':([17,23,24,25,26,28,29,32,33,34,36,37,41,66,67,76,78,82,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,58,-76,-53,-55,-13,-74,-49,-51,-71,-56,-16,-50,58,-52,-70,-54,-15,-77,-74,-75,]),'FIM':([17,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,48,49,50,51,66,67,73,76,78,82,83,84,85,86,88,89,92,94,97,98,100,101,103,105,106,108,109,110,112,121,124,125,126,127,128,129,130,131,132,133,],[-14,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-9,-8,-12,-13,-71,-56,-81,-16,-50,-48,-52,-70,-54,-15,-28,99,-11,-77,-30,-29,-35,-34,-74,-36,-75,-27,-31,-33,-32,-81,-39,-44,-42,130,-43,-40,-37,-81,133,-38,]),'ENTAO':([17,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,66,67,76,78,82,83,84,85,86,94,116,],[-14,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-71,-56,-16,-50,-48,-52,-70,-54,-15,-77,121,]),'OU_LOGICO':([17,23,24,25,26,28,29,32,33,34,35,36,37,41,66,67,76,78,82,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,-47,-76,-53,-55,-13,63,-74,-49,-51,-71,-56,-16,-50,-48,-52,-70,-54,-15,-77,-74,-75,]),'NOTACAO_CIENTIFICA':([15,17,19,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,73,76,78,82,83,84,85,86,88,89,92,93,94,97,98,100,101,102,103,105,106,107,108,109,110,112,114,117,118,121,123,124,125,126,127,128,129,130,131,132,133,],[29,-14,29,-71,-72,-75,-73,-41,-47,-76,-67,-46,-53,-55,-13,-45,-74,-49,29,29,-66,-51,29,-9,-8,-12,-13,-59,-62,-61,-57,-63,29,-60,-58,29,-64,29,-65,29,-71,-56,-69,29,-68,-81,-16,-50,-48,-52,-70,-54,-15,-28,29,-11,29,-77,-30,-29,-35,-34,29,-74,-36,-75,-81,-27,-31,-33,-32,29,29,29,-81,29,-39,-44,-42,29,-43,-40,-37,-81,29,-38,]),'REPITA':([17,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,48,49,50,51,66,67,73,76,78,82,83,84,85,86,88,89,92,94,97,98,100,101,103,105,106,107,108,109,110,112,118,121,124,125,126,127,128,129,130,131,132,133,],[-14,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-9,-8,-12,-13,-71,-56,-81,-16,-50,-48,-52,-70,-54,-15,-28,107,-11,-77,-30,-29,-35,-34,-74,-36,-75,-81,-27,-31,-33,-32,107,-81,-39,-44,-42,107,-43,-40,-37,-81,107,-38,]),'SUB':([15,17,19,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,73,76,78,82,83,84,85,86,88,89,92,93,94,97,98,100,101,102,103,105,106,107,108,109,110,112,114,117,118,121,123,124,125,126,127,128,129,130,131,132,133,],[30,-14,30,-71,-72,-75,-73,-41,-47,-76,-67,-46,-53,-55,-13,-45,-74,30,30,-66,-51,30,-9,-8,-12,-13,-59,-62,-61,-57,-63,30,-60,-58,30,-64,30,-65,30,-71,-56,-69,30,-68,-81,-16,30,-48,-52,-70,-54,-15,-28,30,-11,30,-77,-30,-29,-35,-34,30,-74,-36,-75,-81,-27,-31,-33,-32,30,30,30,-81,30,-39,-44,-42,30,-43,-40,-37,-81,30,-38,]),'FECHA_COL':([17,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,47,65,66,67,71,74,76,78,82,83,84,85,86,94,],[-14,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,76,84,-71,-56,86,90,-16,-50,-48,-52,-70,-54,-15,-77,]),'SE':([17,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,48,49,50,51,66,67,73,76,78,82,83,84,85,86,88,89,92,94,97,98,100,101,103,105,106,107,108,109,110,112,118,121,124,125,126,127,128,129,130,131,132,133,],[-14,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-9,-8,-12,-13,-71,-56,-81,-16,-50,-48,-52,-70,-54,-15,-28,102,-11,-77,-30,-29,-35,-34,-74,-36,-75,-81,-27,-31,-33,-32,102,-81,-39,-44,-42,102,-43,-40,-37,-81,102,-38,]),'SENAO':([17,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,48,49,50,51,66,67,76,78,82,83,84,85,86,88,92,94,97,98,100,101,103,105,106,108,109,110,112,121,124,125,126,127,128,129,130,133,],[-14,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-9,-8,-12,-13,-71,-56,-16,-50,-48,-52,-70,-54,-15,-28,-11,-77,-30,-29,-35,-34,-74,-36,-75,-27,-31,-33,-32,-81,-39,-44,-42,131,-43,-40,-37,-38,]),'MAIOR':([17,23,24,25,26,28,29,32,33,34,36,37,41,66,67,76,78,82,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,59,-76,-53,-55,-13,-74,-49,-51,-71,-56,-16,-50,59,-52,-70,-54,-15,-77,-74,-75,]),'error':([0,17,20,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,48,49,50,51,66,67,73,76,78,82,83,84,85,86,88,89,92,94,97,98,100,101,103,105,106,107,108,109,110,112,118,121,124,125,126,127,128,129,130,131,132,133,],[1,-14,48,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-9,-8,-12,-13,-71,-56,-81,-16,-50,-48,-52,-70,-54,-15,-28,105,-11,-77,-30,-29,-35,-34,-74,-36,-75,-81,-27,-31,-33,-32,105,-81,-39,-44,-42,105,-43,-40,-37,-81,105,-38,]),'E_LOGICO':([17,23,24,25,26,28,29,32,33,34,35,36,37,41,66,67,76,78,82,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,-47,-76,-53,-55,-13,61,-74,-49,-51,-71,-56,-16,-50,-48,-52,-70,-54,-15,-77,-74,-75,]),'ATRIBUT':([3,9,17,23,34,76,86,],[15,-13,-14,15,-13,-16,-15,]),'FECHA_PAR':([17,18,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,43,44,45,60,66,67,76,78,79,80,81,82,83,84,85,86,87,90,91,94,113,119,120,122,],[-14,-81,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,73,-23,-24,-81,-71,-56,-16,-50,94,-79,-80,-48,-52,-70,-54,-15,-22,-26,-25,-77,-78,125,126,128,]),'DIVISAO':([17,23,24,25,26,29,32,33,34,36,41,66,67,76,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,-76,-53,-55,-13,-74,68,-71,-56,-16,68,-70,-54,-15,-77,-74,-75,]),'ID':([0,1,2,4,5,6,7,10,11,12,13,14,15,16,17,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,73,75,76,77,78,82,83,84,85,86,88,89,92,93,94,97,98,99,100,101,102,103,105,106,107,108,109,110,112,114,115,117,118,121,123,124,125,126,127,128,129,130,131,132,133,],[9,-4,-5,-3,-18,-10,9,-20,-6,-17,21,-7,34,-2,-14,34,51,-19,-71,-72,-75,-73,-41,-47,-76,-67,-46,-53,-55,-13,-45,-74,-49,34,34,-66,-51,34,-9,-8,-12,-13,-59,-62,-61,-57,-63,34,-60,-58,34,-64,34,-65,34,-71,-56,-69,34,-68,-81,91,-16,51,-50,-48,-52,-70,-54,-15,-28,34,-11,34,-77,-30,-29,-21,-35,-34,34,-74,-36,-75,-81,-27,-31,-33,-32,34,120,34,34,-81,34,-39,-44,-42,34,-43,-40,-37,-81,34,-38,]),'LEIA':([17,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,48,49,50,51,66,67,73,76,78,82,83,84,85,86,88,89,92,94,97,98,100,101,103,105,106,107,108,109,110,112,118,121,124,125,126,127,128,129,130,131,132,133,],[-14,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-9,-8,-12,-13,-71,-56,-81,-16,-50,-48,-52,-70,-54,-15,-28,96,-11,-77,-30,-29,-35,-34,-74,-36,-75,-81,-27,-31,-33,-32,96,-81,-39,-44,-42,96,-43,-40,-37,-81,96,-38,]),'IGUAL':([17,23,24,25,26,28,29,32,33,34,36,37,41,66,67,76,78,82,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,52,-76,-53,-55,-13,-74,-49,-51,-71,-56,-16,-50,52,-52,-70,-54,-15,-77,-74,-75,]),'VIRGULA':([17,18,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,43,44,45,50,51,60,66,67,76,78,79,80,81,82,83,84,85,86,87,90,91,94,113,],[-14,-81,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,72,-23,-24,77,-13,-81,-71,-56,-16,-50,93,-79,-80,-48,-52,-70,-54,-15,-22,-26,-25,-77,-78,]),'INTEIRO':([0,1,2,4,6,7,10,11,14,15,16,17,18,19,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,72,73,76,78,82,83,84,85,86,88,89,92,93,94,97,98,99,100,101,102,103,105,106,107,108,109,110,112,114,117,118,121,123,124,125,126,127,128,129,130,131,132,133,],[12,-4,-5,-3,-10,12,-20,-6,-7,36,-2,-14,12,36,-19,-71,-72,-75,-73,-41,-47,-76,-67,-46,-53,-55,-13,-45,-74,-49,36,36,-66,-51,36,-9,-8,-12,-13,-59,-62,-61,-57,-63,36,-60,-58,36,-64,36,-65,36,-71,-56,-69,36,-68,12,-81,-16,-50,-48,-52,-70,-54,-15,-28,103,-11,36,-77,-30,-29,-21,-35,-34,36,-74,-36,-75,-81,-27,-31,-33,-32,36,36,103,-81,36,-39,-44,-42,103,-43,-40,-37,-81,103,-38,]),'ESCREVA':([17,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,48,49,50,51,66,67,73,76,78,82,83,84,85,86,88,89,92,94,97,98,100,101,103,105,106,107,108,109,110,112,118,121,124,125,126,127,128,129,130,131,132,133,],[-14,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-9,-8,-12,-13,-71,-56,-81,-16,-50,-48,-52,-70,-54,-15,-28,104,-11,-77,-30,-29,-35,-34,-74,-36,-75,-81,-27,-31,-33,-32,104,-81,-39,-44,-42,104,-43,-40,-37,-81,104,-38,]),'MENOR_IGUAL':([17,23,24,25,26,28,29,32,33,34,36,37,41,66,67,76,78,82,83,84,85,86,94,103,106,],[-14,-71,-72,-75,-73,54,-76,-53,-55,-13,-74,-49,-51,-71,-56,-16,-50,54,-52,-70,-54,-15,-77,-74,-75,]),'$end':([1,2,4,6,7,8,10,11,14,16,17,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,48,49,50,51,66,67,76,78,82,83,84,85,86,92,94,99,],[-4,-5,-3,-10,-1,0,-20,-6,-7,-2,-14,-19,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-9,-8,-12,-13,-71,-56,-16,-50,-48,-52,-70,-54,-15,-11,-77,-21,]),'ABRE_PAR':([9,21,34,95,96,104,],[18,18,60,114,115,117,]),'ABRE_COL':([9,15,17,19,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,73,76,78,82,83,84,85,86,87,88,89,90,91,92,93,94,97,98,100,101,102,103,105,106,107,108,109,110,112,114,117,118,121,123,124,125,126,127,128,129,130,131,132,133,],[19,38,42,38,-71,-72,-75,-73,-41,-47,-76,-67,-46,-53,-55,19,-45,-74,-49,38,38,-66,-51,38,74,-9,-8,-12,19,-59,-62,-61,-57,-63,38,-60,-58,38,-64,38,-65,38,-71,-56,-69,38,-68,-81,-16,-50,-48,-52,-70,-54,-15,74,-28,38,-26,-25,-11,38,-77,-30,-29,-35,-34,38,-74,-36,-75,-81,-27,-31,-33,-32,38,38,38,-81,38,-39,-44,-42,38,-43,-40,-37,-81,38,-38,]),'SOMA':([15,17,19,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,73,76,78,82,83,84,85,86,88,89,92,93,94,97,98,100,101,102,103,105,106,107,108,109,110,112,114,117,118,121,123,124,125,126,127,128,129,130,131,132,133,],[40,-14,40,-71,-72,-75,-73,-41,-47,-76,-67,-46,-53,-55,-13,-45,-74,40,40,-66,-51,40,-9,-8,-12,-13,-59,-62,-61,-57,-63,40,-60,-58,40,-64,40,-65,40,-71,-56,-69,40,-68,-81,-16,40,-48,-52,-70,-54,-15,-28,40,-11,40,-77,-30,-29,-35,-34,40,-74,-36,-75,-81,-27,-31,-33,-32,40,40,40,-81,40,-39,-44,-42,40,-43,-40,-37,-81,40,-38,]),'ATE':([17,23,24,25,26,27,28,29,31,32,33,34,35,36,37,41,48,49,50,51,66,67,76,78,82,83,84,85,86,88,92,94,97,98,100,101,103,105,106,107,108,109,110,112,118,124,125,126,128,129,130,133,],[-14,-71,-72,-75,-73,-41,-47,-76,-46,-53,-55,-13,-45,-74,-49,-51,-9,-8,-12,-13,-71,-56,-16,-50,-48,-52,-70,-54,-15,-28,-11,-77,-30,-29,-35,-34,-74,-36,-75,-81,-27,-31,-33,-32,123,-39,-44,-42,-43,-40,-37,-38,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'var':([0,7,15,19,20,38,39,42,57,60,62,64,69,77,89,93,102,114,117,118,123,127,132,],[3,3,23,23,50,23,66,23,66,23,66,66,66,50,23,23,23,23,23,23,23,23,23,]),'declaracao_variaveis':([0,7,89,118,127,132,],[2,2,97,97,97,97,]),'parametro':([18,72,],[44,87,]),'chamada_funcao':([15,19,38,39,42,57,60,62,64,69,89,93,102,114,117,118,123,127,132,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'inicializacao_variaveis':([0,7,],[11,11,]),'repita':([89,118,127,132,],[112,112,112,112,]),'numero':([15,19,38,39,42,57,60,62,64,69,89,93,102,114,117,118,123,127,132,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'lista_argumentos':([60,],[79,]),'expressao':([15,19,38,42,60,89,93,102,114,117,118,123,127,132,],[27,47,65,71,80,98,113,116,119,122,98,129,98,98,]),'expressao_simples':([15,19,38,42,60,62,89,93,102,114,117,118,123,127,132,],[28,28,28,28,28,82,28,28,28,28,28,28,28,28,28,]),'lista_parametros':([18,],[43,]),'lista_declaracoes':([0,],[7,]),'retorna':([89,118,127,132,],[100,100,100,100,]),'acao':([89,118,127,132,],[108,108,108,108,]),'atribuicao':([0,7,15,19,38,42,60,89,93,102,114,117,118,123,127,132,],[6,6,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'expressao_unaria':([15,19,38,42,57,60,62,64,69,89,93,102,114,117,118,123,127,132,],[32,32,32,32,32,32,32,32,85,32,32,32,32,32,32,32,32,32,]),'fator':([15,19,38,39,42,57,60,62,64,69,89,93,102,114,117,118,123,127,132,],[33,33,33,67,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'programa':([0,],[8,]),'operador_multiplicacao':([41,83,],[69,69,]),'operador_relacional':([28,82,],[57,57,]),'ate':([118,],[124,]),'leia':([89,118,127,132,],[110,110,110,110,]),'declaracao_funcao':([0,7,],[14,14,]),'corpo':([73,107,121,131,],[89,118,127,132,]),'declaracao':([0,7,],[4,16,]),'escreva':([89,118,127,132,],[101,101,101,101,]),'expressao_logica':([15,19,38,42,60,89,93,102,114,117,118,123,127,132,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'cabecalho':([0,7,13,],[10,10,22,]),'lista_variaveis':([20,77,],[49,92,]),'expressao_aditiva':([15,19,38,42,57,60,62,89,93,102,114,117,118,123,127,132,],[37,37,37,37,78,37,37,37,37,37,37,37,37,37,37,37,]),'se':([89,118,127,132,],[109,109,109,109,]),'operador_soma':([15,19,37,38,42,57,60,62,64,69,78,89,93,102,114,117,118,123,127,132,],[39,39,64,39,39,39,39,39,39,39,64,39,39,39,39,39,39,39,39,39,]),'vazio':([18,60,73,107,121,131,],[45,81,88,88,88,88,]),'tipo':([0,7,18,72,89,118,127,132,],[13,13,46,46,111,111,111,111,]),'expressao_multiplicativa':([15,19,38,42,57,60,62,64,89,93,102,114,117,118,123,127,132,],[41,41,41,41,41,41,41,83,41,41,41,41,41,41,41,41,41,]),'indice':([9,34,51,],[17,17,17,]),'operador_logico':([35,],[62,]),}

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
  ('repita -> REPITA corpo ate','repita',3,'p_repita','syntax.py',279),
  ('ate -> ATE expressao','ate',2,'p_ate','syntax.py',287),
  ('atribuicao -> var ATRIBUT expressao','atribuicao',3,'p_atribuicao','syntax.py',301),
  ('leia -> LEIA ABRE_PAR ID FECHA_PAR','leia',4,'p_leia','syntax.py',310),
  ('escreva -> ESCREVA ABRE_PAR expressao FECHA_PAR','escreva',4,'p_escreva','syntax.py',317),
  ('retorna -> RETORNA ABRE_PAR expressao FECHA_PAR','retorna',4,'p_retorna','syntax.py',324),
  ('expressao -> expressao_logica','expressao',1,'p_expressao','syntax.py',331),
  ('expressao -> atribuicao','expressao',1,'p_expressao','syntax.py',332),
  ('expressao_logica -> expressao_simples','expressao_logica',1,'p_expressao_logica','syntax.py',339),
  ('expressao_logica -> expressao_logica operador_logico expressao_simples','expressao_logica',3,'p_expressao_logica','syntax.py',340),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','syntax.py',353),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','syntax.py',354),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','syntax.py',366),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','syntax.py',367),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','syntax.py',379),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','syntax.py',380),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','syntax.py',393),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','syntax.py',394),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','syntax.py',406),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','syntax.py',407),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',408),
  ('operador_relacional -> DIFERENCA','operador_relacional',1,'p_operador_relacional','syntax.py',409),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',410),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',411),
  ('operador_relacional -> NEGACAO','operador_relacional',1,'p_operador_relacional','syntax.py',412),
  ('operador_logico -> E_LOGICO','operador_logico',1,'p_operador_logico','syntax.py',419),
  ('operador_logico -> OU_LOGICO','operador_logico',1,'p_operador_logico','syntax.py',420),
  ('operador_soma -> SOMA','operador_soma',1,'p_operador_soma','syntax.py',429),
  ('operador_soma -> SUB','operador_soma',1,'p_operador_soma','syntax.py',430),
  ('operador_multiplicacao -> MULT','operador_multiplicacao',1,'p_operador_multiplicacao','syntax.py',444),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','syntax.py',445),
  ('fator -> ABRE_COL expressao FECHA_COL','fator',3,'p_fator','syntax.py',452),
  ('fator -> var','fator',1,'p_fator','syntax.py',453),
  ('fator -> chamada_funcao','fator',1,'p_fator','syntax.py',454),
  ('fator -> numero','fator',1,'p_fator','syntax.py',455),
  ('numero -> INTEIRO','numero',1,'p_numero','syntax.py',466),
  ('numero -> FLUTUANTE','numero',1,'p_numero','syntax.py',467),
  ('numero -> NOTACAO_CIENTIFICA','numero',1,'p_numero','syntax.py',468),
  ('chamada_funcao -> ID ABRE_PAR lista_argumentos FECHA_PAR','chamada_funcao',4,'p_chamada_funcao','syntax.py',475),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','syntax.py',483),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','syntax.py',484),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','syntax.py',485),
  ('vazio -> <empty>','vazio',0,'p_vazio','syntax.py',496),
]
