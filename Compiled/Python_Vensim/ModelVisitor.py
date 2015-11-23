# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ModelParser.

class ModelVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ModelParser#model.
    def visitModel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#equation.
    def visitEquation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#lhs.
    def visitLhs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#subscriptList.
    def visitSubscriptList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#constList.
    def visitConstList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Call.
    def visitCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Or.
    def visitOr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Keyword.
    def visitKeyword(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#MulDiv.
    def visitMulDiv(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#AddSub.
    def visitAddSub(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Var.
    def visitVar(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Parens.
    def visitParens(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Const.
    def visitConst(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Relational.
    def visitRelational(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#LookupCall.
    def visitLookupCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Not.
    def visitNot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Negative.
    def visitNegative(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Positive.
    def visitPositive(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#And.
    def visitAnd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Equality.
    def visitEquality(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#LookupArg.
    def visitLookupArg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#Power.
    def visitPower(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#exprList.
    def visitExprList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#lookup.
    def visitLookup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#lookupRange.
    def visitLookupRange(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#lookupPointList.
    def visitLookupPointList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModelParser#lookupPoint.
    def visitLookupPoint(self, ctx):
        return self.visitChildren(ctx)


