grammar FunctionCall;

statement: (function|comment) NEWLINE;

function: operator (argument|'(' function ')')* ;
comment: ';' .*? ;

operator: ID ;

argument: FLOAT
        | INT
        | ID
        | STRING
        ;

ID      : [a-zA-Z][a-zA-Z0-9]* ; // match identifiers
INT     : [0-9]+ ;               // match integers
FLOAT   : [0-9]*'.'[0-9]+ ;      // match floats
STRING  : '"' .*? '"' ;          // match string literals
NEWLINE : '\r'? '\n' ;           // return newlines to parser (is end-statement signal)
WS      : [ \t]+ -> skip ;       // toss out whitespace
ANYCHAR : .; 