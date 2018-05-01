import ply.lex as lex
import io
from ply.lex import TOKEN

class Lexica:
	# Palavras reservadas
	reservadas = {
	    'se':'SE',
	    'então':'ENTAO',
	    'senão':'SENAO',
	    'fim':'FIM',
	    'repita':'REPITA',
	    'vazio':'VAZIO',
	    'até':'ATE',
	    'leia':'LEIA',
	    'escreva':'ESCREVA',
	    'retorna':'RETORNA',
	    'principal':'PRINCIPAL',
	    'inteiro' : 'INTEIRO',
	    'flutuante' : 'FLUTUANTE'
	    }

	# Lista de tokens
	tokens = ['SOMA', 'SUB', 'MULT', 'DIVISAO', 'IGUAL', 'VIRGULA', 'ATRIBUICAO', 'MENOR', 'MAIOR', 'MENOR_IGUAL','MAIOR_IGUAL', 'ABRE_PAR', 'FECHA_PAR', 'DOIS_PONTOS', 'ABRE_COL', 'FECHA_COL', 'E_LOGICO', 'OU_LOGICO', 'NEGACAO', 'ID','NOVA_LINHA', 'COMENTARIO', 'NOTACAO_CIENTIFICA'] + \
	    list(reservadas.values())

	# Regras de expressões regulares
	t_SOMA = r'\+' 
	t_SUB = r'-'
	t_MULT= r'\*'
	t_DIVISAO = r'\/'
	t_IGUAL = r'\='
	t_VIRGULA = r'\,'
	t_ATRIBUICAO = r'\:=+'
	t_MENOR = r'\<'
	t_MAIOR = r'\>'
	t_MENOR_IGUAL = r'<='
	t_MAIOR_IGUAL = r'>='
	t_ABRE_PAR = r'\('
	t_FECHA_PAR = r'\)'
	t_ABRE_COL = r'\[' 
	t_FECHA_COL = r'\]'
	t_DOIS_PONTOS = r':'
	t_E_LOGICO = r'&&' 
	t_OU_LOGICO = r'\|\|'
	t_NEGACAO = r'!'


	def t_ID(t):
	  r'[a-zA-Zà-úÀ-Ú][_0-9a-zà-úA-ZÀ-Ú]*'
	  t.type  = reservadas.get(t.value, 'ID')
	  return t

	def t_NOTACAO_CIENTIFICA(t):
	  r'[0-9]+(\.[0-9]+)*(e|E)+(\+|\-)?[0-9]+(\.[0-9])*'
	  t.type = "NOTACAO_CIENTIFICA"
	  return t


	def t_FLUTUANTE(t):
	  r'[0-9]+(\.[0-9]+)(e(\+|\-)?(\d+))?'
	  t.type = reservadas.get(t.value, 'FLUTUANTE')
	  return t

	def t_INTEIRO(t):
	  r'[0-9]+'
	  t.type = reservadas.get(t.value, 'INTEIRO')
	  return t 

	  
	def t_COMENTARIO(t):
	  r'{[^\{^\}]*}'
	  t.type  = reservadas.get(t.value, 'COMENTARIO')
	  for x in range(1, len(t.value)):
	  	if t.value[x] == "\n":
			t.lexer.lineno += 1
	  pass

	  #return t

	def t_NOVA_LINHA(t):
	  r'\n+'
	  t.lexer.lineno += len(t.value)
	  t.type  = "NOVA_LINHA"
	  return t
	 
	  
	# Ignora espaços
	t_ignore  = ' \t'


	# Error handling rule
	def t_error(t):
	    print ("Erro '%s', linha %d" %(t.value[0], t.lineno))
	    print (type(t.value))
	    t.lexer.skip(1)
	    #exit(0)

lexica = lex.lex()
if __name__ == '__main__':
  import sys
  code = io.open(sys.argv[1], mode="r", encoding="utf-8")
  out = io.open("saida.txt", mode="w", encoding="utf-8")
  lexica.input(code.read())
  while True:
     tok = lexica.token()
     if not tok:
       break
     print(tok)
     out.write(str(tok)+ "\n")
  out.close()
