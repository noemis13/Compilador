from ast import AST
from ply import yacc
from lexer import tokens

def p_tas_definition_1(t):
    'task_definition : task_signature task_definition'
    t[0] = AST('task-def', [t[1], t[2]])

def p_tas_definition_2(t):
    'task_definition : task_signature'
    t[0] = AST('task-def', [t[1]])

def p_task_signature(t):
    ' task_signature : ID L_PAREN parameter_list R_PAREN statement '
    t[0] = AST('task-assign', [t[1], t[3], t[5]])

def p_parameter_list_1(t):
    ' parameter_list : ID COMMA parameter_list '
    t[0] = AST('paramm', [t[1], t[3]])

def p_parameter_list_2(t):
    ' parameter_list : ID '
    t[0] = AST('paramm', [t[1]])

def p_parameter_list_3(t):
    ' parameter_list : empty '

def p_loop_statement_1(t):
    ' loop_statement : LOOP expression statement '
    t[0] = AST('loop-stmt', [t[2], t[3]])

def p_loop_statement_2(t):
    ' loop_statement : LOOP ID COMMA expression COMMA value statement '
    t[0] = AST('loop-stmt', [t[2], t[4], t[6], t[7]])

def p_loop_statement_3(t):
    ' loop_statement : LOOP ID COMMA expression statement '
    t[0] = AST('loop-stmt', [t[2], t[4], t[5]])

def p_condition_statement_1(t):
    ' condition_statement : expression QUESTION statement more_condition '
    t[0] = AST('if-stmt', [t[1], t[3], t[4]])

def p_more_condition_1(t):
    ' more_condition : OR binary_expression QUESTION statement more_condition'
    t[0] = AST('elseif-stmt', [t[2], t[4], t[5]])

def p_more_condition_2(t):
    ' more_condition : COLON statement '
    t[0] = AST('else-stmt', t[2])

def p_more_condition_3(t):
    ' more_condition : empty '

def p_value_list_1(t):
    ' value_list : value_list COMMA expression '
    t[0] = AST('value-list', [t[1], t[3]])

def p_value_list_2(t):
    ' value_list : expression '
    t[0] = AST('value-list', [t[1]])

def p_value_list_3(t):
    ' value_list : empty '
    t[0] = AST('value-list', [])

def p_expression_1(t):
    ' expression : binary_expression '
    t[0] = AST('binary-expr', t[1])

def p_expression_2(t):
    ' expression : list_rem '
    t[0] = AST('list-rem', t[1])

def p_expression_3(t):
    ' expression : hash_def '
    t[0] = AST('hash-def', t[1])

def p_expression_4(t):
    ' expression : hash_rem '
    t[0] = AST('hash-rem', t[1])

def p_list_rem_1(t):
    ' list_rem : ID L_BRACKET OR value R_BRACKET'
    t[0] = AST('list-rem-end', [t[1], t[4]])

def p_list_rem_2(t):
    ' list_rem : ID L_BRACKET value OR R_BRACKET'
    t[0] = AST('list-rem-begin', [t[1], t[3]])

def p_list_rem_3(t):
    ' list_rem : ID L_BRACKET value OR value R_BRACKET'
    t[0] = AST('list-rem-both', [t[1], t[3], t[5]])

def p_binary_expression_1(t):
    ' binary_expression : binary_expression operator binary_expression '
    t[0] = AST('bin-expr', [t[1], t[2], t[3]])

def p_binary_expression_2(t):
    ' binary_expression : L_PAREN binary_expression R_PAREN '
    t[0] = AST('bin-expr-paren', t[2])

def p_binary_expression_3(t):
    ' binary_expression : unary_operator binary_expression '
    t[0] = AST('bin-expr-un', [t[1], t[2]])

def p_binary_expression_4(t):
    ' binary_expression : value '
    t[0] = AST('bin-expr-val', t[1])

def p_list_req(t):
    ' list_req : ID list_req_access '
    t[0] = AST('list-req', [t[1], t[2]])

def p_list_req_access_1(t):
    ' list_req_access : L_BRACKET binary_expression R_BRACKET list_req_access '
    t[0] = AST('list-req-acc', [t[2], t[4]])

def p_list_req_access_2(t):
    ' list_req_access : L_BRACKET binary_expression R_BRACKET '
    t[0] = AST('list-req-acc', [t[2]])

def p_operator_1(t):
    ' operator : binary_operator '
    t[0] = t[1]

def p_operator_2(t):
    ' operator : relational_operator '
    t[0] = t[1]

def p_statement(t):
    '''
    statement : expression_statement SEMICOLON
              | compound_statement
              | loop_statement
              | condition_statement
              | return_command
              | free_function SEMICOLON
              | import_function SEMICOLON
              | external_call SEMICOLON
              | task_call SEMICOLON
              | loop_flows SEMICOLON
    '''
    t[0] = t[1]

def p_external_call(t):
    ' external_call : ID DOT task_call '
    t[0] = AST('ext-call', [t[1], t[3]])

def p_expression_statement_1(t):
    ' expression_statement : ID assignment_operator expression '
    t[0] = AST('expr-assign', [t[1], t[2], t[3]])

def p_expression_statement_2(t):
    ' expression_statement : list_req assignment_operator expression '
    t[0] = AST('expr-assign', [t[1], t[2], t[3]])

