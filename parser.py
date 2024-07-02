import ply.yacc as yacc
from lexer import tokens

# Define precedence and associativity of operators
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# Dictionary to hold variables
variables = {}

# Define the grammar rules
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

# Grammar rules and actions
def p_statement_assign(p):
    'statement : ID ASSIGN expression SEMI'
    variables[p[1]] = p[3]        

def p_statement_expr(p):
    'statement : expression SEMI'
    print(p[1])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print(f"Undefined variable '{p[1]}'")
        p[0] = 0

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the parser
parser = yacc.yacc()

# Test the parser
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)

