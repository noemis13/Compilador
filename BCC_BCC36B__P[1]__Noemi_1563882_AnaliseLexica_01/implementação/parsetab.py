
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVISAO MULT VIRGULA ATRIBUT MENOR MAIOR IGUAL MENOR_IGUAL MAIOR_IGUAL ABRE_PAR FECHA_PAR DOIS_PONTOS E_LOGICO OU_LOGICO SOMA SUB DIFERENCA ABRE_COL FECHA_COL NOTACAO_CIENTIFICA ID NEGACAO LEIA SENAO SE RETORNA INTEIRO FIM ENTAO REPITA ATE ESCREVA FLUTUANTE\n        programa : lista_declaracoes\n        \n        lista_declaracoes : lista_declaracoes declaracao\n                           | declaracao\n\t\t\t   | error\n        \n        declaracao : declaracao_variaveis\n                    | inicializacao_variaveis\n                    | declaracao_funcao\n        \n        declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis\n        \n        declaracao_variaveis : tipo DOIS_PONTOS error\n        \n        inicializacao_variaveis : atribuicao\n        \n        lista_variaveis : lista_variaveis VIRGULA var\n                        | var\n        \n        var : ID\n            | ID indice\n        \n        indice : indice ABRE_COL expressao FECHA_COL\n                | ABRE_COL expressao FECHA_COL\n        \n        indice : indice ABRE_COL error FECHA_COL\n                | ABRE_COL error FECHA_COL\n\t\t| error FECHA_COL\n\t\t| ABRE_COL error\n        \t| indice error FECHA_COL\n\t\t| indice ABRE_COL error\n\t\t\n        \n        tipo : INTEIRO\n\t     | FLUTUANTE\n        \n        declaracao_funcao : tipo cabecalho\n                          | cabecalho\n        \n        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo FIM\n        \n        cabecalho : ID ABRE_PAR lista_parametros FECHA_PAR corpo error\n        \n        lista_parametros : lista_parametros VIRGULA parametro\n                            | parametro\n                            | vazio\n        \n        parametro : tipo DOIS_PONTOS ID\n\t\t  | parametro ABRE_COL FECHA_COL\n        \n        corpo : corpo acao\n                | vazio\n        \n        acao : expressao\n             | declaracao_variaveis\n             | se\n             | repita\n             | leia\n             | escreva\n             | retorna\n        \n            se : SE expressao ENTAO corpo FIM\n               | SE expressao ENTAO corpo SENAO corpo FIM\n        \n            se : SE expressao error corpo FIM\n               | error SENAO corpo FIM\n        \n            repita : REPITA corpo ATE expressao\n        \n            repita : REPITA corpo error\n        \n            atribuicao : var ATRIBUT expressao\n        \n            leia : LEIA ABRE_PAR var FECHA_PAR\n        \n            escreva : ESCREVA ABRE_PAR expressao FECHA_PAR\n        \n            retorna : RETORNA ABRE_PAR expressao FECHA_PAR\n        \n            expressao : expressao_logica\n                        | atribuicao\n        \n            expressao_logica : expressao_simples\n                             | expressao_logica operador_logico expressao_simples\n        \n            expressao_simples : expressao_aditiva\n                                | expressao_simples operador_relacional expressao_aditiva\n        \n            expressao_aditiva : expressao_multiplicativa\n                                | expressao_aditiva operador_soma expressao_multiplicativa\n        \n           expressao_multiplicativa : expressao_unaria\n                           \t    | expressao_multiplicativa operador_multiplicacao expressao_unaria\n\n        \n            expressao_unaria : fator\n                             | operador_soma fator\n\t\t\t     | operador_negacao fator\n        \n            operador_relacional : MENOR\n                                | MAIOR\n                                | IGUAL\n\t\t\t\t| DIFERENCA\n                                | MENOR_IGUAL\n                                | MAIOR_IGUAL\n        \n            operador_soma : SOMA\n                          | SUB\n        \n            operador_negacao : NEGACAO\n        \n            operador_logico : E_LOGICO\n                            | OU_LOGICO\n        \n            operador_multiplicacao : MULT\n                                    | DIVISAO\n        \n            fator : ABRE_COL expressao FECHA_COL\n                  | var\n                  | chamada_funcao\n                  | numero\n        \n            numero : INTEIRO\n                   | FLUTUANTE\n\t\t   | NOTACAO_CIENTIFICA\n        \n            chamada_funcao : ID ABRE_PAR lista_argumentos FECHA_PAR\n        \n            lista_argumentos : lista_argumentos VIRGULA expressao\n                            | expressao\n                            | vazio\n        \n            vazio : \n        '
    
