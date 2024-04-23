grammar ZenithGrammar;


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