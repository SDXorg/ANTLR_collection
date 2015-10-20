grammar Expr;

root: expr ;

expr:   Id '(' exprList? ')'              # Call
    |   ':NOT:' expr                      # Not
    |   '-' expr                          # Negative
    |   '+' expr                          # Positive
    |   expr '^' expr                     # Power
    |   expr op=('*'|'/') expr            # MulDiv
    |   expr op=('+'|'-') expr            # AddSub
    |   expr op=('<'|'>'|'<='|'>=') expr  # Relational
    |   expr op=('='|'<>') expr           # Equality
    |   expr ':AND:' expr                 # And
    |   expr ':OR:' expr                  # Or
    |   Id subscriptList?                 # Var
    |   Const                             # Const
    |   Keyword                           # Keyword
    |   '(' expr ')'                      # Parens
    ;

exprList : expr (',' expr)* ;
subscriptList : '[' Id (',' Id)* ']' ;

Star : '*' ;
Div : '/' ;
Plus : '+' ;
Minus : '-' ;
Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';
Equal : '=' ;
NotEqual : '<>' ;
Exclamation : '!';

Id : ((Nondigit IdChar*) | (Nondigit (IdChar | ' ')* IdChar) | StringLiteral) Exclamation? ;

fragment
IdChar : [a-zA-Z0-9_] ;

fragment
Nondigit : [a-zA-Z_] ;

fragment
Digit
    :   [0-9]
    ;

Const
    :   IntegerConst
    |   FloatingConst
    ;

fragment
IntegerConst
    :   Digit+
    ;

fragment
NonzeroDigit
    :   [1-9]
    ;

fragment
FloatingConst
    :   FractionalConstant ExponentPart?
    |   DigitSeq ExponentPart
    ;

fragment
FractionalConstant
    :   DigitSeq? '.' DigitSeq
    |   DigitSeq '.'
    ;

fragment
ExponentPart
    :   'e' Sign? DigitSeq
    |   'E' Sign? DigitSeq
    ;

fragment
Sign
    :   '+' | '-'
    ;

fragment
DigitSeq
    :   Digit+
    ;

StringLiteral
    :   '"' SCharSequence? '"'
    ;

fragment
SCharSequence
    :   SChar+
    ;

fragment
SChar
    :   ~["\\\r\n]
    ;

fragment
EscapeSequence
    :   '\\' ['"?abfnrtv\\]
    ;

Keyword : ':NA:' ;

Whitespace : [ \t\n\r]+ -> skip ;