_lr_action_items = {'SE':([18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,53,54,55,56,57,61,62,63,65,71,81,84,85,87,88,89,93,94,97,98,100,101,102,103,105,107,108,111,112,113,116,117,119,120,121,124,126,130,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-49,-12,-9,-8,-13,-16,-64,-80,-18,-65,-90,-22,-21,-62,-60,-56,-79,-58,-35,115,-15,-17,-11,-86,-36,-39,-41,-83,-40,-90,-37,-34,-38,-84,-42,-90,115,115,-48,-90,-90,-46,-51,-47,115,115,-50,-52,-45,-43,-90,115,-44,]),'ABRE_PAR':([5,23,37,109,118,122,],[17,17,69,125,128,129,]),'ATE':([18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,53,54,55,56,57,61,62,63,65,71,84,85,87,88,89,93,94,97,100,101,102,103,105,107,108,111,112,113,116,117,119,120,121,126,133,139,140,141,144,145,146,147,150,],[-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-49,-12,-9,-8,-13,-16,-64,-80,-18,-65,-22,-21,-62,-60,-56,-79,-58,-35,-15,-17,-11,-86,-36,-39,-41,-83,-40,-90,-37,-34,-38,-84,-42,132,-48,-46,-51,-47,-50,-52,-45,-43,-44,]),'NOTACAO_CIENTIFICA':([16,18,19,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,81,84,85,87,88,89,93,94,97,98,100,101,102,103,104,105,107,108,111,112,113,115,116,117,119,120,121,124,125,126,129,130,132,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[44,-14,44,-19,-54,-82,-59,-74,-81,44,-57,-20,-63,-61,-53,-13,44,-80,44,-84,-55,-83,-85,-73,-72,44,-49,-12,-9,-8,-13,-78,-77,44,-16,-64,-80,44,-18,-76,-75,44,44,-65,-68,-69,44,-71,-70,-66,-67,-90,-22,-21,-62,-60,-56,-79,-58,-35,44,-15,-17,-11,-86,44,-36,-39,-41,-83,-40,-90,44,-37,-34,-38,-84,-42,-90,44,44,44,44,44,-48,-90,-90,-46,-51,-47,44,44,-50,-52,-45,-43,-90,44,-44,]),'MULT':([18,24,26,27,30,33,34,35,37,39,41,43,44,61,62,63,65,71,84,85,87,88,93,100,101,103,111,120,],[-14,-19,-82,59,-81,-20,-63,-61,-13,-80,-84,-83,-85,-16,-64,-80,-18,-65,-22,-21,-62,59,-79,-15,-17,-86,-83,-84,]),'MENOR':([18,24,26,27,30,32,33,34,35,37,39,41,42,43,44,61,62,63,65,71,84,85,87,88,89,93,94,100,101,103,111,120,],[-14,-19,-82,-59,-81,-57,-20,-63,-61,-13,-80,-84,77,-83,-85,-16,-64,-80,-18,-65,-22,-21,-62,-60,77,-79,-58,-15,-17,-86,-83,-84,]),'SENAO':([18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,53,54,55,56,57,61,62,63,65,71,84,85,87,88,89,93,94,97,100,101,102,103,105,106,107,108,111,112,116,117,119,120,121,133,135,138,139,140,141,143,144,145,146,147,150,],[-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-49,-12,-9,-8,-13,-16,-64,-80,-18,-65,-22,-21,-62,-60,-56,-79,-58,-35,-15,-17,-11,-86,-36,124,-39,-41,-83,-40,-37,-34,-38,-84,-42,124,-90,124,-46,-51,-47,148,-50,-52,-45,-43,-44,]),'NEGACAO':([16,18,19,24,25,26,27,30,32,33,34,35,36,37,38,39,41,42,43,44,45,46,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,81,84,85,87,88,89,93,94,97,98,100,101,102,103,104,105,107,108,111,112,113,115,116,117,119,120,121,124,125,126,129,130,132,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[29,-14,29,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,29,-80,-84,-55,-83,-85,-73,-72,29,-49,-12,-9,-8,-13,-78,-77,29,-16,-64,-80,29,-18,-76,-75,29,29,-65,-68,-69,29,-71,-70,-66,-67,-90,-22,-21,-62,-60,-56,-79,-58,-35,29,-15,-17,-11,-86,29,-36,-39,-41,-83,-40,-90,29,-37,-34,-38,-84,-42,-90,29,29,29,29,29,-48,-90,-90,-46,-51,-47,29,29,-50,-52,-45,-43,-90,29,-44,]),'DIVISAO':([18,24,26,27,30,33,34,35,37,39,41,43,44,61,62,63,65,71,84,85,87,88,93,100,101,103,111,120,],[-14,-19,-82,58,-81,-20,-63,-61,-13,-80,-84,-83,-85,-16,-64,-80,-18,-65,-22,-21,-62,58,-79,-15,-17,-86,-83,-84,]),'FECHA_COL':([15,18,24,25,26,27,28,30,32,33,34,35,36,37,39,41,42,43,44,52,53,61,62,63,65,70,71,79,83,84,85,87,88,89,93,94,100,101,103,],[24,-14,-19,-54,-82,-59,61,-81,-57,65,-63,-61,-53,-13,-80,-84,-55,-83,-85,85,-49,-16,-64,-80,-18,93,-65,95,100,101,-21,-62,-60,-56,-79,-58,-15,-17,-86,]),'LEIA':([18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,53,54,55,56,57,61,62,63,65,71,81,84,85,87,88,89,93,94,97,98,100,101,102,103,105,107,108,111,112,113,116,117,119,120,121,124,126,130,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-49,-12,-9,-8,-13,-16,-64,-80,-18,-65,-90,-22,-21,-62,-60,-56,-79,-58,-35,118,-15,-17,-11,-86,-36,-39,-41,-83,-40,-90,-37,-34,-38,-84,-42,-90,118,118,-48,-90,-90,-46,-51,-47,118,118,-50,-52,-45,-43,-90,118,-44,]),'IGUAL':([18,24,26,27,30,32,33,34,35,37,39,41,42,43,44,61,62,63,65,71,84,85,87,88,89,93,94,100,101,103,111,120,],[-14,-19,-82,-59,-81,-57,-20,-63,-61,-13,-80,-84,72,-83,-85,-16,-64,-80,-18,-65,-22,-21,-62,-60,72,-79,-58,-15,-17,-86,-83,-84,]),'error':([0,5,16,18,21,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,51,53,54,55,56,57,61,62,63,65,71,81,84,85,87,88,89,93,94,97,98,100,101,102,103,105,107,108,111,112,113,116,117,119,120,121,124,126,127,130,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[4,15,33,52,55,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,15,-80,-84,-55,-83,-85,84,-49,-12,-9,-8,15,-16,-64,-80,-18,-65,-90,-22,-21,-62,-60,-56,-79,-58,-35,106,-15,-17,-11,-86,-36,-39,-41,-83,-40,-90,-37,-34,-38,-84,-42,-90,133,134,138,-48,-90,-90,-46,-51,-47,138,138,-50,-52,-45,-43,-90,138,-44,]),'OU_LOGICO':([18,24,26,27,30,32,33,34,35,36,37,39,41,42,43,44,61,62,63,65,71,84,85,87,88,89,93,94,100,101,103,111,120,],[-14,-19,-82,-59,-81,-57,-20,-63,-61,66,-13,-80,-84,-55,-83,-85,-16,-64,-80,-18,-65,-22,-21,-62,-60,-56,-79,-58,-15,-17,-86,-83,-84,]),'ENTAO':([18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,53,61,62,63,65,71,84,85,87,88,89,93,94,100,101,103,127,],[-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-49,-16,-64,-80,-18,-65,-22,-21,-62,-60,-56,-79,-58,-15,-17,-86,135,]),'FECHA_PAR':([17,18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,47,48,49,53,57,61,62,63,65,69,71,84,85,87,88,89,90,91,92,93,94,95,96,99,100,101,103,123,131,136,137,],[-90,-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-31,-30,81,-49,-13,-16,-64,-80,-18,-90,-65,-22,-21,-62,-60,-56,-89,-88,103,-79,-58,-33,-29,-32,-15,-17,-86,-87,140,144,145,]),'ID':([0,1,2,3,4,7,9,10,11,12,13,14,16,18,19,20,21,22,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,81,82,84,85,86,87,88,89,93,94,97,98,100,101,102,103,104,105,106,107,108,110,111,112,113,115,116,117,119,120,121,124,125,126,128,129,130,132,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[5,-10,-5,-3,-4,-24,5,-23,-6,-7,-26,23,37,-14,37,-2,57,-25,-19,-54,-82,-59,-74,-81,37,-57,-20,-63,-61,-53,-13,37,-80,37,-84,-55,-83,-85,-73,-72,37,-49,-12,-9,-8,-13,-78,-77,37,-16,-64,-80,37,-18,-76,-75,37,37,-65,-68,-69,37,-71,-70,-66,-67,-90,99,-22,-21,57,-62,-60,-56,-79,-58,-35,37,-15,-17,-11,-86,37,-36,-28,-39,-41,-27,-83,-40,-90,37,-37,-34,-38,-84,-42,-90,37,37,57,37,37,37,-48,-90,-90,-46,-51,-47,37,37,-50,-52,-45,-43,-90,37,-44,]),'ESCREVA':([18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,53,54,55,56,57,61,62,63,65,71,81,84,85,87,88,89,93,94,97,98,100,101,102,103,105,107,108,111,112,113,116,117,119,120,121,124,126,130,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-49,-12,-9,-8,-13,-16,-64,-80,-18,-65,-90,-22,-21,-62,-60,-56,-79,-58,-35,109,-15,-17,-11,-86,-36,-39,-41,-83,-40,-90,-37,-34,-38,-84,-42,-90,109,109,-48,-90,-90,-46,-51,-47,109,109,-50,-52,-45,-43,-90,109,-44,]),'ABRE_COL':([5,16,18,19,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,81,84,85,87,88,89,93,94,95,96,97,98,99,100,101,102,103,104,105,107,108,111,112,113,115,116,117,119,120,121,124,125,126,129,130,132,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[16,38,51,38,-19,-54,-82,-59,-74,-81,38,-57,-20,-63,-61,-53,16,38,-80,38,-84,-55,-83,-85,-73,-72,79,38,-49,-12,-9,-8,16,-78,-77,38,-16,-64,-80,38,-18,-76,-75,38,38,-65,-68,-69,38,-71,-70,-66,-67,-90,-22,-21,-62,-60,-56,-79,-58,-33,79,-35,38,-32,-15,-17,-11,-86,38,-36,-39,-41,-83,-40,-90,38,-37,-34,-38,-84,-42,-90,38,38,38,38,38,-48,-90,-90,-46,-51,-47,38,38,-50,-52,-45,-43,-90,38,-44,]),'E_LOGICO':([18,24,26,27,30,32,33,34,35,36,37,39,41,42,43,44,61,62,63,65,71,84,85,87,88,89,93,94,100,101,103,111,120,],[-14,-19,-82,-59,-81,-57,-20,-63,-61,67,-13,-80,-84,-55,-83,-85,-16,-64,-80,-18,-65,-22,-21,-62,-60,-56,-79,-58,-15,-17,-86,-83,-84,]),'DOIS_PONTOS':([7,10,14,50,111,114,120,],[-24,-23,21,82,-23,21,-24,]),'FLUTUANTE':([0,1,2,3,4,9,11,12,13,16,17,18,19,20,22,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,80,81,84,85,87,88,89,93,94,97,98,100,101,102,103,104,105,106,107,108,110,111,112,113,115,116,117,119,120,121,124,125,126,129,130,132,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[7,-10,-5,-3,-4,7,-6,-7,-26,41,7,-14,41,-2,-25,-19,-54,-82,-59,-74,-81,41,-57,-20,-63,-61,-53,-13,41,-80,41,-84,-55,-83,-85,-73,-72,41,-49,-12,-9,-8,-13,-78,-77,41,-16,-64,-80,41,-18,-76,-75,41,41,-65,-68,-69,41,-71,-70,-66,-67,7,-90,-22,-21,-62,-60,-56,-79,-58,-35,120,-15,-17,-11,-86,41,-36,-28,-39,-41,-27,-83,-40,-90,41,-37,-34,-38,-84,-42,-90,41,120,41,120,41,-48,-90,-90,-46,-51,-47,120,120,-50,-52,-45,-43,-90,120,-44,]),'FIM':([18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,53,54,55,56,57,61,62,63,65,71,81,84,85,87,88,89,93,94,97,98,100,101,102,103,105,107,108,111,112,116,117,119,120,121,124,130,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-49,-12,-9,-8,-13,-16,-64,-80,-18,-65,-90,-22,-21,-62,-60,-56,-79,-58,-35,110,-15,-17,-11,-86,-36,-39,-41,-83,-40,-37,-34,-38,-84,-42,-90,139,-48,-90,-90,-46,-51,-47,146,147,-50,-52,-45,-43,-90,150,-44,]),'RETORNA':([18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,53,54,55,56,57,61,62,63,65,71,81,84,85,87,88,89,93,94,97,98,100,101,102,103,105,107,108,111,112,113,116,117,119,120,121,124,126,130,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-49,-12,-9,-8,-13,-16,-64,-80,-18,-65,-90,-22,-21,-62,-60,-56,-79,-58,-35,122,-15,-17,-11,-86,-36,-39,-41,-83,-40,-90,-37,-34,-38,-84,-42,-90,122,122,-48,-90,-90,-46,-51,-47,122,122,-50,-52,-45,-43,-90,122,-44,]),'INTEIRO':([0,1,2,3,4,9,11,12,13,16,17,18,19,20,22,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,80,81,84,85,87,88,89,93,94,97,98,100,101,102,103,104,105,106,107,108,110,111,112,113,115,116,117,119,120,121,124,125,126,129,130,132,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[10,-10,-5,-3,-4,10,-6,-7,-26,43,10,-14,43,-2,-25,-19,-54,-82,-59,-74,-81,43,-57,-20,-63,-61,-53,-13,43,-80,43,-84,-55,-83,-85,-73,-72,43,-49,-12,-9,-8,-13,-78,-77,43,-16,-64,-80,43,-18,-76,-75,43,43,-65,-68,-69,43,-71,-70,-66,-67,10,-90,-22,-21,-62,-60,-56,-79,-58,-35,111,-15,-17,-11,-86,43,-36,-28,-39,-41,-27,-83,-40,-90,43,-37,-34,-38,-84,-42,-90,43,111,43,111,43,-48,-90,-90,-46,-51,-47,111,111,-50,-52,-45,-43,-90,111,-44,]),'MAIOR':([18,24,26,27,30,32,33,34,35,37,39,41,42,43,44,61,62,63,65,71,84,85,87,88,89,93,94,100,101,103,111,120,],[-14,-19,-82,-59,-81,-57,-20,-63,-61,-13,-80,-84,78,-83,-85,-16,-64,-80,-18,-65,-22,-21,-62,-60,78,-79,-58,-15,-17,-86,-83,-84,]),'MENOR_IGUAL':([18,24,26,27,30,32,33,34,35,37,39,41,42,43,44,61,62,63,65,71,84,85,87,88,89,93,94,100,101,103,111,120,],[-14,-19,-82,-59,-81,-57,-20,-63,-61,-13,-80,-84,76,-83,-85,-16,-64,-80,-18,-65,-22,-21,-62,-60,76,-79,-58,-15,-17,-86,-83,-84,]),'ATRIBUT':([5,6,18,24,33,37,39,61,65,84,85,100,101,],[-13,19,-14,-19,-20,-13,19,-16,-18,-22,-21,-15,-17,]),'DIFERENCA':([18,24,26,27,30,32,33,34,35,37,39,41,42,43,44,61,62,63,65,71,84,85,87,88,89,93,94,100,101,103,111,120,],[-14,-19,-82,-59,-81,-57,-20,-63,-61,-13,-80,-84,73,-83,-85,-16,-64,-80,-18,-65,-22,-21,-62,-60,73,-79,-58,-15,-17,-86,-83,-84,]),'MAIOR_IGUAL':([18,24,26,27,30,32,33,34,35,37,39,41,42,43,44,61,62,63,65,71,84,85,87,88,89,93,94,100,101,103,111,120,],[-14,-19,-82,-59,-81,-57,-20,-63,-61,-13,-80,-84,75,-83,-85,-16,-64,-80,-18,-65,-22,-21,-62,-60,75,-79,-58,-15,-17,-86,-83,-84,]),'SUB':([16,18,19,24,25,26,27,30,32,33,34,35,36,37,38,39,41,42,43,44,45,46,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,81,84,85,87,88,89,93,94,97,98,100,101,102,103,104,105,107,108,111,112,113,115,116,117,119,120,121,124,125,126,129,130,132,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[45,-14,45,-19,-54,-82,-59,-81,45,-20,-63,-61,-53,-13,45,-80,-84,-55,-83,-85,-73,-72,45,-49,-12,-9,-8,-13,-78,-77,45,-16,-64,-80,45,-18,-76,-75,45,45,-65,-68,-69,45,-71,-70,-66,-67,-90,-22,-21,-62,-60,-56,-79,45,-35,45,-15,-17,-11,-86,45,-36,-39,-41,-83,-40,-90,45,-37,-34,-38,-84,-42,-90,45,45,45,45,45,-48,-90,-90,-46,-51,-47,45,45,-50,-52,-45,-43,-90,45,-44,]),'REPITA':([18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,53,54,55,56,57,61,62,63,65,71,81,84,85,87,88,89,93,94,97,98,100,101,102,103,105,107,108,111,112,113,116,117,119,120,121,124,126,130,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-49,-12,-9,-8,-13,-16,-64,-80,-18,-65,-90,-22,-21,-62,-60,-56,-79,-58,-35,113,-15,-17,-11,-86,-36,-39,-41,-83,-40,-90,-37,-34,-38,-84,-42,-90,113,113,-48,-90,-90,-46,-51,-47,113,113,-50,-52,-45,-43,-90,113,-44,]),'$end':([1,2,3,4,8,9,11,12,13,18,20,22,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,53,54,55,56,57,61,62,63,65,71,84,85,87,88,89,93,94,100,101,102,103,106,110,],[-10,-5,-3,-4,0,-1,-6,-7,-26,-14,-2,-25,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-49,-12,-9,-8,-13,-16,-64,-80,-18,-65,-22,-21,-62,-60,-56,-79,-58,-15,-17,-11,-86,-28,-27,]),'SOMA':([16,18,19,24,25,26,27,30,32,33,34,35,36,37,38,39,41,42,43,44,45,46,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,71,72,73,74,75,76,77,78,81,84,85,87,88,89,93,94,97,98,100,101,102,103,104,105,107,108,111,112,113,115,116,117,119,120,121,124,125,126,129,130,132,133,134,135,139,140,141,142,143,144,145,146,147,148,149,150,],[46,-14,46,-19,-54,-82,-59,-81,46,-20,-63,-61,-53,-13,46,-80,-84,-55,-83,-85,-73,-72,46,-49,-12,-9,-8,-13,-78,-77,46,-16,-64,-80,46,-18,-76,-75,46,46,-65,-68,-69,46,-71,-70,-66,-67,-90,-22,-21,-62,-60,-56,-79,46,-35,46,-15,-17,-11,-86,46,-36,-39,-41,-83,-40,-90,46,-37,-34,-38,-84,-42,-90,46,46,46,46,46,-48,-90,-90,-46,-51,-47,46,46,-50,-52,-45,-43,-90,46,-44,]),'VIRGULA':([17,18,24,25,26,27,30,32,33,34,35,36,37,39,41,42,43,44,47,48,49,53,54,56,57,61,62,63,65,69,71,84,85,87,88,89,90,91,92,93,94,95,96,99,100,101,102,103,123,],[-90,-14,-19,-54,-82,-59,-81,-57,-20,-63,-61,-53,-13,-80,-84,-55,-83,-85,-31,-30,80,-49,-12,86,-13,-16,-64,-80,-18,-90,-65,-22,-21,-62,-60,-56,-89,-88,104,-79,-58,-33,-29,-32,-15,-17,-11,-86,-87,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'atribuicao':([0,9,16,19,38,51,69,98,104,115,125,126,129,130,132,142,143,149,],[1,1,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'numero':([16,19,31,38,40,51,60,64,68,69,74,98,104,115,125,126,129,130,132,142,143,149,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'declaracao_variaveis':([0,9,98,126,130,142,143,149,],[2,2,116,116,116,116,116,116,]),'vazio':([17,69,81,113,124,134,135,148,],[47,90,97,97,97,97,97,97,]),'corpo':([81,113,124,134,135,148,],[98,126,130,142,143,149,]),'expressao_multiplicativa':([16,19,38,51,64,68,69,74,98,104,115,125,126,129,130,132,142,143,149,],[27,27,27,27,88,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'operador_multiplicacao':([27,88,],[60,60,]),'expressao':([16,19,38,51,69,98,104,115,125,126,129,130,132,142,143,149,],[28,53,70,83,91,105,123,127,131,105,137,105,141,105,105,105,]),'lista_argumentos':([69,],[92,]),'operador_logico':([36,],[68,]),'chamada_funcao':([16,19,31,38,40,51,60,64,68,69,74,98,104,115,125,126,129,130,132,142,143,149,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'operador_soma':([16,19,32,38,51,60,64,68,69,74,94,98,104,115,125,126,129,130,132,142,143,149,],[31,31,64,31,31,31,31,31,31,31,64,31,31,31,31,31,31,31,31,31,31,31,]),'lista_parametros':([17,],[49,]),'declaracao':([0,9,],[3,20,]),'fator':([16,19,31,38,40,51,60,64,68,69,74,98,104,115,125,126,129,130,132,142,143,149,],[34,34,62,34,71,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'expressao_unaria':([16,19,38,51,60,64,68,69,74,98,104,115,125,126,129,130,132,142,143,149,],[35,35,35,35,87,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'parametro':([17,80,],[48,96,]),'escreva':([98,126,130,142,143,149,],[108,108,108,108,108,108,]),'expressao_logica':([16,19,38,51,69,98,104,115,125,126,129,130,132,142,143,149,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'retorna':([98,126,130,142,143,149,],[121,121,121,121,121,121,]),'repita':([98,126,130,142,143,149,],[107,107,107,107,107,107,]),'se':([98,126,130,142,143,149,],[119,119,119,119,119,119,]),'var':([0,9,16,19,21,31,38,40,51,60,64,68,69,74,86,98,104,115,125,126,128,129,130,132,142,143,149,],[6,6,39,39,54,63,39,63,39,63,63,63,39,63,102,39,39,39,39,39,136,39,39,39,39,39,39,]),'operador_negacao':([16,19,38,51,60,64,68,69,74,98,104,115,125,126,129,130,132,142,143,149,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'acao':([98,126,130,142,143,149,],[117,117,117,117,117,117,]),'programa':([0,],[8,]),'lista_declaracoes':([0,],[9,]),'inicializacao_variaveis':([0,9,],[11,11,]),'leia':([98,126,130,142,143,149,],[112,112,112,112,112,112,]),'declaracao_funcao':([0,9,],[12,12,]),'operador_relacional':([42,89,],[74,74,]),'cabecalho':([0,9,14,],[13,13,22,]),'expressao_aditiva':([16,19,38,51,68,69,74,98,104,115,125,126,129,130,132,142,143,149,],[32,32,32,32,32,32,94,32,32,32,32,32,32,32,32,32,32,32,]),'lista_variaveis':([21,],[56,]),'expressao_simples':([16,19,38,51,68,69,98,104,115,125,126,129,130,132,142,143,149,],[42,42,42,42,89,42,42,42,42,42,42,42,42,42,42,42,42,]),'tipo':([0,9,17,80,98,126,130,142,143,149,],[14,14,50,50,114,114,114,114,114,114,]),'indice':([5,37,57,],[18,18,18,]),}

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
