import ply.lex as lex
from ply.lex import TOKEN

# Dictionary of reserved words
reserved = {
    'continue': 'CONTINUE',
    'break' : 'BREAK',
    'default': 'DEFAULT',
    'loop': 'LOOP',
    'import': 'IMPORT',
    'return': 'RETURN',
    'free': 'FREE',
    'null': 'NULL'
}

# List of token names
tokens = ['RIGHT_ASSIGN', 'LEFT_ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN', 'REM',
    'MUL_ASSIGN', 'DIV_ASSIGN', 'EXP_ASSIGN', 'MOD_ASSIGN', 'AND_ASSIGN', 'LEN',
    'XOR_ASSIGN', 'OR_ASSIGN', 'RIGHT_OP', 'LEFT_OP', 'AND_OP', 'OR_OP',
    'LE_OP', 'GE_OP', 'EQ_OP', 'NE_OP', 'SEMICOLON', 'L_BRACE', 'R_BRACE',
    'COMMA', 'COLON', 'ASSIGN', 'L_PAREN', 'R_PAREN', 'L_BRACKET', 'R_BRACKET',
    'DOT', 'AND', 'NOT', 'NOT_OP', 'EXP', 'ADD', 'SUB', 'MUL', 'DIV', 'MOD',
    'MINOR', 'MAJOR', 'XOR', 'OR', 'QUESTION', 'ID', 'INT', 'FLOAT', 'STR'] + \
    list(reserved.values())

# Regular expressions rulers
t_RIGHT_ASSIGN = r'>>='
t_LEFT_ASSIGN = r'<<='
t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN = r'-='
t_MUL_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_EXP_ASSIGN = r'\*\*='
t_MOD_ASSIGN = r'%='
t_AND_ASSIGN = r'&='
t_XOR_ASSIGN = r'\^='
t_OR_ASSIGN = r'\|='
t_RIGHT_OP = r'>>'
t_LEFT_OP = r'<<'
t_AND_OP = r'&&'
t_OR_OP = r'\|\|'
t_LE_OP = r'<='
t_GE_OP = r'>='
t_EQ_OP = r'=='
t_NE_OP = r'!='
t_NOT_OP = r'~'
t_NOT = r'\!'
t_SEMICOLON = r';'
t_L_BRACE = r'\{'
t_R_BRACE = r'\}'
t_COMMA = r','
t_COLON = r':'
t_ASSIGN = r'='
t_L_PAREN = r'\('
t_R_PAREN = r'\)'
t_L_BRACKET = r'\['
t_R_BRACKET = r'\]'
t_DOT = r'\.'
t_AND = r'&'
t_EXP = r'\*\*'
t_ADD = r'\+'
t_REM = r'--'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_MINOR = r'<'
t_MAJOR = r'>'
t_XOR = r'\^'
t_OR = r'\|'
t_QUESTION = r'\?'
t_LEN = r'\#'

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_INT = r'\d+'
t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))'
t_STR = r'\"([^\\\n]|(\\.))*?\"'

# Only one line comments
def t_COMMENT(t):
    r'//.*'

# New lines will be counted
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Contains ignore characters as spaces and tabs
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print 'Illegal character: %s' % t.value[0]
    t.lexer.skip(1)

lexer = lex.lex(optimize=0)

if __name__ == '__main__':
    import sys
    code = open(sys.argv[1])
    lex.input(code.read())
    while True:
        tok = lex.token()
        if not tok:
            break
        print tok