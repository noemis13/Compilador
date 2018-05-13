
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVISAO MULT VIRGULA ATRIBUT MENOR MAIOR IGUAL MENOR_IGUAL MAIOR_IGUAL ABRE_PAR FECHA_PAR DOIS_PONTOS E_LOGICO OU_LOGICO SOMA SUB DIFERENCA ABRE_COL FECHA_COL NOTACAO_CIENTIFICA ID NEGACAO REPITA ATE SE FLUTUANTE FIM INTEIRO SENAO ENTAO RETORNA LEIA ESCREVA\n        programa : lista_declaracoes\n        \n        lista_declaracoes : lista_declaracoes declaracao\n                           | declaracao\n\t\t\t   | error\n        \n        declaracao : declaracao_variaveis\n                    | inicializacao_variaveis\n                    | declaracao_funcao\n        \n        declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n        \n        declaracao_variaveis : tipo DOIS_PONTOS error\n        \n        inicializacao_variaveis : atribuicao\n        \n        lista_variaveis : lista_variaveis VIRGULA var\n                        | var\n        \n        var : ID\n            | ID indice\n        \n        indice : indice ABRE_COL expressao FECHA_COL\n                | ABRE_COL expressao FECHA_COL\n        \n        indice : indice ABRE_COL error FECHA_COL\n                | ABRE_COL error FECHA_COL\n\t\t| error FECHA_COL\n\t\t| ABRE_COL error\n        \t| indice error FECHA_COL\n\t\t| indice ABRE_COL error\n\t\t\n        \n        tipo : INTEIRO\n\t     | FLUTUANTE\n        \n        declaracao_funcao : tipo cabecalho\n                          | cabecalho\n        \n        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM\n        \n        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo error\n        \n        lista_parametros : lista_parametros VIRGULA parametro\n                            | parametro\n                            | vazio\n        \n        parametro : tipo DOIS_PONTOS ID\n\t\t  | parametro ABRE_COL FECHA_COL\n        \n        corpo : corpo acao\n                | vazio\n        \n        acao : expressao\n             | declaracao_variaveis\n             | se\n             | repita\n             | leia\n             | escreva\n             | retorna\n        \n            se : SE expressao ENTAO corpo FIM\n               | SE expressao ENTAO corpo SENAO corpo FIM\n        \n            se : SE expressao error corpo FIM\n               | error SENAO corpo FIM\n        \n            repita : REPITA corpo ATE expressao\n        \n            repita : REPITA corpo error\n        \n            atribuicao : var ATRIBUT expressao\n        \n            leia : LEIA ABRE_PAR var FECHA_PAR\n        \n            escreva : ESCREVA ABRE_PAR expressao FECHA_PAR\n        \n            retorna : RETORNA ABRE_PAR expressao FECHA_PAR\n        \n            expressao : expressao_logica\n                        | atribuicao\n        \n            expressao_logica : expressao_simples\n                             | expressao_logica operador_logico expressao_simples\n        \n            expressao_simples : expressao_aditiva\n                                | expressao_simples operador_relacional expressao_aditiva\n        \n            expressao_aditiva : expressao_multiplicativa\n                                | expressao_aditiva operador_soma expressao_multiplicativa\n        \n           expressao_multiplicativa : expressao_unaria\n                           \t    | expressao_multiplicativa operador_multiplicacao expressao_unaria\n\n        \n            expressao_unaria : fator\n                             | operador_soma fator\n\t\t\t     | operador_negacao fator\n        \n            operador_relacional : MENOR\n                                | MAIOR\n                                | IGUAL\n\t\t\t\t| DIFERENCA\n                                | MENOR_IGUAL\n                                | MAIOR_IGUAL\n        \n            operador_soma : SOMA\n                          | SUB\n        \n            operador_negacao : NEGACAO\n        \n            operador_logico : E_LOGICO\n                            | OU_LOGICO\n        \n            operador_multiplicacao : MULT\n                                    | DIVISAO\n        \n            fator : ABRE_COL expressao FECHA_COL\n                  | var\n                  | chamada_funcao\n                  | numero\n        \n            numero : INTEIRO\n                   | FLUTUANTE\n\t\t   | NOTACAO_CIENTIFICA\n        \n            chamada_funcao : ID ABRE_PAR lista_argumentos FECHA_PAR\n        \n            lista_argumentos : lista_argumentos VIRGULA expressao\n                            | expressao\n                            | vazio\n        \n            vazio : \n        '
    
