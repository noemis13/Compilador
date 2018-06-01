import ply.lex as lex
import io

class Lexica:
	def __init__(self):
	    self.lexer = lex.lex(debug=False, module=self)

	# Palavras reservadas
	reservadas = {
	    'se':'SE',
	    'então':'ENTAO',
	    'senão':'SENAO',
	    'fim':'FIM',
	    'flutuante' : 'FLUTUANTE',
	    'inteiro' : 'INTEIRO',
	    #'vazio':'VAZIO',
	    'até':'ATE',
	    'leia':'LEIA',
	    'repita':'REPITA',
	    'escreva':'ESCREVA',
	    'retorna':'RETORNA'
	    #'principal':'PRINCIPAL',
	    
	    }

	# Lista de tokens
	tokens = ['DIVISAO', 'MULT', 'VIRGULA', 'ATRIBUT', 'MENOR', 'MAIOR', 'IGUAL', 'MENOR_IGUAL','MAIOR_IGUAL', 'ABRE_PAR', 'FECHA_PAR', 'DOIS_PONTOS', 'SOMA', 'SUB',   'DIFERENCA', 'ABRE_COL', 'FECHA_COL', 'NOTACAO_CIENTIFICA', 'ID', 'E_LOGICO', 'OU_LOGICO','NEGACAO'] + list(reservadas.values())

	# Regras de expressões regulares
	t_SOMA = r'\+' 
	t_SUB = r'-'
	t_MULT= r'\*'
	t_DIVISAO = r'\/'
	t_IGUAL = r'\='
	t_DIFERENCA = r'\<\>'
	t_VIRGULA = r'\,'
	t_ATRIBUT = r'\:=+'
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


	def t_ID(self, t):
	  r'[a-zA-Zà-úÀ-Ú][_0-9a-zà-úA-ZÀ-Ú]*'
	  t.type  = self.reservadas.get(t.value, 'ID')
	  return t

	def t_NOTACAO_CIENTIFICA(self, t):
	  r'[0-9]+(\.[0-9]+)*(e|E)+(\+|\-)?[0-9]+(\.[0-9])*'
	  t.type = "NOTACAO_CIENTIFICA"
	  return t


	def t_FLUTUANTE(self, t):
	  r'[0-9]+(\.[0-9]+)(e(\+|\-)?(\d+))?'
	  t.value = float(t.value)
	  return t

	def t_INTEIRO(self, t):
	  r'[0-9]+'
	  #t.type = reservadas.get(t.value, 'INTEIRO')
	  t.value = int(t.value)
	  return t 

	  
	def t_COMENTARIO(self, t):
	  r'{[^\{^\}]*}'
	  #t.type  = reservadas.get(t.value, 'COMENTARIO')
	  for x in range(1, len(t.value)):
	  	if t.value[x] == "\n":
	  		t.lexer.lineno += 1
	  pass

	  #return t

	def t_NOVA_LINHA(self, t):
	  r'\n+'
	  t.lexer.lineno += len(t.value)
	  #t.type  = "NOVA_LINHA"
	  #return t
	 
	  
	# Ignora espaços
	t_ignore  = ' \t'


	# Error handling rule
	def t_error(self, t):
	    print ("Erro '%s', linha %d" %(t.value[0], t.lineno))
	    print (type(t.value))
	    #t.lexer.skip(1)
	    exit(0)


	# Salvar os tokens
	def saida(self, code):
	    out = io.open("saida.txt", mode="w", encoding="utf-8")
	    lex.input(code)
	    while True:
	    	tok = lex.token()
	    	if not tok:
	    		break
	    	print(tok)
	    	out.write(str(tok) + "\n")
	    out.close()

if __name__ == '__main__':
  import sys
  code = io.open(sys.argv[1], mode="r", encoding="utf-8")
  lexica = Lexica()
  lexica.saida(code.read())
