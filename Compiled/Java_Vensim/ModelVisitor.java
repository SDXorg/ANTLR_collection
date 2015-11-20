// Generated from Model.g4 by ANTLR 4.5
import org.antlr.v4.runtime.misc.NotNull;
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link ModelParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface ModelVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link ModelParser#model}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitModel(ModelParser.ModelContext ctx);
	/**
	 * Visit a parse tree produced by {@link ModelParser#equation}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEquation(ModelParser.EquationContext ctx);
	/**
	 * Visit a parse tree produced by {@link ModelParser#lhs}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLhs(ModelParser.LhsContext ctx);
	/**
	 * Visit a parse tree produced by {@link ModelParser#subscriptList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubscriptList(ModelParser.SubscriptListContext ctx);
	/**
	 * Visit a parse tree produced by {@link ModelParser#constList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConstList(ModelParser.ConstListContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Call}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCall(ModelParser.CallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Or}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOr(ModelParser.OrContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Keyword}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitKeyword(ModelParser.KeywordContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMulDiv(ModelParser.MulDivContext ctx);
	/**
	 * Visit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddSub(ModelParser.AddSubContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Var}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar(ModelParser.VarContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Parens}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParens(ModelParser.ParensContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Const}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitConst(ModelParser.ConstContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Relational}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelational(ModelParser.RelationalContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LookupCall}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLookupCall(ModelParser.LookupCallContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Not}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNot(ModelParser.NotContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Negative}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNegative(ModelParser.NegativeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Positive}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPositive(ModelParser.PositiveContext ctx);
	/**
	 * Visit a parse tree produced by the {@code And}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAnd(ModelParser.AndContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Equality}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEquality(ModelParser.EqualityContext ctx);
	/**
	 * Visit a parse tree produced by the {@code LookupArg}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLookupArg(ModelParser.LookupArgContext ctx);
	/**
	 * Visit a parse tree produced by the {@code Power}
	 * labeled alternative in {@link ModelParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPower(ModelParser.PowerContext ctx);
	/**
	 * Visit a parse tree produced by {@link ModelParser#exprList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprList(ModelParser.ExprListContext ctx);
	/**
	 * Visit a parse tree produced by {@link ModelParser#lookup}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLookup(ModelParser.LookupContext ctx);
	/**
	 * Visit a parse tree produced by {@link ModelParser#lookupRange}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLookupRange(ModelParser.LookupRangeContext ctx);
	/**
	 * Visit a parse tree produced by {@link ModelParser#lookupPointList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLookupPointList(ModelParser.LookupPointListContext ctx);
	/**
	 * Visit a parse tree produced by {@link ModelParser#lookupPoint}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLookupPoint(ModelParser.LookupPointContext ctx);
}