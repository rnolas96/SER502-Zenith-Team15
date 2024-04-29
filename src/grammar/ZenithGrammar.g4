grammar ZenithGrammar;
//Program Structure and Blocks
// --program
program
	: 'start' block 'end'
	;

// --block
block
    : '{' atomic_block+ '}' 
    | '{'  '}'
    ;

// -- atomic block
atomic_block
	:  command+ 
    |  declaration+ 
	;

// -- declaration
declaration
    : 'int' VARIABLE_IDENTIFIER (ASSIGNMENT_OPERATOR num_expr)?              # integerDeclaration
	| 'int' VARIABLE_IDENTIFIER (ASSIGNMENT_OPERATOR ternary_expr)?          # integerDeclaration
	| 'boolean' VARIABLE_IDENTIFIER (ASSIGNMENT_OPERATOR bool_expr)?         # booleanDeclaration
	| 'boolean' VARIABLE_IDENTIFIER (ASSIGNMENT_OPERATOR ternary_expr)?      # booleanDeclaration
	| 'string' VARIABLE_IDENTIFIER (ASSIGNMENT_OPERATOR VALID_STRING)?       # stringDeclaration
	| 'string' VARIABLE_IDENTIFIER (ASSIGNMENT_OPERATOR ternary_expr)?       # stringDeclaration
    | 'float' VARIABLE_IDENTIFIER (ASSIGNMENT_OPERATOR num_expr)?       # floatDeclaration
    | 'float' VARIABLE_IDENTIFIER (ASSIGNMENT_OPERATOR ternary_expr)?        # floatDeclaration
    | 'double' VARIABLE_IDENTIFIER (ASSIGNMENT_OPERATOR num_expr)?      # doubleDeclaration
    | 'double' VARIABLE_IDENTIFIER (ASSIGNMENT_OPERATOR ternary_expr)?       # doubleDeclaration
    | '{}'                                                # emptyDeclaration
    ;

//Commands and Expressions
// --commands
command
	: (if_expr|while_expr|for_enhanced|for_loop|print|assignment_expr)
	;

// --assignments
assignment_expr
	: VARIABLE_IDENTIFIER ASSIGNMENT_OPERATOR num_expr                       # integerAssignment
	| VARIABLE_IDENTIFIER ASSIGNMENT_OPERATOR bool_expr                      # booleanAssignment
    | VARIABLE_IDENTIFIER ASSIGNMENT_OPERATOR ternary_expr                   # ternaryAssignment
    ;

// --expressions
exprs
    : num_expr
    | bool_expr
    ;

// --boolean expressions
bool_expr
    : VARIABLE_IDENTIFIER ASSIGNMENT_OPERATOR bool_expr      
    | bool_computation_expr                                  
    ;

// --bool computation
bool_computation_expr
    : bool_computation_expr op=(AND|OR|IS_EQUL_TO|NOT_EQUL_TO) bool_computation_expr  
    | comp_expr                                 
    | bool_bracket_expr
    ;

bool_bracket_expr
    : '(' bool_expr ')'
    | BOOLEAN										          
    | VARIABLE_IDENTIFIER										      
    ;

// --comparison expressions
comp_expr
    : num_expr op=(GREATER_THAN|LESS_THAN|MORE_THAN_OR_EQUL|LESS_THAN_OR_EQUL|IS_EQUL_TO|NOT_EQUL_TO) num_expr  # numberComparisonExpression
    ;

// --arithmetic expressions
num_expr
    : VARIABLE_IDENTIFIER ASSIGNMENT_OPERATOR num_expr
    | add_sub_expr
    ;

// --add and sub expressions
add_sub_expr
    : add_sub_expr (ADD|SUB) term_expr
    | term_expr
    ;

// --term expressions
term_expr
    : term_expr (MUL|DIV) bracket_expr
    | bracket_expr 
    ;

// --bracket expressions
bracket_expr
    : '(' num_expr ')' 
    | SUB? DIGITS
    | SUB? DECIMAL_VALUE
    | SUB? VARIABLE_IDENTIFIER
    ;

// Conditional and Looping Constructs
// --conditional expression
cond_expr
    : '(' bool_expr ')'
    ;

// --if expression
if_expr
    : 'if' cond_expr block (else_if_expr)* (else_expr)?
    ;

// --else if (condition) expression
else_if_expr
    : 'elseIf' cond_expr block
    ;

// --else expression
else_expr
    : 'else' block
    ;

// --while(condition) expression
while_expr
    : 'while' cond_expr block
    ;

// --for enhanced
for_enhanced
    : 'for' VARIABLE_IDENTIFIER 'in' 'range' '(' rangeVal '..' rangeVal ')' block
    ;

rangeVal
	: VARIABLE_IDENTIFIER
	| DIGITS
	;

// --for normal
for_loop
    : 'for' '(' VARIABLE_IDENTIFIER '$=' DIGITS ';' bool_expr ';' variable_change_part ')' block
    ;

variable_change_part : increment_expression
                        | decrement_expression
                        |VARIABLE_IDENTIFIER ASSIGNMENT_OPERATOR num_expr;

decrement_expression : VARIABLE_IDENTIFIER '--'
                       | '--' VARIABLE_IDENTIFIER;


increment_expression : VARIABLE_IDENTIFIER '++'
                       | '++' VARIABLE_IDENTIFIER;


//Other Elements and Miscellaneous
ternary_expr
    : cond_expr '?' exprs ':' exprs
    | cond_expr '?' BOOLEAN ':' BOOLEAN
    | cond_expr '?' VALID_STRING ':' VALID_STRING
    ;

// all types of values
value
    : DIGITS
    | BOOLEAN
    | VARIABLE_IDENTIFIER
    | num_expr
    | bool_expr
    | VALID_STRING
    ;

// --print statement
print
    : 'print' '(' print_parameters ')'
    | 'print' '(' (print_parameters ',')+ print_parameters ')'
    ;

// -- print parameters
print_parameters
    : value
    ;


// --numbers > 0.
DIGITS
	: [1-9] [0-9]*
	| '0'
	;

//  --primitive types
primitive_type
    : 'num'
    | 'boolean'
    | 'float'
    | 'double'
    | 'string'
    ;

// --Boolean value as true or false.
BOOLEAN
	: 'true'
	| 'false'
	;

// --operators
ADD               : '+';
SUB               : '-';
MUL               : '*';
DIV               : '/';
AND               : 'and';
OR                : 'or';
LESS_THAN         : '<';
GREATER_THAN      : '>';
LESS_THAN_OR_EQUL : '<=';
MORE_THAN_OR_EQUL : '>=';
NOT_EQUL_TO       : 'not';
IS_EQUL_TO        : '==';

// --lower case and upper case letters.
VARIABLE_IDENTIFIER
	: [a-zA-Z_] [a-zA-Z_0-9]*
	;

// --valid Strings
VALID_STRING
    : '"'[a-zA-Z0-9_]+'"'
    | EMPTY_STRING
    ;

// --decimal values
DECIMAL_VALUE
    : DIGITS '.' (DIGITS)
    | DIGITS '.0'
    ;

// --assignment operator
ASSIGNMENT_OPERATOR   : '=';

// --defining whitespaces
WHITE_SPACES    : [ \t\r\n]+ -> skip; // skip spaces, tabs and newline

// --empty string
EMPTY_STRING: '""';

// --comment syntax
Comment : ('#' ~[\r\n]* | '/#' .*? '#/') -> skip;
