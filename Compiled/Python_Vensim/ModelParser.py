# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .ModelVisitor import ModelVisitor
else:
    from ModelVisitor import ModelVisitor

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\36\u0096\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\3\2\3\2\6\2\35\n\2\r\2\16\2\36\3\3\3\3\3\3\3\3\3\4")
        buf.write(u"\3\4\5\4\'\n\4\3\5\3\5\5\5+\n\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7\7;\n\7\f\7\16\7")
        buf.write(u">\13\7\3\b\3\b\3\b\3\b\7\bD\n\b\f\b\16\bG\13\b\3\b\3")
        buf.write(u"\b\3\t\3\t\3\t\7\tN\n\t\f\t\16\tQ\13\t\3\n\3\n\3\n\3")
        buf.write(u"\n\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\5\fe\n\f\3\f\3\f\3\f\5\fj\n\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\5\fr\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write(u"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7")
        buf.write(u"\f\u0089\n\f\f\f\16\f\u008c\13\f\3\r\3\r\3\r\7\r\u0091")
        buf.write(u"\n\r\f\r\16\r\u0094\13\r\3\r\2\3\26\16\2\4\6\b\n\f\16")
        buf.write(u"\20\22\24\26\30\2\6\3\2\17\20\3\2\21\22\3\2\23\26\3\2")
        buf.write(u"\27\30\u00a1\2\34\3\2\2\2\4 \3\2\2\2\6$\3\2\2\2\b*\3")
        buf.write(u"\2\2\2\n,\3\2\2\2\f\67\3\2\2\2\16?\3\2\2\2\20J\3\2\2")
        buf.write(u"\2\22R\3\2\2\2\24X\3\2\2\2\26q\3\2\2\2\30\u008d\3\2\2")
        buf.write(u"\2\32\35\5\4\3\2\33\35\5\n\6\2\34\32\3\2\2\2\34\33\3")
        buf.write(u"\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37\3")
        buf.write(u"\3\2\2\2 !\5\6\4\2!\"\7\27\2\2\"#\5\b\5\2#\5\3\2\2\2")
        buf.write(u"$&\7\32\2\2%\'\5\16\b\2&%\3\2\2\2&\'\3\2\2\2\'\7\3\2")
        buf.write(u"\2\2(+\5\26\f\2)+\5\20\t\2*(\3\2\2\2*)\3\2\2\2+\t\3\2")
        buf.write(u"\2\2,-\5\6\4\2-.\7\3\2\2./\7\4\2\2/\60\5\22\n\2\60\61")
        buf.write(u"\7\22\2\2\61\62\5\22\n\2\62\63\7\5\2\2\63\64\7\6\2\2")
        buf.write(u"\64\65\5\f\7\2\65\66\7\7\2\2\66\13\3\2\2\2\67<\5\22\n")
        buf.write(u"\289\7\6\2\29;\5\22\n\2:8\3\2\2\2;>\3\2\2\2<:\3\2\2\2")
        buf.write(u"<=\3\2\2\2=\r\3\2\2\2><\3\2\2\2?@\7\4\2\2@E\7\32\2\2")
        buf.write(u"AB\7\6\2\2BD\7\32\2\2CA\3\2\2\2DG\3\2\2\2EC\3\2\2\2E")
        buf.write(u"F\3\2\2\2FH\3\2\2\2GE\3\2\2\2HI\7\5\2\2I\17\3\2\2\2J")
        buf.write(u"O\7\33\2\2KL\7\6\2\2LN\7\33\2\2MK\3\2\2\2NQ\3\2\2\2O")
        buf.write(u"M\3\2\2\2OP\3\2\2\2P\21\3\2\2\2QO\3\2\2\2RS\7\3\2\2S")
        buf.write(u"T\7\33\2\2TU\7\6\2\2UV\7\33\2\2VW\7\7\2\2W\23\3\2\2\2")
        buf.write(u"XY\5\26\f\2Y\25\3\2\2\2Z[\b\f\1\2[\\\7\b\2\2\\r\5\26")
        buf.write(u"\f\20]^\7\22\2\2^r\5\26\f\17_`\7\21\2\2`r\5\26\f\16a")
        buf.write(u"b\7\32\2\2bd\7\3\2\2ce\5\30\r\2dc\3\2\2\2de\3\2\2\2e")
        buf.write(u"f\3\2\2\2fr\7\7\2\2gi\7\32\2\2hj\5\16\b\2ih\3\2\2\2i")
        buf.write(u"j\3\2\2\2jr\3\2\2\2kr\7\33\2\2lr\7\35\2\2mn\7\3\2\2n")
        buf.write(u"o\5\26\f\2op\7\7\2\2pr\3\2\2\2qZ\3\2\2\2q]\3\2\2\2q_")
        buf.write(u"\3\2\2\2qa\3\2\2\2qg\3\2\2\2qk\3\2\2\2ql\3\2\2\2qm\3")
        buf.write(u"\2\2\2r\u008a\3\2\2\2st\f\r\2\2tu\7\t\2\2u\u0089\5\26")
        buf.write(u"\f\16vw\f\f\2\2wx\t\2\2\2x\u0089\5\26\f\ryz\f\13\2\2")
        buf.write(u"z{\t\3\2\2{\u0089\5\26\f\f|}\f\n\2\2}~\t\4\2\2~\u0089")
        buf.write(u"\5\26\f\13\177\u0080\f\t\2\2\u0080\u0081\t\5\2\2\u0081")
        buf.write(u"\u0089\5\26\f\n\u0082\u0083\f\b\2\2\u0083\u0084\7\n\2")
        buf.write(u"\2\u0084\u0089\5\26\f\t\u0085\u0086\f\7\2\2\u0086\u0087")
        buf.write(u"\7\13\2\2\u0087\u0089\5\26\f\b\u0088s\3\2\2\2\u0088v")
        buf.write(u"\3\2\2\2\u0088y\3\2\2\2\u0088|\3\2\2\2\u0088\177\3\2")
        buf.write(u"\2\2\u0088\u0082\3\2\2\2\u0088\u0085\3\2\2\2\u0089\u008c")
        buf.write(u"\3\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write(u"\27\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u0092\5\26\f\2")
        buf.write(u"\u008e\u008f\7\6\2\2\u008f\u0091\5\26\f\2\u0090\u008e")
        buf.write(u"\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092")
        buf.write(u"\u0093\3\2\2\2\u0093\31\3\2\2\2\u0094\u0092\3\2\2\2\17")
        buf.write(u"\34\36&*<EOdiq\u0088\u008a\u0092")
        return buf.getvalue()


class ModelParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"'['", u"']'", u"','", u"')'", 
                     u"':NOT:'", u"'^'", u"':AND:'", u"':OR:'", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'*'", u"'/'", u"'+'", 
                     u"'-'", u"'<'", u"'<='", u"'>'", u"'>='", u"'='", u"'<>'", 
                     u"'!'", u"<INVALID>", u"<INVALID>", u"<INVALID>", u"':NA:'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"Encoding", u"UnitsDoc", 
                      u"Group", u"Star", u"Div", u"Plus", u"Minus", u"Less", 
                      u"LessEqual", u"Greater", u"GreaterEqual", u"Equal", 
                      u"NotEqual", u"Exclamation", u"Id", u"Const", u"StringLiteral", 
                      u"Keyword", u"Whitespace" ]

    RULE_model = 0
    RULE_equation = 1
    RULE_varname = 2
    RULE_formula = 3
    RULE_lookup = 4
    RULE_lookupList = 5
    RULE_subscriptList = 6
    RULE_constList = 7
    RULE_lookupPoint = 8
    RULE_root = 9
    RULE_expr = 10
    RULE_exprList = 11

    ruleNames =  [ u"model", u"equation", u"varname", u"formula", u"lookup", 
                   u"lookupList", u"subscriptList", u"constList", u"lookupPoint", 
                   u"root", u"expr", u"exprList" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    Encoding=10
    UnitsDoc=11
    Group=12
    Star=13
    Div=14
    Plus=15
    Minus=16
    Less=17
    LessEqual=18
    Greater=19
    GreaterEqual=20
    Equal=21
    NotEqual=22
    Exclamation=23
    Id=24
    Const=25
    StringLiteral=26
    Keyword=27
    Whitespace=28

    def __init__(self, input):
        super(ModelParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ModelContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.ModelContext, self).__init__(parent, invokingState)
            self.parser = parser

        def equation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.EquationContext)
            else:
                return self.getTypedRuleContext(ModelParser.EquationContext,i)


        def lookup(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.LookupContext)
            else:
                return self.getTypedRuleContext(ModelParser.LookupContext,i)


        def getRuleIndex(self):
            return ModelParser.RULE_model

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitModel(self)
            else:
                return visitor.visitChildren(self)




    def model(self):

        localctx = ModelParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 24
                    self.equation()
                    pass

                elif la_ == 2:
                    self.state = 25
                    self.lookup()
                    pass


                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ModelParser.Id):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EquationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.EquationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varname(self):
            return self.getTypedRuleContext(ModelParser.VarnameContext,0)


        def formula(self):
            return self.getTypedRuleContext(ModelParser.FormulaContext,0)


        def getRuleIndex(self):
            return ModelParser.RULE_equation

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitEquation(self)
            else:
                return visitor.visitChildren(self)




    def equation(self):

        localctx = ModelParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.varname()
            self.state = 31
            self.match(ModelParser.Equal)
            self.state = 32
            self.formula()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarnameContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.VarnameContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(ModelParser.Id, 0)

        def subscriptList(self):
            return self.getTypedRuleContext(ModelParser.SubscriptListContext,0)


        def getRuleIndex(self):
            return ModelParser.RULE_varname

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitVarname(self)
            else:
                return visitor.visitChildren(self)




    def varname(self):

        localctx = ModelParser.VarnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ModelParser.Id)
            self.state = 36
            _la = self._input.LA(1)
            if _la==ModelParser.T__1:
                self.state = 35
                self.subscriptList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.FormulaContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ModelParser.ExprContext,0)


        def constList(self):
            return self.getTypedRuleContext(ModelParser.ConstListContext,0)


        def getRuleIndex(self):
            return ModelParser.RULE_formula

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitFormula(self)
            else:
                return visitor.visitChildren(self)




    def formula(self):

        localctx = ModelParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 38
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 39
                self.constList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LookupContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.LookupContext, self).__init__(parent, invokingState)
            self.parser = parser

        def varname(self):
            return self.getTypedRuleContext(ModelParser.VarnameContext,0)


        def lookupPoint(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.LookupPointContext)
            else:
                return self.getTypedRuleContext(ModelParser.LookupPointContext,i)


        def lookupList(self):
            return self.getTypedRuleContext(ModelParser.LookupListContext,0)


        def getRuleIndex(self):
            return ModelParser.RULE_lookup

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitLookup(self)
            else:
                return visitor.visitChildren(self)




    def lookup(self):

        localctx = ModelParser.LookupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lookup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.varname()
            self.state = 43
            self.match(ModelParser.T__0)
            self.state = 44
            self.match(ModelParser.T__1)
            self.state = 45
            self.lookupPoint()
            self.state = 46
            self.match(ModelParser.Minus)
            self.state = 47
            self.lookupPoint()
            self.state = 48
            self.match(ModelParser.T__2)
            self.state = 49
            self.match(ModelParser.T__3)
            self.state = 50
            self.lookupList()
            self.state = 51
            self.match(ModelParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LookupListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.LookupListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def lookupPoint(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.LookupPointContext)
            else:
                return self.getTypedRuleContext(ModelParser.LookupPointContext,i)


        def getRuleIndex(self):
            return ModelParser.RULE_lookupList

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitLookupList(self)
            else:
                return visitor.visitChildren(self)




    def lookupList(self):

        localctx = ModelParser.LookupListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lookupList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.lookupPoint()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ModelParser.T__3:
                self.state = 54
                self.match(ModelParser.T__3)
                self.state = 55
                self.lookupPoint()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubscriptListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.SubscriptListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Id(self, i=None):
            if i is None:
                return self.getTokens(ModelParser.Id)
            else:
                return self.getToken(ModelParser.Id, i)

        def getRuleIndex(self):
            return ModelParser.RULE_subscriptList

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitSubscriptList(self)
            else:
                return visitor.visitChildren(self)




    def subscriptList(self):

        localctx = ModelParser.SubscriptListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_subscriptList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ModelParser.T__1)
            self.state = 62
            self.match(ModelParser.Id)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ModelParser.T__3:
                self.state = 63
                self.match(ModelParser.T__3)
                self.state = 64
                self.match(ModelParser.Id)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(ModelParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.ConstListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Const(self, i=None):
            if i is None:
                return self.getTokens(ModelParser.Const)
            else:
                return self.getToken(ModelParser.Const, i)

        def getRuleIndex(self):
            return ModelParser.RULE_constList

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitConstList(self)
            else:
                return visitor.visitChildren(self)




    def constList(self):

        localctx = ModelParser.ConstListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_constList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ModelParser.Const)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ModelParser.T__3:
                self.state = 73
                self.match(ModelParser.T__3)
                self.state = 74
                self.match(ModelParser.Const)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LookupPointContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.LookupPointContext, self).__init__(parent, invokingState)
            self.parser = parser

        def Const(self, i=None):
            if i is None:
                return self.getTokens(ModelParser.Const)
            else:
                return self.getToken(ModelParser.Const, i)

        def getRuleIndex(self):
            return ModelParser.RULE_lookupPoint

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitLookupPoint(self)
            else:
                return visitor.visitChildren(self)




    def lookupPoint(self):

        localctx = ModelParser.LookupPointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lookupPoint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ModelParser.T__0)
            self.state = 81
            self.match(ModelParser.Const)
            self.state = 82
            self.match(ModelParser.T__3)
            self.state = 83
            self.match(ModelParser.Const)
            self.state = 84
            self.match(ModelParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.RootContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ModelParser.ExprContext,0)


        def getRuleIndex(self):
            return ModelParser.RULE_root

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = ModelParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ModelParser.RULE_expr

     
        def copyFrom(self, ctx):
            super(ModelParser.ExprContext, self).copyFrom(ctx)


    class CallContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.CallContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Id(self):
            return self.getToken(ModelParser.Id, 0)
        def exprList(self):
            return self.getTypedRuleContext(ModelParser.ExprListContext,0)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.OrContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.ExprContext)
            else:
                return self.getTypedRuleContext(ModelParser.ExprContext,i)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class KeywordContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.KeywordContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Keyword(self):
            return self.getToken(ModelParser.Keyword, 0)

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitKeyword(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.MulDivContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.ExprContext)
            else:
                return self.getTypedRuleContext(ModelParser.ExprContext,i)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.AddSubContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.ExprContext)
            else:
                return self.getTypedRuleContext(ModelParser.ExprContext,i)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.VarContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Id(self):
            return self.getToken(ModelParser.Id, 0)
        def subscriptList(self):
            return self.getTypedRuleContext(ModelParser.SubscriptListContext,0)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.ParensContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ModelParser.ExprContext,0)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class ConstContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.ConstContext, self).__init__(parser)
            self.copyFrom(ctx)

        def Const(self):
            return self.getToken(ModelParser.Const, 0)

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)


    class RelationalContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.RelationalContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.ExprContext)
            else:
                return self.getTypedRuleContext(ModelParser.ExprContext,i)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)


    class NotContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.NotContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ModelParser.ExprContext,0)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class NegativeContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.NegativeContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ModelParser.ExprContext,0)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitNegative(self)
            else:
                return visitor.visitChildren(self)


    class PositiveContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.PositiveContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ModelParser.ExprContext,0)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitPositive(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.AndContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.ExprContext)
            else:
                return self.getTypedRuleContext(ModelParser.ExprContext,i)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class EqualityContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.EqualityContext, self).__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.ExprContext)
            else:
                return self.getTypedRuleContext(ModelParser.ExprContext,i)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)


    class PowerContext(ExprContext):

        def __init__(self, parser, ctx): # actually a ModelParser.ExprContext)
            super(ModelParser.PowerContext, self).__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.ExprContext)
            else:
                return self.getTypedRuleContext(ModelParser.ExprContext,i)


        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ModelParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = ModelParser.NotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 89
                self.match(ModelParser.T__5)
                self.state = 90
                self.expr(14)
                pass

            elif la_ == 2:
                localctx = ModelParser.NegativeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.match(ModelParser.Minus)
                self.state = 92
                self.expr(13)
                pass

            elif la_ == 3:
                localctx = ModelParser.PositiveContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(ModelParser.Plus)
                self.state = 94
                self.expr(12)
                pass

            elif la_ == 4:
                localctx = ModelParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(ModelParser.Id)
                self.state = 96
                self.match(ModelParser.T__0)
                self.state = 98
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ModelParser.T__0) | (1 << ModelParser.T__5) | (1 << ModelParser.Plus) | (1 << ModelParser.Minus) | (1 << ModelParser.Id) | (1 << ModelParser.Const) | (1 << ModelParser.Keyword))) != 0):
                    self.state = 97
                    self.exprList()


                self.state = 100
                self.match(ModelParser.T__4)
                pass

            elif la_ == 5:
                localctx = ModelParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self.match(ModelParser.Id)
                self.state = 103
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 102
                    self.subscriptList()


                pass

            elif la_ == 6:
                localctx = ModelParser.ConstContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                self.match(ModelParser.Const)
                pass

            elif la_ == 7:
                localctx = ModelParser.KeywordContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.match(ModelParser.Keyword)
                pass

            elif la_ == 8:
                localctx = ModelParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(ModelParser.T__0)
                self.state = 108
                self.expr(0)
                self.state = 109
                self.match(ModelParser.T__4)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 134
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = ModelParser.PowerContext(self, ModelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 113
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 114
                        self.match(ModelParser.T__6)
                        self.state = 115
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = ModelParser.MulDivContext(self, ModelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 116
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 117
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ModelParser.Star or _la==ModelParser.Div):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 118
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = ModelParser.AddSubContext(self, ModelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 119
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 120
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ModelParser.Plus or _la==ModelParser.Minus):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 121
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = ModelParser.RelationalContext(self, ModelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 123
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ModelParser.Less) | (1 << ModelParser.LessEqual) | (1 << ModelParser.Greater) | (1 << ModelParser.GreaterEqual))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 124
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = ModelParser.EqualityContext(self, ModelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 126
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ModelParser.Equal or _la==ModelParser.NotEqual):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 127
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = ModelParser.AndContext(self, ModelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 129
                        self.match(ModelParser.T__7)
                        self.state = 130
                        self.expr(7)
                        pass

                    elif la_ == 7:
                        localctx = ModelParser.OrContext(self, ModelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 131
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 132
                        self.match(ModelParser.T__8)
                        self.state = 133
                        self.expr(6)
                        pass

             
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ExprListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ModelParser.ExprListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ModelParser.ExprContext)
            else:
                return self.getTypedRuleContext(ModelParser.ExprContext,i)


        def getRuleIndex(self):
            return ModelParser.RULE_exprList

        def accept(self, visitor):
            if isinstance( visitor, ModelVisitor ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = ModelParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.expr(0)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ModelParser.T__3:
                self.state = 140
                self.match(ModelParser.T__3)
                self.state = 141
                self.expr(0)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 5)
         



