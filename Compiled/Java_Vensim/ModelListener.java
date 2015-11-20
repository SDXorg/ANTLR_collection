// Generated from Model.g4 by ANTLR 4.5
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ModelParser}.
 */
public interface ModelListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ModelParser#model}.
	 * @param ctx the parse tree
	 */
	void enterModel(ModelParser.ModelContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#model}.
	 * @param ctx the parse tree
	 */
	void exitModel(ModelParser.ModelContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#equation}.
	 * @param ctx the parse tree
	 */
	void enterEquation(ModelParser.EquationContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#equation}.
	 * @param ctx the parse tree
	 */
	void exitEquation(ModelParser.EquationContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#lhs}.
	 * @param ctx the parse tree
	 */
	void enterLhs(ModelParser.LhsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#lhs}.
	 * @param ctx the parse tree
	 */
	void exitLhs(ModelParser.LhsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#subscriptList}.
	 * @param ctx the parse tree
	 */
	void enterSubscriptList(ModelParser.SubscriptListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#subscriptList}.
	 * @param ctx the parse tree
	 */
	void exitSubscriptList(ModelParser.SubscriptListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#constList}.
	 * @param ctx the parse tree
	 */
	void enterConstList(ModelParser.ConstListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#constList}.
	 * @param ctx the parse tree
	 */
	void exitConstList(ModelParser.ConstListContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Call}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterCall(ModelParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Call}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitCall(ModelParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Or}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOr(ModelParser.OrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Or}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOr(ModelParser.OrContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Keyword}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterKeyword(ModelParser.KeywordContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Keyword}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitKeyword(ModelParser.KeywordContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(ModelParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(ModelParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(ModelParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(ModelParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Var}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVar(ModelParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Var}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVar(ModelParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParens(ModelParser.ParensContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParens(ModelParser.ParensContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Const}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterConst(ModelParser.ConstContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Const}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitConst(ModelParser.ConstContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Relational}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterRelational(ModelParser.RelationalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Relational}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitRelational(ModelParser.RelationalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LookupCall}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLookupCall(ModelParser.LookupCallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LookupCall}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLookupCall(ModelParser.LookupCallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Not}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNot(ModelParser.NotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Not}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNot(ModelParser.NotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Negative}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNegative(ModelParser.NegativeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Negative}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNegative(ModelParser.NegativeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Positive}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPositive(ModelParser.PositiveContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Positive}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPositive(ModelParser.PositiveContext ctx);
	/**
	 * Enter a parse tree produced by the {@code And}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAnd(ModelParser.AndContext ctx);
	/**
	 * Exit a parse tree produced by the {@code And}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAnd(ModelParser.AndContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Equality}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterEquality(ModelParser.EqualityContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Equality}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitEquality(ModelParser.EqualityContext ctx);
	/**
	 * Enter a parse tree produced by the {@code LookupArg}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLookupArg(ModelParser.LookupArgContext ctx);
	/**
	 * Exit a parse tree produced by the {@code LookupArg}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLookupArg(ModelParser.LookupArgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Power}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPower(ModelParser.PowerContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Power}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPower(ModelParser.PowerContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#exprList}.
	 * @param ctx the parse tree
	 */
	void enterExprList(ModelParser.ExprListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#exprList}.
	 * @param ctx the parse tree
	 */
	void exitExprList(ModelParser.ExprListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#lookup}.
	 * @param ctx the parse tree
	 */
	void enterLookup(ModelParser.LookupContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#lookup}.
	 * @param ctx the parse tree
	 */
	void exitLookup(ModelParser.LookupContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#lookupRange}.
	 * @param ctx the parse tree
	 */
	void enterLookupRange(ModelParser.LookupRangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#lookupRange}.
	 * @param ctx the parse tree
	 */
	void exitLookupRange(ModelParser.LookupRangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#lookupPointList}.
	 * @param ctx the parse tree
	 */
	void enterLookupPointList(ModelParser.LookupPointListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#lookupPointList}.
	 * @param ctx the parse tree
	 */
	void exitLookupPointList(ModelParser.LookupPointListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ModelParser#lookupPoint}.
	 * @param ctx the parse tree
	 */
	void enterLookupPoint(ModelParser.LookupPointContext ctx);
	/**
	 * Exit a parse tree produced by {@link ModelParser#lookupPoint}.
	 * @param ctx the parse tree
	 */
	void exitLookupPoint(ModelParser.LookupPointContext ctx);
}