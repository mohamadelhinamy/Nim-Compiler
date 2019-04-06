import argparse
from antlr4 import *
from NimLexer import NimLexer
from NimListener import NimListener
from NimParser import NimParser
from antlr4.tree.Trees import Trees
def get_token_type(token):
    if token.type == NimLexer.AND:
        return "AND"
    elif token.type == NimLexer.VARIABLE:
        return "VARIABLE"
    elif token.type == NimLexer.ADDR:
        return "ADDR"
    elif token.type == NimLexer.AS:
        return "AS"
    elif token.type == NimLexer.ASM:
        return "ASM"
    elif token.type == NimLexer.BIND:
        return "BIND"
    elif token.type == NimLexer.BLOCK:
        return "BLOCK"
    elif token.type == NimLexer.BREAK:
        return "BREAK"
    elif token.type == NimLexer.CASE:
        return "CASE"
    elif token.type == NimLexer.CAST:
        return "CAST"
    elif token.type == NimLexer.CONCEPT:
        return "CONCEPT"
    elif token.type == NimLexer.CONST:
        return "CONST"
    elif token.type == NimLexer.CONTINUE:
        return "CONTINUE"
    elif token.type == NimLexer.CONVERTER:
        return "CONVERTER"
    elif token.type == NimLexer.DEFER:
        return "DEFER"
    elif token.type == NimLexer.DISCARD:
        return "DISCARD"
    elif token.type == NimLexer.DISTINCT:
        return "DISTINCT"
    elif token.type == NimLexer.DIV:
        return "DIV"
    elif token.type == NimLexer.DO:
        return "DO"
    elif token.type == NimLexer.ELIF:
        return "ELIF"
    elif token.type == NimLexer.ELSE:
        return "ELSE"
    elif token.type == NimLexer.END:
        return "END"
    elif token.type == NimLexer.ENUM:
        return "ENUM"
    elif token.type == NimLexer.EXCEPT:
        return "EXCEPT"
    elif token.type == NimLexer.EXPORT:
        return "EXPORT"
    elif token.type == NimLexer.FINALLY:
        return "FINALLY"
    elif token.type == NimLexer.FOR:
        return "FOR"
    elif token.type == NimLexer.FROM:
        return "FROM"
    elif token.type == NimLexer.FUNC:
        return "FUNC"
    elif token.type == NimLexer.IF:
        return "IF"
    elif token.type == NimLexer.IMPORT:
        return "IMPORT"
    elif token.type == NimLexer.IN:
        return "IN"
    elif token.type == NimLexer.INCLUDE:
        return "INCLUDE"
    elif token.type == NimLexer.INTERFACE:
        return "INTERFACE"
    elif token.type == NimLexer.IS:
        return "IS"
    elif token.type == NimLexer.ISNOT:
        return "ISNOT"
    elif token.type == NimLexer.ITERATOR:
        return "ITERATOR"
    elif token.type == NimLexer.LET:
        return "LET"
    elif token.type == NimLexer.MACRO:
        return "MACRO"
    elif token.type == NimLexer.METHOD:
        return "METHOD"
    elif token.type == NimLexer.MIXIN:
        return "MIXIN"
    elif token.type == NimLexer.MOD:
        return "MOD"
    elif token.type == NimLexer.NIL:
        return "NIL"
    elif token.type == NimLexer.NOT:
        return "NOT"
    elif token.type == NimLexer.NOTIN:
        return "NOTIN"
    elif token.type == NimLexer.OBJECT:
        return "OBJECT"
    elif token.type == NimLexer.OF:
        return "OF"
    elif token.type == NimLexer.OR:
        return "OR"
    elif token.type == NimLexer.OUT:
        return "OUT"
    elif token.type == NimLexer.PROC:
        return "PROC"
    elif token.type == NimLexer.PTR:
        return "PTR"
    elif token.type == NimLexer.RAISE:
        return "RAISE"
    elif token.type == NimLexer.REF:
        return "REF"
    elif token.type == NimLexer.RETURN:
        return "RETURN"
    elif token.type == NimLexer.SHL:
        return "SHL"
    elif token.type == NimLexer.SHR:
        return "SHR"
    elif token.type == NimLexer.STATIC:
        return "STATIC"
    elif token.type == NimLexer.TEMPLATE:
        return "TEMPLATE"
    elif token.type == NimLexer.TRY:
        return "TRY"
    elif token.type == NimLexer.TUPLE:
        return "TUPLE"
    elif token.type == NimLexer.TYPE:
        return "TYPE"
    elif token.type == NimLexer.USING:
        return "USING"
    elif token.type == NimLexer.WHEN:
        return "WHEN"
    elif token.type == NimLexer.WHILE:
        return "WHILE"
    elif token.type == NimLexer.XOR:
        return "XOR"
    elif token.type == NimLexer.YIELD:
        return "YIELD"
    elif token.type == NimLexer.LETTER:
        return "LETTER"
    elif token.type == NimLexer.DIGIT:
        return "DIGIT"
    elif token.type == NimLexer.IDENTIFIER:
        return "IDENTIFIER"
    elif token.type == NimLexer.HEXDIGIT:
        return "HEXDIGIT"
    elif token.type == NimLexer.OCTDIGIT:
        return "OCTDIGIT"
    elif token.type == NimLexer.BINDIGIT:
        return "BINDIGIT"
    elif token.type == NimLexer.HEX_LIT:
        return "HEX_LIT"
    elif token.type == NimLexer.DEC_LIT:
        return "DEC_LIT"
    elif token.type == NimLexer.OCT_LIT:
        return "OCT_LIT"
    elif token.type == NimLexer.BIN_LIT:
        return "BIN_LIT"
    elif token.type == NimLexer.INT_LIT:
        return "INT_LIT"
    elif token.type == NimLexer.INT8_LIT:
        return "INT8_LIT"
    elif token.type == NimLexer.INT16_LIT:
        return "INT16_LIT"
    elif token.type == NimLexer.INT32_LIT:
        return "INT32_LIT"
    elif token.type == NimLexer.INT64_LIT:
        return "INT64_LIT"
    elif token.type == NimLexer.UINT_LIT:
        return "UINT_LIT"
    elif token.type == NimLexer.UINT8_LIT:
        return "UINT8_LIT"
    elif token.type == NimLexer.UINT16_LIT:
        return "UINT16_LIT"
    elif token.type == NimLexer.UINT32_LIT:
        return "UINT32_LIT"
    elif token.type == NimLexer.UINT64_LIT:
        return "UINT64_LIT"
    elif token.type == NimLexer.EXP:
        return "EXP"
    elif token.type == NimLexer.FLOAT_LIT:
        return "FLOAT_LIT"
    elif token.type == NimLexer.FLOAT32_SUFFIX:
        return "FLOAT32_SUFFIX"
    elif token.type == NimLexer.FLOAT64_SUFFIX:
        return "FLOAT64_SUFFIX"
    elif token.type == NimLexer.FLOAT32_LIT:
        return "FLOAT32_LIT"
    elif token.type == NimLexer.FLOAT64_LIT:
        return "FLOAT64_LIT"
    elif token.type == NimLexer.EQUALS_OPERATOR:
        return "EQUALS_OPERATOR"
    elif token.type == NimLexer.ADD_OPERATOR:
        return "ADD_OPERATOR"
    elif token.type == NimLexer.MUL_OPERATOR:
        return "MUL_OPERATOR"
    elif token.type == NimLexer.MINUS_OPERATOR:
        return "MINUS_OPERATOR"
    elif token.type == NimLexer.DIV_OPERATOR:
        return "DIV_OPERATOR"
    elif token.type == NimLexer.BITWISE_NOT_OPERATOR:
        return "BITWISE_NOT_OPERATOR"
    elif token.type == NimLexer.AND_OPERATOR:
        return "AND_OPERATOR"
    elif token.type == NimLexer.OR_OPERATOR:
        return "OR_OPERATOR"
    elif token.type == NimLexer.LESS_THAN:
        return "LESS_THAN"
    elif token.type == NimLexer.GREATER_THAN:
        return "GREATER_THAN"
    elif token.type == NimLexer.AT:
        return "AT"
    elif token.type == NimLexer.MODULUS:
        return "MODULUS"
    elif token.type == NimLexer.NOT_OPERATOR:
        return "NOT_OPERATOR"
    elif token.type == NimLexer.XOR_OPERATOR:
        return "XOR_OPERATOR"
    elif token.type == NimLexer.DOT:
        return "DOT"
    elif token.type == NimLexer.COLON:
        return "COLON"
    elif token.type == NimLexer.OPEN_PAREN:
        return "OPEN_PAREN"
    elif token.type == NimLexer.CLOSE_PAREN:
        return "CLOSE_PAREN"
    elif token.type == NimLexer.OPEN_BRACE:
        return "OPEN_BRACE"
    elif token.type == NimLexer.CLOSE_BRACE:
        return "CLOSE_BRACE"
    elif token.type == NimLexer.OPEN_BRACK:
        return "OPEN_BRACK"
    elif token.type == NimLexer.CLOSE_BRACK:
        return "CLOSE_BRACK"
    elif token.type == NimLexer.COMMA:
        return "COMMA"
    elif token.type == NimLexer.SEMI_COLON:
        return "SEMI_COLON"
    elif token.type == NimLexer.ESCAPE:
        return "ESCAPE"
    elif token.type == NimLexer.STR_LIT:
        return "STR_LIT"
    elif token.type == NimLexer.CHAR_LIT:
        return "CHAR_LIT"
    elif token.type == NimLexer.TRIPLESTR_LIT:
        return "TRIPLESTR_LIT"
    elif token.type == NimLexer.RSTR_LIT:
        return "RSTR_LIT"
    elif token.type == NimLexer.GENERALIZED_STR_LIT:
        return "GENERALIZED_STR_LIT"
    elif token.type == NimLexer.GENERALIZED_TRIPLESTR_LIT:
        return "GENERALIZED_TRIPLESTR_LIT"
    elif token.type == NimLexer.INDENT:
        return "INDENT"
    elif token.type == NimLexer.COMMENT:
        return "COMMENT"
    elif token.type == NimLexer.MULTILINE_COMMENT:
        return "MULTILINE_COMMENT"
    else:
        return "ERROR UNKNOWN TOKEN"

def main():

    with open(args.file, "r") as file:
        lines = file.read()
    input_stream = InputStream(lines)
    lexer = NimLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = NimParser(token_stream)

 #   tree = parser.start()
 #   print(Trees.toStringTree(tree,None, parser))

    token = lexer.nextToken()
    f = open("Nim_result.txt", "w")

    while not token.type == Token.EOF:
        print(get_token_type(token), token.text)
        f.write(get_token_type(token)+"  "+token.text)
        f.write("\n")
        token = lexer.nextToken()

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?", metavar="file")

    args = parser.parse_args()


    # parser.add_argument('--dfa-file', action="store", help="path of file to take as input to construct DFA", nargs="?", metavar="dfa_file")
    # parser.add_argument('--input-file', action="store", help="path of file to take as input to test strings in on DFA", nargs="?", metavar="input_file")
    
    

    # print(args.dfa_file)
    # print(args.input_file)

    main()