_lr_action_items = {'FIM':([22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,47,48,54,57,65,66,67,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,106,108,110,112,114,117,119,120,121,122,127,130,131,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,-8,-9,-12,-20,-19,-80,-65,-64,-90,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,113,-15,-17,-86,-42,-37,-34,-84,-39,-36,-40,-41,-83,-38,-90,-90,-90,-48,143,147,148,-47,-50,-46,-52,-51,-90,-43,-45,150,-44,]),'MENOR':([22,25,26,27,29,30,31,36,37,39,40,41,43,54,57,65,66,67,82,83,85,86,87,88,89,90,94,101,102,103,112,121,],[-14,-82,-85,-80,-59,-61,-63,-83,-81,69,-13,-84,-57,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,69,-58,-60,-15,-17,-86,-84,-83,]),'MAIOR_IGUAL':([22,25,26,27,29,30,31,36,37,39,40,41,43,54,57,65,66,67,82,83,85,86,87,88,89,90,94,101,102,103,112,121,],[-14,-82,-85,-80,-59,-61,-63,-83,-81,73,-13,-84,-57,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,73,-58,-60,-15,-17,-86,-84,-83,]),'ID':([0,1,2,5,6,7,8,9,10,11,13,14,15,17,18,19,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,81,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,104,105,106,107,108,110,111,112,113,114,117,119,120,121,122,125,126,127,128,129,130,131,132,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[12,-7,-26,-6,16,-3,-23,12,-4,-5,-24,-10,40,45,-25,-2,40,-14,-72,-82,-85,-80,-73,-59,-61,-63,40,-53,-49,40,-83,-81,40,-55,-13,-84,-74,-57,-54,-13,-8,-9,-12,-20,40,-19,40,-78,-77,-76,40,-75,-80,-65,-64,-68,-66,40,-67,-69,-71,-70,40,40,45,-90,100,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,40,-15,-17,-86,40,40,-42,-90,-37,-34,-28,-84,-27,-39,-36,-40,-41,-83,-38,40,45,-90,40,40,-90,-90,40,-48,40,40,40,-47,-50,-46,-52,-51,-90,-43,-45,40,-44,]),'FECHA_PAR':([20,22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,49,50,51,54,57,65,66,67,75,82,83,85,86,87,88,89,90,91,92,93,94,98,99,100,101,102,103,123,134,136,137,],[-90,-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,78,-30,-31,-20,-19,-80,-65,-64,-90,-16,-18,-22,-21,-62,-79,-56,-58,-89,103,-88,-60,-29,-33,-32,-15,-17,-86,-87,141,144,145,]),'SOMA':([15,21,22,24,25,26,27,28,29,30,31,32,33,34,36,37,39,40,41,43,44,45,46,47,48,54,55,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,104,105,106,107,108,110,112,114,117,119,120,121,122,125,127,128,129,130,131,132,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[24,24,-14,-72,-82,-85,-80,-73,-59,-61,-63,24,-53,-49,-83,-81,-55,-13,-84,24,-54,-13,-8,-9,-12,-20,24,-19,24,-78,-77,-76,24,-75,-80,-65,-64,-68,-66,24,-67,-69,-71,-70,24,24,-90,-16,-18,-22,-21,-62,-79,-56,24,-60,-11,-35,24,-15,-17,-86,24,24,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,24,-90,24,24,-90,-90,24,-48,24,24,24,-47,-50,-46,-52,-51,-90,-43,-45,24,-44,]),'FLUTUANTE':([0,1,2,5,7,9,10,11,14,15,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,104,105,106,107,108,110,111,112,113,114,117,119,120,121,122,125,127,128,129,130,131,132,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[13,-7,-26,-6,-3,13,-4,-5,-10,41,-25,-2,13,41,-14,-72,-82,-85,-80,-73,-59,-61,-63,41,-53,-49,41,-83,-81,41,-55,-13,-84,-74,-57,-54,-13,-8,-9,-12,-20,41,-19,41,-78,-77,-76,41,-75,-80,-65,-64,-68,-66,41,-67,-69,-71,-70,41,41,-90,13,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,112,-15,-17,-86,41,41,-42,-90,-37,-34,-28,-84,-27,-39,-36,-40,-41,-83,-38,112,-90,41,41,-90,-90,41,-48,112,112,112,-47,-50,-46,-52,-51,-90,-43,-45,112,-44,]),'DIVISAO':([22,25,26,27,29,30,31,36,37,40,41,54,57,65,66,67,82,83,85,86,87,88,94,101,102,103,112,121,],[-14,-82,-85,-80,59,-61,-63,-83,-81,-13,-84,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,59,-15,-17,-86,-84,-83,]),'SUB':([15,21,22,24,25,26,27,28,29,30,31,32,33,34,36,37,39,40,41,43,44,45,46,47,48,54,55,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,104,105,106,107,108,110,112,114,117,119,120,121,122,125,127,128,129,130,131,132,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[28,28,-14,-72,-82,-85,-80,-73,-59,-61,-63,28,-53,-49,-83,-81,-55,-13,-84,28,-54,-13,-8,-9,-12,-20,28,-19,28,-78,-77,-76,28,-75,-80,-65,-64,-68,-66,28,-67,-69,-71,-70,28,28,-90,-16,-18,-22,-21,-62,-79,-56,28,-60,-11,-35,28,-15,-17,-86,28,28,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,28,-90,28,28,-90,-90,28,-48,28,28,28,-47,-50,-46,-52,-51,-90,-43,-45,28,-44,]),'VIRGULA':([20,22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,48,49,50,51,54,57,65,66,67,75,82,83,85,86,87,88,89,90,91,92,93,94,95,98,99,100,101,102,103,123,],[-90,-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,77,-12,79,-30,-31,-20,-19,-80,-65,-64,-90,-16,-18,-22,-21,-62,-79,-56,-58,-89,104,-88,-60,-11,-29,-33,-32,-15,-17,-86,-87,]),'$end':([1,2,4,5,7,9,10,11,14,18,19,22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,47,48,54,57,65,66,67,82,83,85,86,87,88,89,90,94,95,101,102,103,111,113,],[-7,-26,0,-6,-3,-1,-4,-5,-10,-25,-2,-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,-8,-9,-12,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-15,-17,-86,-28,-27,]),'NOTACAO_CIENTIFICA':([15,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,104,105,106,107,108,110,112,114,117,119,120,121,122,125,127,128,129,130,131,132,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[26,26,-14,-72,-82,-85,-80,-73,-59,-61,-63,26,-53,-49,26,-83,-81,26,-55,-13,-84,-74,-57,-54,-13,-8,-9,-12,-20,26,-19,26,-78,-77,-76,26,-75,-80,-65,-64,-68,-66,26,-67,-69,-71,-70,26,26,-90,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,26,-15,-17,-86,26,26,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,26,-90,26,26,-90,-90,26,-48,26,26,26,-47,-50,-46,-52,-51,-90,-43,-45,26,-44,]),'SENAO':([22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,47,48,54,57,65,66,67,82,83,85,86,87,88,89,90,94,95,96,101,102,103,106,108,110,111,112,114,117,119,120,121,122,130,133,138,140,141,142,143,144,145,147,148,150,],[-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,-8,-9,-12,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,-15,-17,-86,-42,-37,-34,127,-84,-39,-36,-40,-41,-83,-38,-90,127,146,-47,-50,127,-46,-52,-51,-43,-45,-44,]),'SE':([22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,47,48,54,57,65,66,67,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,106,107,108,110,112,114,117,119,120,121,122,125,127,130,131,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,-8,-9,-12,-20,-19,-80,-65,-64,-90,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,105,-15,-17,-86,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,105,-90,-90,-90,-48,105,105,105,-47,-50,-46,-52,-51,-90,-43,-45,105,-44,]),'ABRE_COL':([12,15,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,54,55,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,83,85,86,87,88,89,90,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,110,112,114,117,119,120,121,122,125,127,128,129,130,131,132,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[21,32,32,55,-72,-82,-85,-80,-73,-59,-61,-63,32,-53,-49,32,-83,-81,32,-55,21,-84,-74,-57,-54,21,-8,-9,-12,80,-20,32,-19,32,-78,-77,-76,32,-75,-80,-65,-64,-68,-66,32,-67,-69,-71,-70,32,32,-90,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,32,80,-33,-32,-15,-17,-86,32,32,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,32,-90,32,32,-90,-90,32,-48,32,32,32,-47,-50,-46,-52,-51,-90,-43,-45,32,-44,]),'REPITA':([22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,47,48,54,57,65,66,67,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,106,107,108,110,112,114,117,119,120,121,122,125,127,130,131,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,-8,-9,-12,-20,-19,-80,-65,-64,-90,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,107,-15,-17,-86,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,107,-90,-90,-90,-48,107,107,107,-47,-50,-46,-52,-51,-90,-43,-45,107,-44,]),'MENOR_IGUAL':([22,25,26,27,29,30,31,36,37,39,40,41,43,54,57,65,66,67,82,83,85,86,87,88,89,90,94,101,102,103,112,121,],[-14,-82,-85,-80,-59,-61,-63,-83,-81,74,-13,-84,-57,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,74,-58,-60,-15,-17,-86,-84,-83,]),'ATRIBUT':([3,12,22,27,40,54,57,82,83,85,86,101,102,],[15,-13,-14,15,-13,-20,-19,-16,-18,-22,-21,-15,-17,]),'RETORNA':([22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,47,48,54,57,65,66,67,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,106,107,108,110,112,114,117,119,120,121,122,125,127,130,131,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,-8,-9,-12,-20,-19,-80,-65,-64,-90,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,115,-15,-17,-86,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,115,-90,-90,-90,-48,115,115,115,-47,-50,-46,-52,-51,-90,-43,-45,115,-44,]),'OU_LOGICO':([22,25,26,27,29,30,31,33,36,37,39,40,41,43,54,57,65,66,67,82,83,85,86,87,88,89,90,94,101,102,103,112,121,],[-14,-82,-85,-80,-59,-61,-63,62,-83,-81,-55,-13,-84,-57,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,-56,-58,-60,-15,-17,-86,-84,-83,]),'INTEIRO':([0,1,2,5,7,9,10,11,14,15,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,104,105,106,107,108,110,111,112,113,114,117,119,120,121,122,125,127,128,129,130,131,132,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[8,-7,-26,-6,-3,8,-4,-5,-10,36,-25,-2,8,36,-14,-72,-82,-85,-80,-73,-59,-61,-63,36,-53,-49,36,-83,-81,36,-55,-13,-84,-74,-57,-54,-13,-8,-9,-12,-20,36,-19,36,-78,-77,-76,36,-75,-80,-65,-64,-68,-66,36,-67,-69,-71,-70,36,36,-90,8,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,121,-15,-17,-86,36,36,-42,-90,-37,-34,-28,-84,-27,-39,-36,-40,-41,-83,-38,121,-90,36,36,-90,-90,36,-48,121,121,121,-47,-50,-46,-52,-51,-90,-43,-45,121,-44,]),'ESCREVA':([22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,47,48,54,57,65,66,67,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,106,107,108,110,112,114,117,119,120,121,122,125,127,130,131,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,-8,-9,-12,-20,-19,-80,-65,-64,-90,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,118,-15,-17,-86,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,118,-90,-90,-90,-48,118,118,118,-47,-50,-46,-52,-51,-90,-43,-45,118,-44,]),'FECHA_COL':([22,23,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,53,54,56,57,61,65,66,67,80,82,83,84,85,86,87,88,89,90,94,101,102,103,],[-14,57,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,82,83,86,-19,88,-80,-65,-64,99,-16,-18,101,102,-21,-62,-79,-56,-58,-60,-15,-17,-86,]),'error':([0,12,17,21,22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,47,48,54,55,57,65,66,67,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,106,107,108,110,112,114,117,119,120,121,122,124,125,127,130,131,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[10,23,47,54,56,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,23,-84,-57,-54,23,-8,-9,-12,-20,85,-19,-80,-65,-64,-90,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,111,-15,-17,-86,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,131,133,-90,-90,-90,-48,142,142,142,-47,-50,-46,-52,-51,-90,-43,-45,142,-44,]),'E_LOGICO':([22,25,26,27,29,30,31,33,36,37,39,40,41,43,54,57,65,66,67,82,83,85,86,87,88,89,90,94,101,102,103,112,121,],[-14,-82,-85,-80,-59,-61,-63,64,-83,-81,-55,-13,-84,-57,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,-56,-58,-60,-15,-17,-86,-84,-83,]),'ABRE_PAR':([12,16,40,109,115,118,],[20,20,75,126,128,129,]),'LEIA':([22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,47,48,54,57,65,66,67,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,106,107,108,110,112,114,117,119,120,121,122,125,127,130,131,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,-8,-9,-12,-20,-19,-80,-65,-64,-90,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,109,-15,-17,-86,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,109,-90,-90,-90,-48,109,109,109,-47,-50,-46,-52,-51,-90,-43,-45,109,-44,]),'ATE':([22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,45,46,47,48,54,57,65,66,67,82,83,85,86,87,88,89,90,94,95,96,101,102,103,106,107,108,110,112,114,117,119,120,121,122,125,133,140,141,143,144,145,147,148,150,],[-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,-8,-9,-12,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,-15,-17,-86,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,132,-48,-47,-50,-46,-52,-51,-43,-45,-44,]),'DIFERENCA':([22,25,26,27,29,30,31,36,37,39,40,41,43,54,57,65,66,67,82,83,85,86,87,88,89,90,94,101,102,103,112,121,],[-14,-82,-85,-80,-59,-61,-63,-83,-81,72,-13,-84,-57,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,72,-58,-60,-15,-17,-86,-84,-83,]),'MAIOR':([22,25,26,27,29,30,31,36,37,39,40,41,43,54,57,65,66,67,82,83,85,86,87,88,89,90,94,101,102,103,112,121,],[-14,-82,-85,-80,-59,-61,-63,-83,-81,71,-13,-84,-57,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,71,-58,-60,-15,-17,-86,-84,-83,]),'DOIS_PONTOS':([6,8,13,52,112,116,121,],[17,-23,-24,81,-24,17,-23,]),'NEGACAO':([15,21,22,24,25,26,27,28,29,30,31,32,33,34,36,37,39,40,41,43,44,45,46,47,48,54,55,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,82,83,85,86,87,88,89,90,94,95,96,97,101,102,103,104,105,106,107,108,110,112,114,117,119,120,121,122,125,127,128,129,130,131,132,133,135,138,139,140,141,143,144,145,146,147,148,149,150,],[42,42,-14,-72,-82,-85,-80,-73,-59,-61,-63,42,-53,-49,-83,-81,-55,-13,-84,-57,-54,-13,-8,-9,-12,-20,42,-19,42,-78,-77,-76,42,-75,-80,-65,-64,-68,-66,42,-67,-69,-71,-70,42,42,-90,-16,-18,-22,-21,-62,-79,-56,-58,-60,-11,-35,42,-15,-17,-86,42,42,-42,-90,-37,-34,-84,-39,-36,-40,-41,-83,-38,42,-90,42,42,-90,-90,42,-48,42,42,42,-47,-50,-46,-52,-51,-90,-43,-45,42,-44,]),'ENTAO':([22,25,26,27,29,30,31,33,34,36,37,39,40,41,43,44,54,57,65,66,67,82,83,85,86,87,88,89,90,94,101,102,103,124,],[-14,-82,-85,-80,-59,-61,-63,-53,-49,-83,-81,-55,-13,-84,-57,-54,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,-56,-58,-60,-15,-17,-86,130,]),'MULT':([22,25,26,27,29,30,31,36,37,40,41,54,57,65,66,67,82,83,85,86,87,88,94,101,102,103,112,121,],[-14,-82,-85,-80,60,-61,-63,-83,-81,-13,-84,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,60,-15,-17,-86,-84,-83,]),'IGUAL':([22,25,26,27,29,30,31,36,37,39,40,41,43,54,57,65,66,67,82,83,85,86,87,88,89,90,94,101,102,103,112,121,],[-14,-82,-85,-80,-59,-61,-63,-83,-81,68,-13,-84,-57,-20,-19,-80,-65,-64,-16,-18,-22,-21,-62,-79,68,-58,-60,-15,-17,-86,-84,-83,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'repita':([97,125,135,138,139,149,],[114,114,114,114,114,114,]),'numero':([15,21,32,35,38,55,58,63,70,75,76,97,104,105,125,128,129,132,135,138,139,149,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'declaracao_funcao':([0,9,],[1,1,]),'lista_declaracoes':([0,],[9,]),'se':([97,125,135,138,139,149,],[122,122,122,122,122,122,]),'cabecalho':([0,6,9,],[2,18,2,]),'expressao':([15,21,32,55,75,97,104,105,125,128,129,132,135,138,139,149,],[34,53,61,84,93,117,123,124,117,136,137,140,117,117,117,117,]),'var':([0,9,15,17,21,32,35,38,55,58,63,70,75,76,77,97,104,105,125,126,128,129,132,135,138,139,149,],[3,3,27,48,27,27,65,65,27,65,65,65,27,65,95,27,27,27,27,134,27,27,27,27,27,27,27,]),'programa':([0,],[4,]),'lista_parametros':([20,],[49,]),'vazio':([20,75,78,107,127,130,131,146,],[51,91,96,96,96,96,96,96,]),'operador_relacional':([39,89,],[70,70,]),'lista_argumentos':([75,],[92,]),'inicializacao_variaveis':([0,9,],[5,5,]),'expressao_multiplicativa':([15,21,32,55,63,70,75,76,97,104,105,125,128,129,132,135,138,139,149,],[29,29,29,29,29,29,29,94,29,29,29,29,29,29,29,29,29,29,29,]),'expressao_unaria':([15,21,32,55,58,63,70,75,76,97,104,105,125,128,129,132,135,138,139,149,],[30,30,30,30,87,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'parametro':([20,79,],[50,98,]),'lista_variaveis':([17,],[46,]),'tipo':([0,9,20,79,97,125,135,138,139,149,],[6,6,52,52,116,116,116,116,116,116,]),'fator':([15,21,32,35,38,55,58,63,70,75,76,97,104,105,125,128,129,132,135,138,139,149,],[31,31,31,66,67,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'operador_logico':([33,],[63,]),'expressao_logica':([15,21,32,55,75,97,104,105,125,128,129,132,135,138,139,149,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'declaracao':([0,9,],[7,19,]),'operador_negacao':([15,21,32,55,58,63,70,75,76,97,104,105,125,128,129,132,135,138,139,149,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'escreva':([97,125,135,138,139,149,],[120,120,120,120,120,120,]),'retorna':([97,125,135,138,139,149,],[106,106,106,106,106,106,]),'chamada_funcao':([15,21,32,35,38,55,58,63,70,75,76,97,104,105,125,128,129,132,135,138,139,149,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'acao':([97,125,135,138,139,149,],[110,110,110,110,110,110,]),'leia':([97,125,135,138,139,149,],[119,119,119,119,119,119,]),'corpo':([78,107,127,130,131,146,],[97,125,135,138,139,149,]),'operador_soma':([15,21,32,43,55,58,63,70,75,76,90,97,104,105,125,128,129,132,135,138,139,149,],[38,38,38,76,38,38,38,38,38,38,76,38,38,38,38,38,38,38,38,38,38,38,]),'declaracao_variaveis':([0,9,97,125,135,138,139,149,],[11,11,108,108,108,108,108,108,]),'operador_multiplicacao':([29,94,],[58,58,]),'expressao_simples':([15,21,32,55,63,75,97,104,105,125,128,129,132,135,138,139,149,],[39,39,39,39,89,39,39,39,39,39,39,39,39,39,39,39,39,]),'expressao_aditiva':([15,21,32,55,63,70,75,97,104,105,125,128,129,132,135,138,139,149,],[43,43,43,43,43,90,43,43,43,43,43,43,43,43,43,43,43,43,]),'indice':([12,40,45,],[22,22,22,]),'atribuicao':([0,9,15,21,32,55,75,97,104,105,125,128,129,132,135,138,139,149,],[14,14,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> lista_declaracoes','programa',1,'p_programa','syntax.py',30),
  ('lista_declaracoes -> lista_declaracoes declaracao','lista_declaracoes',2,'p_lista_declaracoes','syntax.py',36),
  ('lista_declaracoes -> declaracao','lista_declaracoes',1,'p_lista_declaracoes','syntax.py',37),
  ('lista_declaracoes -> error','lista_declaracoes',1,'p_lista_declaracoes','syntax.py',38),
  ('declaracao -> declaracao_variaveis','declaracao',1,'p_declaracao','syntax.py',50),
  ('declaracao -> inicializacao_variaveis','declaracao',1,'p_declaracao','syntax.py',51),
  ('declaracao -> declaracao_funcao','declaracao',1,'p_declaracao','syntax.py',52),
  ('declaracao_variaveis -> tipo DOIS_PONTOS lista_variaveis','declaracao_variaveis',3,'p_declaracao_variaveis','syntax.py',59),
  ('declaracao_variaveis -> tipo DOIS_PONTOS error','declaracao_variaveis',3,'p_declaracao_variaveis_error','syntax.py',65),
  ('inicializacao_variaveis -> atribuicao','inicializacao_variaveis',1,'p_inicializacao_variaveis','syntax.py',72),
  ('lista_variaveis -> lista_variaveis VIRGULA var','lista_variaveis',3,'p_lista_variaveis','syntax.py',79),
  ('lista_variaveis -> var','lista_variaveis',1,'p_lista_variaveis','syntax.py',80),
  ('var -> ID','var',1,'p_var','syntax.py',89),
  ('var -> ID indice','var',2,'p_var','syntax.py',90),
  ('indice -> indice ABRE_COL expressao FECHA_COL','indice',4,'p_indice','syntax.py',99),
  ('indice -> ABRE_COL expressao FECHA_COL','indice',3,'p_indice','syntax.py',100),
  ('indice -> indice ABRE_COL error FECHA_COL','indice',4,'p_indice_error','syntax.py',109),
  ('indice -> ABRE_COL error FECHA_COL','indice',3,'p_indice_error','syntax.py',110),
  ('indice -> error FECHA_COL','indice',2,'p_indice_error','syntax.py',111),
  ('indice -> ABRE_COL error','indice',2,'p_indice_error','syntax.py',112),
  ('indice -> indice error FECHA_COL','indice',3,'p_indice_error','syntax.py',113),
  ('indice -> indice ABRE_COL error','indice',3,'p_indice_error','syntax.py',114),
  ('tipo -> INTEIRO','tipo',1,'p_tipo','syntax.py',121),
  ('tipo -> FLUTUANTE','tipo',1,'p_tipo','syntax.py',122),
  ('declaracao_funcao -> tipo cabecalho','declaracao_funcao',2,'p_declaracao_funcao','syntax.py',129),
  ('declaracao_funcao -> cabecalho','declaracao_funcao',1,'p_declaracao_funcao','syntax.py',130),
  ('cabecalho -> ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM','cabecalho',6,'p_cabecalho','syntax.py',139),
  ('cabecalho -> ID ABRE_PAR lista_parametros FECHA_PAR corpo error','cabecalho',6,'p_cabecalho_error','syntax.py',145),
  ('lista_parametros -> lista_parametros VIRGULA parametro','lista_parametros',3,'p_lista_parametros','syntax.py',151),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros','syntax.py',152),
  ('lista_parametros -> vazio','lista_parametros',1,'p_lista_parametros','syntax.py',153),
  ('parametro -> tipo DOIS_PONTOS ID','parametro',3,'p_parametro','syntax.py',162),
  ('parametro -> parametro ABRE_COL FECHA_COL','parametro',3,'p_parametro','syntax.py',163),
  ('corpo -> corpo acao','corpo',2,'p_corpo','syntax.py',173),
  ('corpo -> vazio','corpo',1,'p_corpo','syntax.py',174),
  ('acao -> expressao','acao',1,'p_acao','syntax.py',183),
  ('acao -> declaracao_variaveis','acao',1,'p_acao','syntax.py',184),
  ('acao -> se','acao',1,'p_acao','syntax.py',185),
  ('acao -> repita','acao',1,'p_acao','syntax.py',186),
  ('acao -> leia','acao',1,'p_acao','syntax.py',187),
  ('acao -> escreva','acao',1,'p_acao','syntax.py',188),
  ('acao -> retorna','acao',1,'p_acao','syntax.py',189),
  ('se -> SE expressao ENTAO corpo FIM','se',5,'p_se','syntax.py',195),
  ('se -> SE expressao ENTAO corpo SENAO corpo FIM','se',7,'p_se','syntax.py',196),
  ('se -> SE expressao error corpo FIM','se',5,'p_se_error','syntax.py',205),
  ('se -> error SENAO corpo FIM','se',4,'p_se_error','syntax.py',206),
  ('repita -> REPITA corpo ATE expressao','repita',4,'p_repita','syntax.py',215),
  ('repita -> REPITA corpo error','repita',3,'p_repita_error','syntax.py',221),
  ('atribuicao -> var ATRIBUT expressao','atribuicao',3,'p_atribuicao','syntax.py',228),
  ('leia -> LEIA ABRE_PAR var FECHA_PAR','leia',4,'p_leia','syntax.py',235),
  ('escreva -> ESCREVA ABRE_PAR expressao FECHA_PAR','escreva',4,'p_escreva','syntax.py',242),
  ('retorna -> RETORNA ABRE_PAR expressao FECHA_PAR','retorna',4,'p_retorna','syntax.py',248),
  ('expressao -> expressao_logica','expressao',1,'p_expressao','syntax.py',254),
  ('expressao -> atribuicao','expressao',1,'p_expressao','syntax.py',255),
  ('expressao_logica -> expressao_simples','expressao_logica',1,'p_expressao_logica','syntax.py',261),
  ('expressao_logica -> expressao_logica operador_logico expressao_simples','expressao_logica',3,'p_expressao_logica','syntax.py',262),
  ('expressao_simples -> expressao_aditiva','expressao_simples',1,'p_expressao_simples','syntax.py',272),
  ('expressao_simples -> expressao_simples operador_relacional expressao_aditiva','expressao_simples',3,'p_expressao_simples','syntax.py',273),
  ('expressao_aditiva -> expressao_multiplicativa','expressao_aditiva',1,'p_expressao_aditiva','syntax.py',282),
  ('expressao_aditiva -> expressao_aditiva operador_soma expressao_multiplicativa','expressao_aditiva',3,'p_expressao_aditiva','syntax.py',283),
  ('expressao_multiplicativa -> expressao_unaria','expressao_multiplicativa',1,'p_expressao_multiplicativa','syntax.py',292),
  ('expressao_multiplicativa -> expressao_multiplicativa operador_multiplicacao expressao_unaria','expressao_multiplicativa',3,'p_expressao_multiplicativa','syntax.py',293),
  ('expressao_unaria -> fator','expressao_unaria',1,'p_expressao_unaria','syntax.py',303),
  ('expressao_unaria -> operador_soma fator','expressao_unaria',2,'p_expressao_unaria','syntax.py',304),
  ('expressao_unaria -> operador_negacao fator','expressao_unaria',2,'p_expressao_unaria','syntax.py',305),
  ('operador_relacional -> MENOR','operador_relacional',1,'p_operador_relacional','syntax.py',314),
  ('operador_relacional -> MAIOR','operador_relacional',1,'p_operador_relacional','syntax.py',315),
  ('operador_relacional -> IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',316),
  ('operador_relacional -> DIFERENCA','operador_relacional',1,'p_operador_relacional','syntax.py',317),
  ('operador_relacional -> MENOR_IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',318),
  ('operador_relacional -> MAIOR_IGUAL','operador_relacional',1,'p_operador_relacional','syntax.py',319),
  ('operador_soma -> SOMA','operador_soma',1,'p_operador_soma','syntax.py',326),
  ('operador_soma -> SUB','operador_soma',1,'p_operador_soma','syntax.py',327),
  ('operador_negacao -> NEGACAO','operador_negacao',1,'p_operador_negacao','syntax.py',334),
  ('operador_logico -> E_LOGICO','operador_logico',1,'p_operador_logico','syntax.py',342),
  ('operador_logico -> OU_LOGICO','operador_logico',1,'p_operador_logico','syntax.py',343),
  ('operador_multiplicacao -> MULT','operador_multiplicacao',1,'p_operador_multiplicacao','syntax.py',351),
  ('operador_multiplicacao -> DIVISAO','operador_multiplicacao',1,'p_operador_multiplicacao','syntax.py',352),
  ('fator -> ABRE_COL expressao FECHA_COL','fator',3,'p_fator','syntax.py',358),
  ('fator -> var','fator',1,'p_fator','syntax.py',359),
  ('fator -> chamada_funcao','fator',1,'p_fator','syntax.py',360),
  ('fator -> numero','fator',1,'p_fator','syntax.py',361),
  ('numero -> INTEIRO','numero',1,'p_numero','syntax.py',370),
  ('numero -> FLUTUANTE','numero',1,'p_numero','syntax.py',371),
  ('numero -> NOTACAO_CIENTIFICA','numero',1,'p_numero','syntax.py',372),
  ('chamada_funcao -> ID ABRE_PAR lista_argumentos FECHA_PAR','chamada_funcao',4,'p_chamada_funcao','syntax.py',378),
  ('lista_argumentos -> lista_argumentos VIRGULA expressao','lista_argumentos',3,'p_lista_argumentos','syntax.py',384),
  ('lista_argumentos -> expressao','lista_argumentos',1,'p_lista_argumentos','syntax.py',385),
  ('lista_argumentos -> vazio','lista_argumentos',1,'p_lista_argumentos','syntax.py',386),
  ('vazio -> <empty>','vazio',0,'p_vazio','syntax.py',395),
]