def p_assignment_operator(t):
    '''
    assignment_operator : ASSIGN
                        | MUL_ASSIGN
                        | DIV_ASSIGN
                        | ADD_ASSIGN
                        | SUB_ASSIGN
                        | EXP_ASSIGN
                        | LEFT_ASSIGN
                        | RIGHT_ASSIGN
                        | AND_ASSIGN
                        | OR_ASSIGN
                        | XOR_ASSIGN
                        | MOD_ASSIGN
    '''
    t[0] = AST('assign-op', t[1])

def p_compound_statement_1(t):
    ' compound_statement : L_BRACE R_BRACE '
    t[0] = AST('comp-stmt', None)

def p_compound_statement_2(t):
    ' compound_statement : L_BRACE statement_list R_BRACE '
    t[0] = AST('comp-stmt', t[2])

def p_statement_list_1(t):
    ' statement_list : statement_list statement '
    t[0] = AST('stmt-list', [t[1], t[2]])

def p_statement_list_2(t):
    ' statement_list : statement '
    t[0] = AST('stmt-list', [t[1]])

def p_loop_flows(t):
    ''' loop_flows : CONTINUE
                   | BREAK '''
    t[0] = AST('loop-flow', t[1])

def p_import_function_1(t):
    ' import_function : ID ASSIGN IMPORT L_PAREN STR R_PAREN '
    t[0] = AST('import-func', [t[1], t[5]])

def p_import_function_2(t):
    ' import_function : IMPORT L_PAREN ID R_PAREN '
    t[0] = AST('import-func', [t[3]])

def p_free_function(t):
    ' free_function : ID ASSIGN FREE L_PAREN ID R_PAREN '
    t[0] = AST('free-func', [t[1], t[5]])

def p_return_command(t):
    ' return_command : RETURN L_PAREN expression R_PAREN SEMICOLON '
    t[0] = AST('return-func', t[3])

def p_list_def_1(t):
    ' list_def : L_BRACKET binary_expression COLON binary_expression R_BRACKET '
    t[0] = AST('list-def', [t[2], t[4]])

def p_list_def_2(t):
    ' list_def : L_BRACKET value_list R_BRACKET '
    t[0] = AST('list-def', t[2])

def p_hash_def(t):
    ' hash_def : L_BRACE key_value_list R_BRACE '
    t[0] = AST('hash-def', t[2])
    
def p_hash_rem(t):
    ''' hash_rem : value REM list_def '''
    t[0] = AST('hash-rem', [t[1], t[3]])

def p_key_value_list_1(t):
    ' key_value_list : key_value_list COMMA value COLON expression '
    t[0] = AST('key-value-list', [t[1], t[3], t[5]])

def p_key_value_list_2(t):
    ' key_value_list : value COLON expression '
    t[0] = AST('key-value-list', [t[1], t[3]])

def p_key_value_list_3(t):
    ' key_value_list : empty '
    t[0] = AST('hey-value-list', [])

def p_task_call(t):
    ' task_call : ID L_PAREN value_list R_PAREN '
    t[0] = AST('task-call', [t[1], t[3]])

def p_value_1(t):
    ' value : ID '
    t[0] = AST('id', t[1])

def p_value_2(t):
    ' value : INT '
    t[0] = AST('int', t[1])

def p_value_3(t):
    ' value : FLOAT '
    t[0] = AST('float', t[1])

def p_value_4(t):
    ' value : STR '
    t[0] = AST('str', t[1])

def p_value_5(t):
    ' value : task_call '
    t[0] = AST('task-call', [t[1]])

def p_value_6(t):
    ' value : list_req '
    t[0] = AST('list-req', t[1])

def p_value_7(t):
    ' value : external_call '
    t[0] = AST('ext-call', t[1])

def p_value_8(t):
    ' value : list_def '
    t[0] = AST('list-def', t[1])

def p_value_9(t):
    ' value : LEN value '
    t[0] = AST('len', t[2])

def p_value_10(t):
    ' value : NULL '
    t[0] = AST('null', t[1])

def p_unary_operator(t):
    '''
    unary_operator : ADD
                   | SUB
                   | NOT
    '''
    t[0] = AST('unary-operator', t[1])

def p_binary_operator(t):
    '''
    binary_operator : ADD
                    | SUB
                    | MUL
                    | DIV
                    | EXP
                    | AND
                    | OR
                    | XOR
                    | MOD
                    | RIGHT_OP
                    | LEFT_OP
    '''
    t[0] = AST('binary-operator', t[1])

def p_relational_operator(t):
    '''
    relational_operator : NOT_OP
                        | AND_OP
                        | OR_OP
                        | LE_OP
                        | GE_OP
                        | EQ_OP
                        | NE_OP
                        | MAJOR
                        | MINOR
    '''
    t[0] = AST('relational-operator', t[1])

def p_empty(t):
    ' empty : '

def p_error(t):
    if t:
        print "Syntax error: '%s' Line %d" % (t.value, t.lineno)
    else:
        yacc.restart()
        print "Syntax error"

def parse_tree(code):
    parser = yacc.yacc(debug=True)
    return parser.parse(code)

if __name__ == "__main__":
    import sys
    parser = yacc.yacc(debug=True)
    code = open(sys.argv[1])
    parser.parse(code.read())
