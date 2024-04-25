# Generated from ZenithGrammar.g4 by ANTLR 4.13.0
import sys
from antlr4 import *

from compiler.IntermediateCode import IntermediateCode

if "." in __name__:
    from .ZenithGrammarParser import ZenithGrammarParser
else:
    from ZenithGrammarParser import ZenithGrammarParser


# This class defines a complete listener for a parse tree produced by ZenithGrammarParser.
class ZenithGrammarListener(ParseTreeListener):
    def __init__(self):
        self.intermediate_code = IntermediateCode()
        self.variable_list = []

    def get_output(self):
        return self.intermediate_code.get_intermediate_code()

    def add_variable_to_list(self, named_variable):
        self.variable_list.append(named_variable)

    def does_variable_exist(self, named_variable):
        return named_variable in self.variable_list

    def update_variable_in_list(self, named_variable, value):
        for variable in self.variable_list:
            if variable["value"] == named_variable:
                variable['value'] = value
                return
        self.missing_variable_error(named_variable)

    def missing_variable_error(self, identifier):
        print(
            f"Compiletime error: Variable {identifier} not defined. Did you forget to declare variable {identifier}?",
            file=sys.stderr)
        sys.exit(1)

    # Enter a parse tree produced by ZenithGrammarParser#program.
    def enterProgram(self, ctx: ZenithGrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#program.
    def exitProgram(self, ctx: ZenithGrammarParser.ProgramContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#block.
    def enterBlock(self, ctx: ZenithGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#block.
    def exitBlock(self, ctx: ZenithGrammarParser.BlockContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#atomic_block.
    def enterAtomic_block(self, ctx: ZenithGrammarParser.Atomic_blockContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#atomic_block.
    def exitAtomic_block(self, ctx: ZenithGrammarParser.Atomic_blockContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#integerDeclaration.
    def enterIntegerDeclaration(self, ctx: ZenithGrammarParser.IntegerDeclarationContext):
        var_name = ctx.VARIABLE_IDENTIFIER().getText()
        self.add_variable_to_list(var_name)
        declaration_code = f"{var_name}"
        if ctx.ASSIGNMENT_OPERATOR():
            value = ctx.num_expr().getText()
            declaration_code += f" = {value}"
        else:
            declaration_code += ""
        self.intermediate_code.add_intermediate_output(declaration_code)

    # Exit a parse tree produced by ZenithGrammarParser#integerDeclaration.
    def exitIntegerDeclaration(self, ctx: ZenithGrammarParser.IntegerDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#booleanDeclaration.
    def enterBooleanDeclaration(self, ctx: ZenithGrammarParser.BooleanDeclarationContext):
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        self.add_variable_to_list(variable_name)
        value = None
        if ctx.bool_expr():
            value = ctx.bool_expr().getText()
        elif ctx.ternary_expr():
            value = ctx.ternary_expr().getText()

        # Add the boolean declaration to the intermediate code
        declaration_code = f" {variable_name}"
        if value:
            declaration_code += f" = {value}"
        self.intermediate_code.add_intermediate_output(declaration_code)
        pass

    # Exit a parse tree produced by ZenithGrammarParser#booleanDeclaration.
    def exitBooleanDeclaration(self, ctx: ZenithGrammarParser.BooleanDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#stringDeclaration.
    def enterStringDeclaration(self, ctx: ZenithGrammarParser.StringDeclarationContext):
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        self.add_variable_to_list(variable_name)
        value = None
        if ctx.VALID_STRING():
            value = ctx.VALID_STRING().getText()
        elif ctx.ternary_expr():
            value = ctx.ternary_expr().getText()

        # Add the string declaration to the intermediate code
        declaration_code = f" {variable_name}"
        if value:
            declaration_code += f" = {value}"
        self.intermediate_code.add_intermediate_output(declaration_code)
        pass

    # Exit a parse tree produced by ZenithGrammarParser#stringDeclaration.
    def exitStringDeclaration(self, ctx: ZenithGrammarParser.StringDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#floatDeclaration.
    def enterFloatDeclaration(self, ctx: ZenithGrammarParser.FloatDeclarationContext):
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        self.add_variable_to_list(variable_name)
        value = None
        if ctx.DECIMAL_VALUE():
            value = ctx.DECIMAL_VALUE().getText()
        elif ctx.ternary_expr():
            value = ctx.ternary_expr().getText()

        # Add the float declaration to the intermediate code
        declaration_code = f" {variable_name}"
        if value:
            declaration_code += f" = {value}"
        self.intermediate_code.add_intermediate_output(declaration_code)
        pass

    # Exit a parse tree produced by ZenithGrammarParser#floatDeclaration.
    def exitFloatDeclaration(self, ctx: ZenithGrammarParser.FloatDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#doubleDeclaration.
    def enterDoubleDeclaration(self, ctx: ZenithGrammarParser.DoubleDeclarationContext):
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        self.add_variable_to_list(variable_name)
        value = None
        if ctx.DECIMAL_VALUE():
            value = ctx.DECIMAL_VALUE().getText()
        elif ctx.ternary_expr():
            value = ctx.ternary_expr().getText()

        # Add the double declaration to the intermediate code
        declaration_code = f" {variable_name}"
        if value:
            declaration_code += f" = {value}"
        self.intermediate_code.add_intermediate_output(declaration_code)
        pass

    # Exit a parse tree produced by ZenithGrammarParser#doubleDeclaration.
    def exitDoubleDeclaration(self, ctx: ZenithGrammarParser.DoubleDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#emptyDeclaration.
    def enterEmptyDeclaration(self, ctx: ZenithGrammarParser.EmptyDeclarationContext):
        self.intermediate_code.add_intermediate_output("{}")
        pass

    # Exit a parse tree produced by ZenithGrammarParser#emptyDeclaration.
    def exitEmptyDeclaration(self, ctx: ZenithGrammarParser.EmptyDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#command.
    def enterCommand(self, ctx: ZenithGrammarParser.CommandContext):
        command = ctx.getText()
        self.intermediate_code.add_intermediate_output(command)
        pass

    # Exit a parse tree produced by ZenithGrammarParser#command.
    def exitCommand(self, ctx: ZenithGrammarParser.CommandContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#integerAssignment.
    def enterIntegerAssignment(self, ctx: ZenithGrammarParser.IntegerAssignmentContext):
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        value = ctx.num_expr().getText()
        self.update_variable_in_list(variable_name, value)

        # Add the integer assignment to the intermediate code
        # assignment_code = f"{variable_name}"
        # if value:
        #     assignment_code += f" = {value}"
        # self.intermediate_code.add_intermediate_output(assignment_code)
        pass

    # Exit a parse tree produced by ZenithGrammarParser#integerAssignment.
    def exitIntegerAssignment(self, ctx: ZenithGrammarParser.IntegerAssignmentContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#booleanAssignment.
    def enterBooleanAssignment(self, ctx: ZenithGrammarParser.BooleanAssignmentContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#booleanAssignment.
    def exitBooleanAssignment(self, ctx: ZenithGrammarParser.BooleanAssignmentContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#ternaryAssignment.
    def enterTernaryAssignment(self, ctx: ZenithGrammarParser.TernaryAssignmentContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#ternaryAssignment.
    def exitTernaryAssignment(self, ctx: ZenithGrammarParser.TernaryAssignmentContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#exprs.
    def enterExprs(self, ctx: ZenithGrammarParser.ExprsContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#exprs.
    def exitExprs(self, ctx: ZenithGrammarParser.ExprsContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#booleanExpressionInBrackets.
    def enterBooleanExpressionInBrackets(self, ctx: ZenithGrammarParser.BooleanExpressionInBracketsContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#booleanExpressionInBrackets.
    def exitBooleanExpressionInBrackets(self, ctx: ZenithGrammarParser.BooleanExpressionInBracketsContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#booleanIdentifierOnlyExpression.
    def enterBooleanIdentifierOnlyExpression(self, ctx: ZenithGrammarParser.BooleanIdentifierOnlyExpressionContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#booleanIdentifierOnlyExpression.
    def exitBooleanIdentifierOnlyExpression(self, ctx: ZenithGrammarParser.BooleanIdentifierOnlyExpressionContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#primitiveBooleanValuesOnly.
    def enterPrimitiveBooleanValuesOnly(self, ctx: ZenithGrammarParser.PrimitiveBooleanValuesOnlyContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#primitiveBooleanValuesOnly.
    def exitPrimitiveBooleanValuesOnly(self, ctx: ZenithGrammarParser.PrimitiveBooleanValuesOnlyContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#booleanLogicalExpression.
    def enterBooleanLogicalExpression(self, ctx: ZenithGrammarParser.BooleanLogicalExpressionContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#booleanLogicalExpression.
    def exitBooleanLogicalExpression(self, ctx: ZenithGrammarParser.BooleanLogicalExpressionContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#booleanComparisonExpression.
    def enterBooleanComparisonExpression(self, ctx: ZenithGrammarParser.BooleanComparisonExpressionContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#booleanComparisonExpression.
    def exitBooleanComparisonExpression(self, ctx: ZenithGrammarParser.BooleanComparisonExpressionContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#numberComparisonExpression.
    def enterNumberComparisonExpression(self, ctx: ZenithGrammarParser.NumberComparisonExpressionContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#numberComparisonExpression.
    def exitNumberComparisonExpression(self, ctx: ZenithGrammarParser.NumberComparisonExpressionContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#num_expr.
    def enterNum_expr(self, ctx: ZenithGrammarParser.Num_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#num_expr.
    def exitNum_expr(self, ctx: ZenithGrammarParser.Num_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#add_sub_expr.
    def enterAdd_sub_expr(self, ctx: ZenithGrammarParser.Add_sub_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#add_sub_expr.
    def exitAdd_sub_expr(self, ctx: ZenithGrammarParser.Add_sub_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#term_expr.
    def enterTerm_expr(self, ctx: ZenithGrammarParser.Term_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#term_expr.
    def exitTerm_expr(self, ctx: ZenithGrammarParser.Term_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#bracket_expr.
    def enterBracket_expr(self, ctx: ZenithGrammarParser.Bracket_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#bracket_expr.
    def exitBracket_expr(self, ctx: ZenithGrammarParser.Bracket_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#cond_expr.
    def enterCond_expr(self, ctx: ZenithGrammarParser.Cond_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#cond_expr.
    def exitCond_expr(self, ctx: ZenithGrammarParser.Cond_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#if_expr.
    def enterIf_expr(self, ctx: ZenithGrammarParser.If_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#if_expr.
    def exitIf_expr(self, ctx: ZenithGrammarParser.If_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#else_if_expr.
    def enterElse_if_expr(self, ctx: ZenithGrammarParser.Else_if_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#else_if_expr.
    def exitElse_if_expr(self, ctx: ZenithGrammarParser.Else_if_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#else_expr.
    def enterElse_expr(self, ctx: ZenithGrammarParser.Else_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#else_expr.
    def exitElse_expr(self, ctx: ZenithGrammarParser.Else_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#while_expr.
    def enterWhile_expr(self, ctx: ZenithGrammarParser.While_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#while_expr.
    def exitWhile_expr(self, ctx: ZenithGrammarParser.While_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#for_enhanced.
    def enterFor_enhanced(self, ctx: ZenithGrammarParser.For_enhancedContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#for_enhanced.
    def exitFor_enhanced(self, ctx: ZenithGrammarParser.For_enhancedContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#rangeVal.
    def enterRangeVal(self, ctx: ZenithGrammarParser.RangeValContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#rangeVal.
    def exitRangeVal(self, ctx: ZenithGrammarParser.RangeValContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#for_loop.
    def enterFor_loop(self, ctx: ZenithGrammarParser.For_loopContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#for_loop.
    def exitFor_loop(self, ctx: ZenithGrammarParser.For_loopContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#variable_change_part.
    def enterVariable_change_part(self, ctx: ZenithGrammarParser.Variable_change_partContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#variable_change_part.
    def exitVariable_change_part(self, ctx: ZenithGrammarParser.Variable_change_partContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#decrement_expression.
    def enterDecrement_expression(self, ctx: ZenithGrammarParser.Decrement_expressionContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#decrement_expression.
    def exitDecrement_expression(self, ctx: ZenithGrammarParser.Decrement_expressionContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#increment_expression.
    def enterIncrement_expression(self, ctx: ZenithGrammarParser.Increment_expressionContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#increment_expression.
    def exitIncrement_expression(self, ctx: ZenithGrammarParser.Increment_expressionContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#ternary_expr.
    def enterTernary_expr(self, ctx: ZenithGrammarParser.Ternary_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#ternary_expr.
    def exitTernary_expr(self, ctx: ZenithGrammarParser.Ternary_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#value.
    def enterValue(self, ctx: ZenithGrammarParser.ValueContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#value.
    def exitValue(self, ctx: ZenithGrammarParser.ValueContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#print.
    def enterPrint(self, ctx: ZenithGrammarParser.PrintContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#print.
    def exitPrint(self, ctx: ZenithGrammarParser.PrintContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#print_parameters.
    def enterPrint_parameters(self, ctx: ZenithGrammarParser.Print_parametersContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#print_parameters.
    def exitPrint_parameters(self, ctx: ZenithGrammarParser.Print_parametersContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#primitive_type.
    def enterPrimitive_type(self, ctx: ZenithGrammarParser.Primitive_typeContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#primitive_type.
    def exitPrimitive_type(self, ctx: ZenithGrammarParser.Primitive_typeContext):
        pass


del ZenithGrammarParser