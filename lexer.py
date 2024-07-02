import ply.lex as lex
import  tokens

tokens = tokens.token_list

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_ASSIGN = r'='

# Keyword recognition
reserved = {
    'מש': 'INT',
    'תו': 'CHAR',
    'ממ': 'DOUBLE',
    'דגל': 'BOOL',
    'אם': 'IF',
    'אחרת': 'ELSE',
    'אחרת אם': 'ELSEIF',
    'עבור': 'FOR',
    'כל_עוד': 'WHILE',
    'הפסק': 'BREAK',
    'המשך': 'CONTINUE',
    'בדוק': 'SWITCH',
    'כאשר': 'CASE',
    'אף_אחד': 'DEFAULT',
    'כלום': 'VOID',
    'החזר': 'RETURN',
}

def t_ID(t):
    r'[א-ת][א-ת0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words (keywords)
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer
# data = '3 + 4 * (10 - 5) / 2'
# data = 'מש מטבעות = 5;'
data = 'אם(שם == "דניאללל"{}'
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

