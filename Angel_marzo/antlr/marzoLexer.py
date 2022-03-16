# Generated from /Users/angelheredia/Desktop/Angel_marzo/antlr/marzo.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\6\13<\n\13\r\13\16\13=\3\f\3\f\3\r\6")
        buf.write("\rC\n\r\r\r\16\rD\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\5\3\2\62;\4\2")
        buf.write("C\\c|\5\2\13\f\17\17\"\"\2I\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2")
        buf.write("\2\t!\3\2\2\2\13#\3\2\2\2\r(\3\2\2\2\17*\3\2\2\2\21/\3")
        buf.write("\2\2\2\23\63\3\2\2\2\25;\3\2\2\2\27?\3\2\2\2\31B\3\2\2")
        buf.write("\2\33\34\7-\2\2\34\4\3\2\2\2\35\36\7?\2\2\36\6\3\2\2\2")
        buf.write("\37 \7>\2\2 \b\3\2\2\2!\"\7@\2\2\"\n\3\2\2\2#$\7k\2\2")
        buf.write("$%\7h\2\2%&\7\"\2\2&\'\7*\2\2\'\f\3\2\2\2()\7+\2\2)\16")
        buf.write("\3\2\2\2*+\7g\2\2+,\7n\2\2,-\7u\2\2-.\7g\2\2.\20\3\2\2")
        buf.write("\2/\60\7k\2\2\60\61\7p\2\2\61\62\7v\2\2\62\22\3\2\2\2")
        buf.write("\63\64\7r\2\2\64\65\7t\2\2\65\66\7k\2\2\66\67\7p\2\2\67")
        buf.write("8\7v\2\289\7*\2\29\24\3\2\2\2:<\t\2\2\2;:\3\2\2\2<=\3")
        buf.write("\2\2\2=;\3\2\2\2=>\3\2\2\2>\26\3\2\2\2?@\t\3\2\2@\30\3")
        buf.write("\2\2\2AC\t\4\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2")
        buf.write("\2EF\3\2\2\2FG\b\r\2\2G\32\3\2\2\2\5\2=D\3\b\2\2")
        return buf.getvalue()


class marzoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    Numero = 10
    Letra = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'='", "'<'", "'>'", "'if ('", "')'", "'else'", "'int'", 
            "'print('" ]

    symbolicNames = [ "<INVALID>",
            "Numero", "Letra", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "Numero", "Letra", "WS" ]

    grammarFileName = "marzo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


