grammar Model;
import Expr;

model : (equation | lookup)+ ;
equation: varname '=' formula ;
varname: Id subscriptList? ;
formula: (expr | constList) ;
lookup: varname '(' '[' lookupPoint '-' lookupPoint ']' ',' lookupList ')' ;
lookupList: lookupPoint (',' lookupPoint)* ;
subscriptList : '[' Id (',' Id)* ']' ;
constList : Const (',' Const)* ;
lookupPoint: '(' Const ',' Const ')' ;

Encoding: '{' [A-Za-z0-9-]+ '}' -> skip ;
UnitsDoc: '~' .*? '|' -> skip ;
Group: '****' .*? '|' -> skip;
