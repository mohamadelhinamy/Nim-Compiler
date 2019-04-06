# Generated from Nim.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u0082")
        buf.write("\13\4\2\t\2\3\2\7\2\6\n\2\f\2\16\2\t\13\2\3\2\2\2\3\2")
        buf.write("\2\2\2\n\2\7\3\2\2\2\4\6\7N\2\2\5\4\3\2\2\2\6\t\3\2\2")
        buf.write("\2\7\5\3\2\2\2\7\b\3\2\2\2\b\3\3\2\2\2\t\7\3\2\2\2\3\7")
        return buf.getvalue()


class NimParser ( Parser ):

    grammarFileName = "Nim.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'and'", "'var'", "'addr'", 
                     "'as'", "'asm'", "'bind'", "'block'", "'break'", "'case'", 
                     "'cast'", "'concept'", "'const'", "'continue'", "'converter'", 
                     "'defer'", "'discard'", "'distinct'", "'div'", "'do'", 
                     "'elif'", "'else'", "'end'", "'enum'", "'except'", 
                     "'export'", "'finally'", "'for'", "'from'", "'func'", 
                     "'if'", "'import'", "'in'", "'include'", "'interface'", 
                     "'is'", "'isnot'", "'iterator'", "'let'", "'macro'", 
                     "'method'", "'mixin'", "'mod'", "'nil'", "'not'", "'notin'", 
                     "'object'", "'of'", "'or'", "'out'", "'proc'", "'ptr'", 
                     "'raise'", "'ref'", "'return'", "'shl'", "'shr'", "'static'", 
                     "'template'", "'try'", "'tuple'", "'type'", "'using'", 
                     "'when'", "'while'", "'xor'", "'yield'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'*'", "'-'", "'/'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'<'", "'>'", 
                     "'at'", "<INVALID>", "<INVALID>", "<INVALID>", "'.'", 
                     "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "SPACE", "AND", "VARIABLE", "ADDR", "AS", 
                      "ASM", "BIND", "BLOCK", "BREAK", "CASE", "CAST", "CONCEPT", 
                      "CONST", "CONTINUE", "CONVERTER", "DEFER", "DISCARD", 
                      "DISTINCT", "DIV", "DO", "ELIF", "ELSE", "END", "ENUM", 
                      "EXCEPT", "EXPORT", "FINALLY", "FOR", "FROM", "FUNC", 
                      "IF", "IMPORT", "IN", "INCLUDE", "INTERFACE", "IS", 
                      "ISNOT", "ITERATOR", "LET", "MACRO", "METHOD", "MIXIN", 
                      "MOD", "NIL", "NOT", "NOTIN", "OBJECT", "OF", "OR", 
                      "OUT", "PROC", "PTR", "RAISE", "REF", "RETURN", "SHL", 
                      "SHR", "STATIC", "TEMPLATE", "TRY", "TUPLE", "TYPE", 
                      "USING", "WHEN", "WHILE", "XOR", "YIELD", "IDENTIFIER", 
                      "LETTER", "DIGIT", "HEXDIGIT", "OCTDIGIT", "BINDIGIT", 
                      "INT_LIT", "HEX_LIT", "DEC_LIT", "OCT_LIT", "BIN_LIT", 
                      "INT8_LIT", "INT16_LIT", "INT32_LIT", "INT64_LIT", 
                      "UINT_LIT", "UINT8_LIT", "UINT16_LIT", "UINT32_LIT", 
                      "UINT64_LIT", "EXP", "FLOAT_LIT", "FLOAT32_SUFFIX", 
                      "FLOAT64_SUFFIX", "FLOAT32_LIT", "FLOAT64_LIT", "EQUALS_OPERATOR", 
                      "ADD_OPERATOR", "MUL_OPERATOR", "MINUS_OPERATOR", 
                      "DIV_OPERATOR", "BITWISE_NOT_OPERATOR", "AND_OPERATOR", 
                      "OR_OPERATOR", "LESS_THAN", "GREATER_THAN", "AT", 
                      "MODULUS", "NOT_OPERATOR", "XOR_OPERATOR", "DOT", 
                      "COLON", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE", 
                      "CLOSE_BRACE", "OPEN_BRACK", "CLOSE_BRACK", "COMMA", 
                      "SEMI_COLON", "ESCAPE", "STR_LIT", "CHAR_LIT", "TRIPLESTR_LIT", 
                      "RSTR_LIT", "GENERALIZED_STR_LIT", "GENERALIZED_TRIPLESTR_LIT", 
                      "MULTILINE_COMMENT", "COMMENT", "INDENT", "INDENT_GREATER" ]

    RULE_start = 0

    ruleNames =  [ "start" ]

    EOF = Token.EOF
    SPACE=1
    AND=2
    VARIABLE=3
    ADDR=4
    AS=5
    ASM=6
    BIND=7
    BLOCK=8
    BREAK=9
    CASE=10
    CAST=11
    CONCEPT=12
    CONST=13
    CONTINUE=14
    CONVERTER=15
    DEFER=16
    DISCARD=17
    DISTINCT=18
    DIV=19
    DO=20
    ELIF=21
    ELSE=22
    END=23
    ENUM=24
    EXCEPT=25
    EXPORT=26
    FINALLY=27
    FOR=28
    FROM=29
    FUNC=30
    IF=31
    IMPORT=32
    IN=33
    INCLUDE=34
    INTERFACE=35
    IS=36
    ISNOT=37
    ITERATOR=38
    LET=39
    MACRO=40
    METHOD=41
    MIXIN=42
    MOD=43
    NIL=44
    NOT=45
    NOTIN=46
    OBJECT=47
    OF=48
    OR=49
    OUT=50
    PROC=51
    PTR=52
    RAISE=53
    REF=54
    RETURN=55
    SHL=56
    SHR=57
    STATIC=58
    TEMPLATE=59
    TRY=60
    TUPLE=61
    TYPE=62
    USING=63
    WHEN=64
    WHILE=65
    XOR=66
    YIELD=67
    IDENTIFIER=68
    LETTER=69
    DIGIT=70
    HEXDIGIT=71
    OCTDIGIT=72
    BINDIGIT=73
    INT_LIT=74
    HEX_LIT=75
    DEC_LIT=76
    OCT_LIT=77
    BIN_LIT=78
    INT8_LIT=79
    INT16_LIT=80
    INT32_LIT=81
    INT64_LIT=82
    UINT_LIT=83
    UINT8_LIT=84
    UINT16_LIT=85
    UINT32_LIT=86
    UINT64_LIT=87
    EXP=88
    FLOAT_LIT=89
    FLOAT32_SUFFIX=90
    FLOAT64_SUFFIX=91
    FLOAT32_LIT=92
    FLOAT64_LIT=93
    EQUALS_OPERATOR=94
    ADD_OPERATOR=95
    MUL_OPERATOR=96
    MINUS_OPERATOR=97
    DIV_OPERATOR=98
    BITWISE_NOT_OPERATOR=99
    AND_OPERATOR=100
    OR_OPERATOR=101
    LESS_THAN=102
    GREATER_THAN=103
    AT=104
    MODULUS=105
    NOT_OPERATOR=106
    XOR_OPERATOR=107
    DOT=108
    COLON=109
    OPEN_PAREN=110
    CLOSE_PAREN=111
    OPEN_BRACE=112
    CLOSE_BRACE=113
    OPEN_BRACK=114
    CLOSE_BRACK=115
    COMMA=116
    SEMI_COLON=117
    ESCAPE=118
    STR_LIT=119
    CHAR_LIT=120
    TRIPLESTR_LIT=121
    RSTR_LIT=122
    GENERALIZED_STR_LIT=123
    GENERALIZED_TRIPLESTR_LIT=124
    MULTILINE_COMMENT=125
    COMMENT=126
    INDENT=127
    INDENT_GREATER=128

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEC_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(NimParser.DEC_LIT)
            else:
                return self.getToken(NimParser.DEC_LIT, i)

        def getRuleIndex(self):
            return NimParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = NimParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==NimParser.DEC_LIT:
                self.state = 2
                self.match(NimParser.DEC_LIT)
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





