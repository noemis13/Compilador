import ply.lex as lex
from ply.lex import TOKEN


# Palavras reservadas
reservadas = {
    'se':'SE',
    'então':'ENTÃO',
    'senão':'SENÃO',
    'fim':'FIM',
    'repita':'REPITA',
    'vazio':'VAZIO',
    'até':'ATÉ',
    'leia':'LEIA',
    'escreva':'ESCREVA',
    'retorna':'RETORNA',
    'principal':'PRINCIPAL',
    'inteiro' : 'INTEIRO',
    'flutuante' : 'FLUTUANTE'
    }

# Lista de tokens
tokens = ['SOMA', 'SUB', 'MULT', 'DIVISÃO', 'IGUAL', 'VÍRGULA', 'ATRIBUIÇÃO', 'MENOR', 'MAIOR', 'MENOR_IGUAL', 
	  'MAIOR_IGUAL', 'ABRE_PAR', 'FECHA_PAR', 'DOIS_PONTOS', 'ID','NOVA_LINHA', 'COMENTÁRIO'] + \
    list(reservadas.values())
