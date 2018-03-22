import ply.lex as lex

# Palavras reservadas
reservadas = {
    'se': 'SE',
    'então': 'ENTÃO',
    'senão': 'SENÃO',
    'fim': 'FIM',
    'repita': 'REPITA',
    'vazio': 'VAZIO',
    'até': 'ATÉ',
    'leia': 'LEIA',
    'escreva': 'ESCREVA',
    'retorna': 'RETORNA',
    'principal': 'PRINCIPAL',
    'inteiro': 'INTEIRO',
    'flutuante': 'FLUTUANTE'
}

# Lista de tokens
tokens = ['SOMA', 'SUB', 'MULT', 'DIVISÃO', 'IGUAL', 'VÍRGULA', 'ATRIBUIÇÃO', 'MENOR', 'MAIOR', 'MENOR_IGUAL',
          'MAIOR_IGUAL', 'ABRE_PAR', 'FECHA_PAR', 'DOIS_PONTOS', 'ABRE_COL', 'FECHA_COL', 'E_LOGICO', 'OU_LOGICO',
          'NEGAÇÃO' 'ID', 'NOVA_LINHA', 'COMENTÁRIO'] + \
         list(reservadas.values())

# Regras de expressões regulares
t_SOMA = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIVISÃO = r'\/'
t_IGUAL = r'\='
t_VÍRGULA = r'\,'
t_ATRIBUIÇÃO = r'\:='
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
t_OU_LOGICO = r'\|'
t_NEGAÇÃO = r'\!'


def t_ID(t):
    r'[a-zA-Zà-úÀ-Ú][0-9a-zà-úA-ZÀ-Ú]*'
    t.type = reservadas.get(t.value, 'ID')
    return t


def t_NOVA_LINHA(t):
    r'(\n)+'
    t.type = reservadas.get(t.value, 'NOVA_LINHA')
    return t


def t_COMENTÁRIO(t):
    r'[\{]+[a-zA-Zà-úÀ-Ú]*[0-9a-zà-úA-ZÀ-Ú\s\n]*[\}]+'
    t.type = reservadas.get(t.value, 'COMENTÁRIO')
    return t


# Ignora espaços
t_ignore = ' \t'


# Regras para erros
def t_error(t):
    print ("Erro '%s', linha %d" % (t.value[0], t.lineno))
    print (type(t.value))
    t.lexer.skip(1)
    # exit(0)


# Build the lexer
lexer = lex.lex()

if __name__ == '__main__':
    import sys

    code = open(sys.argv[1])
    lex.input(code.read())
    while True:
        tok = lex.token()
        if not tok:
            break
print (tok)
