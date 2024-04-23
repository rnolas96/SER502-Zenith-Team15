grammar ZenithGrammar;

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
    : 'for' '(' (declaration|assignment_expr) ';' bool_expr ';' variable_change_part ')' block
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