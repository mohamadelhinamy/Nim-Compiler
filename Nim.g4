//Nim.g4 file
grammar Nim;


SPACE :  [ \t\r\n] -> skip ;
AND : 'and';
VARIABLE : 'var';
ADDR : 'addr';
AS : 'as';
ASM : 'asm';
BIND : 'bind';
BLOCK : 'block';
BREAK : 'break';
CASE : 'case';
CAST : 'cast';
CONCEPT : 'concept';
CONST : 'const';
CONTINUE : 'continue';
CONVERTER : 'converter';
DEFER : 'defer';
DISCARD : 'discard';
DISTINCT : 'distinct';
DIV : 'div';
DO : 'do';
ELIF : 'elif';
ELSE : 'else';
END : 'end';
ENUM : 'enum';
EXCEPT : 'except';
EXPORT : 'export';
FINALLY : 'finally';
FOR : 'for';
FROM : 'from';
FUNC : 'func';
IF : 'if';
IMPORT : 'import';
IN : 'in';
INCLUDE : 'include';
INTERFACE : 'interface';
IS : 'is';
ISNOT : 'isnot';
ITERATOR : 'iterator';
LET : 'let';
MACRO : 'macro';
METHOD : 'method';
MIXIN : 'mixin';
MOD : 'mod';
NIL : 'nil';
NOT : 'not';
NOTIN : 'notin';
OBJECT : 'object';
OF : 'of';
OR : 'or';
OUT : 'out';
PROC : 'proc';
PTR : 'ptr';
RAISE : 'raise';
REF : 'ref';
RETURN : 'return';
SHL : 'shl';
SHR : 'shr';
STATIC : 'static';
TEMPLATE : 'template';
TRY : 'try';
TUPLE : 'tuple';
TYPE : 'type';
USING : 'using';
WHEN : 'when';
WHILE : 'while';
XOR : 'xor';
YIELD : 'yield';
IDENTIFIER : LETTER+('_'?(LETTER | DIGIT))* ; 
LETTER : [a-zA-Z_] ;
DIGIT : [0-9] ;
HEXDIGIT : DIGIT | [A-F] | [a-f];
OCTDIGIT : [0-7];
BINDIGIT : [0-1];
INT_LIT : (HEX_LIT | DEC_LIT | OCT_LIT | BIN_LIT);
HEX_LIT : '0' ('x' | 'X' ) HEXDIGIT ( '_'? HEXDIGIT )* ;
DEC_LIT : DIGIT ( '_'? DIGIT )* ;
OCT_LIT : '0' 'o' OCTDIGIT ( '_'? OCTDIGIT )* ;
BIN_LIT : '0' ('b' | 'B' ) BINDIGIT ( '_'? BINDIGIT )* ;
INT8_LIT : INT_LIT ['] ('i' | 'I') '8';
INT16_LIT : INT_LIT ['] ('i' | 'I') '16';
INT32_LIT : INT_LIT ['] ('i' | 'I') '32';
INT64_LIT : INT_LIT ['] ('i' | 'I') '64';
UINT_LIT : INT_LIT ['] ('u' | 'U');
UINT8_LIT : INT_LIT ['] ('u' | 'U') '8';
UINT16_LIT : INT_LIT ['] ('u' | 'U') '16';
UINT32_LIT : INT_LIT ['] ('u' | 'U') '32';
UINT64_LIT : INT_LIT ['] ('u' | 'U') '64';
EXP : ('e' | 'E' ) [+-] DIGIT ( '_'? DIGIT )* ;
FLOAT_LIT : DIGIT ('_'? DIGIT)* (('.' DIGIT ('_'? DIGIT)* (EXP)?) |EXP);
FLOAT32_SUFFIX : ('f' | 'F') '32';
FLOAT64_SUFFIX : ( ('f' | 'F') '64' ) | 'd' | 'D' ;
FLOAT32_LIT : HEX_LIT ['] FLOAT32_SUFFIX | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) ['] FLOAT32_SUFFIX ;
FLOAT64_LIT : HEX_LIT ['] FLOAT64_SUFFIX | (FLOAT_LIT | DEC_LIT | OCT_LIT | BIN_LIT) ['] FLOAT64_SUFFIX ;
EQUALS_OPERATOR : '=' | '==';
ADD_OPERATOR : '+';
MUL_OPERATOR : '*';
MINUS_OPERATOR : '-';
DIV_OPERATOR : '/';
BITWISE_NOT_OPERATOR : NOT ;
AND_OPERATOR : AND;
OR_OPERATOR : OR;
LESS_THAN : '<';
GREATER_THAN : '>';
AT : 'at';
MODULUS : MOD | '%';
NOT_OPERATOR : '!' | '~' ;
XOR_OPERATOR : XOR ;
DOT : '.' ;
COLON : ':';
OPEN_PAREN : '(';
CLOSE_PAREN : ')';
OPEN_BRACE : '{';
CLOSE_BRACE : '}';
OPEN_BRACK : '[';
CLOSE_BRACK : ']';
COMMA : ',';
SEMI_COLON : ';' ;
ESCAPE : ('\\' [rnft\\"'abe]) | ('\\x HH') ;
STR_LIT : '"' .*? '"';
CHAR_LIT : ['] (. | ESCAPE) ['];
TRIPLESTR_LIT : '""' STR_LIT '""'  ;
RSTR_LIT : [rR] STR_LIT ;
GENERALIZED_STR_LIT : IDENTIFIER STR_LIT;
GENERALIZED_TRIPLESTR_LIT : IDENTIFIER TRIPLESTR_LIT ;
//MULTILINE_COMMENT : ' '* (('#[' .*? SPACE*  ']#')| ('##[' .*? SPACE* ']##') ) ('\n') -> skip;
MULTILINE_COMMENT : ' '* ('#[' .*? (MULTILINE_COMMENT)* .*?']#' | '##[' .*? (MULTILINE_COMMENT)* .*? ']##') -> skip;
//MULTILINE_COMMENT_HELPER: '#' (MULTILINE_COMMENT_HELPER | MULTILINE_COMMENT_HELPER2) '#';
//MULTILINE_COMMENT_HELPER2 : '[' (.|SPACE)*? ']';
COMMENT : ' '* '#' .*? '\n' -> skip;
INDENT : '    '+;
INDENT_GREATER : ('    ' ' '+) -> skip ;



start : (DEC_LIT)*;








