grammar RelationalLang;

program
    : subprogram* statement* EOF
    ;

subprogram
    : 'def' ID '(' params? ')' block
    ;

params
    : ID (',' ID)*
    ;

block
    : '{' (statement | NEWLINE)* '}'
    ;

statement
    : ifStmt
    | whileStmt
    | untilStmt
    | forStmt
    | assignment
    | functionCall
    | returnStmt
    | NEWLINE
    ;

ifStmt
    : 'if' expr 'then' block ('else' block)?
    ;

whileStmt : 'while' expr block ;
untilStmt : 'until' expr block ;
forStmt   : 'for' ID '=' expr ';' expr ';' assignment block ;

assignment
    : varName '=' expr
    ;

varName
    : ID | TYPE 
    ;

returnStmt : 'return' expr ;

expr
    : '(' TYPE ')' expr
    | '(' expr ')'
    | expr (MUL | DIV | MOD) expr
    | expr (ADD | SUB) expr
    | expr (EQ | NEQ | GT | LT | GE | LE) expr
    | expr (AND | OR) expr
    | primary
    ;

primary
    : varName
    | NUMBER
    | STRING
    | functionCall
    | varName '[' expr ']'
    ;

functionCall
    : 'read' '(' ')'
    | 'write' '(' expr ')'
    | 'table' '(' (expr (',' expr)*)? ')'
    | 'find' '(' (expr (',' expr)*)? ')'
    | 'update' '(' (expr (',' expr)*)? ')'
    | ID '(' (expr (',' expr)*)? ')'
    ;

TYPE: 'table' | 'row' | 'column' | 'int' | 'float' | 'string';
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' .*? '"';

ADD: '+'; SUB: '-'; MUL: '*'; DIV: '/'; MOD: '%';
EQ: '=='; NEQ: '!='; GT: '>'; LT: '<'; GE: '>='; LE: '<=';
AND: '&&'; OR: '||';

WS: [ \t\r\n]+ -> skip;
NEWLINE: '\n';