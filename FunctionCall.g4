grammar FunctionCall;

statement: function NEWLINE;

function: '(' operator (argument|function)* ')' ;

operator: ID ;

argument: FLOAT
        | INT
        | ID
        ;

ID      : [a-zA-Z][a-zA-Z0-9]* ; // match identifiers
INT     : [0-9]+ ;               // match integers
FLOAT   : [0-9]*'.'[0-9]+ ;      // match floats
NEWLINE : '\r'? '\n' ;           // return newlines to parser (is end-statement signal)
WS      : [ \t]+ -> skip ;       // toss out whitespace