# Generated from ZenithGrammar.g4 by ANTLR 4.13.0
import sys
import re
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
        self.type_list = {}
        self.indent_list = []

    def indentOpp(self):
        # print("listop regular", self.indent_list)
        if len(self.indent_list) > 0:
            last_element = self.indent_list.pop()
            last_element -= 1
            if last_element > 0:
                self.indent_list.append(last_element)
            else:
                self.intermediate_code.add_intermediate_output("}")
                while len(self.indent_list) > 0 and self.indent_list[-1] == 1:
                    current = self.indent_list.pop()
                    self.intermediate_code.add_intermediate_output("}")
                if len(self.indent_list) > 0:
                    current = self.indent_list.pop()
                    current -=1
                    self.indent_list.append(current)

    def indentOppCond(self):
        # print("listop cond", self.indent_list)
        if len(self.indent_list) > 0:
            last_element = self.indent_list.pop()
            if last_element > 0:
                self.indent_list.append(last_element)
            else:
                self.intermediate_code.add_intermediate_output("}")
                while len(self.indent_list) > 0 and self.indent_list[-1] == 1:
                    current = self.indent_list.pop()
                    self.intermediate_code.add_intermediate_output("}")
                if len(self.indent_list) > 0:
                    current = self.indent_list.pop()
                    current -=1
                    self.indent_list.append(current)

    def get_output(self):
        return self.intermediate_code.get_intermediate_code()

    def add_variable_to_list(self, named_variable):
        self.variable_list.append(named_variable)

    def add_variable_type_to_list(self, type):
        self.type_list.update(type)

    def does_variable_exist(self, named_variable):
        return named_variable in self.variable_list

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
        self.add_variable_type_to_list({var_name: 'int'})
        declaration_code = f"{var_name}"
        value = None
        if ctx.num_expr():
            value = ctx.num_expr().getText()
        elif ctx.ternary_expr():
            value = self.enterTernary_expr(ctx.ternary_expr())
        else:
            declaration_code += ""
       
        if value:
            int_value = f"int({value})"
            declaration_code += f" = {int_value}"
        elif not ctx.ternary_expr() :
            declaration_code += f" = 0"
        # print("value from integer declaration",declaration_code)
        self.intermediate_code.add_intermediate_output(declaration_code)
        self.indentOpp()

    # Exit a parse tree produced by ZenithGrammarParser#integerDeclaration.
    def exitIntegerDeclaration(self, ctx: ZenithGrammarParser.IntegerDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#booleanDeclaration.
    def enterBooleanDeclaration(self, ctx: ZenithGrammarParser.BooleanDeclarationContext):
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        self.add_variable_to_list(variable_name)
        self.add_variable_type_to_list({variable_name: 'boolean'})
        declaration_code = f"{variable_name}"
        value = None
        if ctx.bool_expr():
            value = ctx.bool_expr().getText()
        elif ctx.ternary_expr():
            value = self.enterTernary_expr(ctx.ternary_expr())
        # Add the boolean declaration to the intermediate code
        if value:
            declaration_code += f" = {value}"
        else:
            declaration_code += f" = True"
        self.intermediate_code.add_intermediate_output(declaration_code)
        self.indentOpp()
        pass

    # Exit a parse tree produced by ZenithGrammarParser#booleanDeclaration.
    def exitBooleanDeclaration(self, ctx: ZenithGrammarParser.BooleanDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#stringDeclaration.
    def enterStringDeclaration(self, ctx: ZenithGrammarParser.StringDeclarationContext):
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        self.add_variable_to_list(variable_name)
        self.add_variable_type_to_list({variable_name: 'string'})
        declaration_code = f"{variable_name}"
        value = None
        if ctx.VALID_STRING():
            value = ctx.VALID_STRING().getText()
        elif ctx.ternary_expr():
            value = self.enterTernary_expr(ctx.ternary_expr())
        else:
            declaration_code += ""

        # Add the string declaration to the intermediate code
        if value:
            declaration_code += f" = {value}"
        else :
            declaration_code += f" = \"\""
        self.intermediate_code.add_intermediate_output(declaration_code)
        self.indentOpp()

        pass

    # Exit a parse tree produced by ZenithGrammarParser#stringDeclaration.
    def exitStringDeclaration(self, ctx: ZenithGrammarParser.StringDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#floatDeclaration.
    def enterFloatDeclaration(self, ctx: ZenithGrammarParser.FloatDeclarationContext):
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        self.add_variable_to_list(variable_name)
        self.add_variable_type_to_list({variable_name: 'float'})
        declaration_code = f"{variable_name}"
        value = None
        if ctx.num_expr():
            value = ctx.num_expr().getText()
        elif ctx.ternary_expr():
            value = ctx.ternary_expr().getText()
        else:
            declaration_code += ""

        # Add the float declaration to the intermediate code
        if value:
            float_value = f"{round(float(value), 4)}"
            declaration_code += f" = {float_value}"
        else:
            declaration_code += f" = 0.0"
        self.intermediate_code.add_intermediate_output(declaration_code)
        self.indentOpp()

        pass

    # Exit a parse tree produced by ZenithGrammarParser#floatDeclaration.
    def exitFloatDeclaration(self, ctx: ZenithGrammarParser.FloatDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#doubleDeclaration.
    def enterDoubleDeclaration(self, ctx: ZenithGrammarParser.DoubleDeclarationContext):
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        self.add_variable_to_list(variable_name)
        self.add_variable_type_to_list({variable_name: 'double'})
        declaration_code = f"{variable_name}"
        value = None
        if ctx.num_expr():
            value = ctx.num_expr().getText()
        elif ctx.ternary_expr():
            value = ctx.ternary_expr().getText()
        else:
            declaration_code += ""

        # Add the double declaration to the intermediate code
        if value:
            declaration_code += f" = {value}"
        else:
            declaration_code += f" = 0.0"
        self.intermediate_code.add_intermediate_output(declaration_code)
        self.indentOpp()

        pass

    # Exit a parse tree produced by ZenithGrammarParser#doubleDeclaration.
    def exitDoubleDeclaration(self, ctx: ZenithGrammarParser.DoubleDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#emptyDeclaration.
    def enterEmptyDeclaration(self, ctx: ZenithGrammarParser.EmptyDeclarationContext):
        self.intermediate_code.add_intermediate_output("{}")
        self.indentOpp()

        pass

    # Exit a parse tree produced by ZenithGrammarParser#emptyDeclaration.
    def exitEmptyDeclaration(self, ctx: ZenithGrammarParser.EmptyDeclarationContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#command.
    def enterCommand(self, ctx: ZenithGrammarParser.CommandContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#command.
    def exitCommand(self, ctx: ZenithGrammarParser.CommandContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#integerAssignment.
    def enterIntegerAssignment(self, ctx: ZenithGrammarParser.IntegerAssignmentContext):
        # print("Comes to the integer assignment")
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        check = self.does_variable_exist(variable_name)
        declaration_code = f"{variable_name}"

        if check:
            if self.type_list[variable_name] == 'int' or self.type_list[variable_name] == 'float' or self.type_list[variable_name] == 'double':
                if ctx.num_expr():
                    value = self.enterNum_expr(ctx.num_expr())
                    if self.type_list[variable_name] == 'int':
                        int_value = f"int({value})"
                        declaration_code += f" = {int_value}"
                    else:
                        declaration_code += f" = {value}"
                    # print("comes to integer assignment", declaration_code)
                    self.intermediate_code.add_intermediate_output(declaration_code)
                    self.indentOpp()

                    # print("comes to integer assignment", declaration_code)
                    # print("comes to integer assignment", ctx.num_expr().getText())

    # Exit a parse tree produced by ZenithGrammarParser#integerAssignment.
    def exitIntegerAssignment(self, ctx: ZenithGrammarParser.IntegerAssignmentContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#booleanAssignment.
    def enterBooleanAssignment(self, ctx: ZenithGrammarParser.BooleanAssignmentContext):
        # print("bool assignment", ctx.getText(), ctx.getChildCount())
        variable_name = ctx.VARIABLE_IDENTIFIER().getText()
        # print("bool variable", variable_name)
        check = self.does_variable_exist(variable_name)
        declaration_code = f"{variable_name}"
        if check:
            # print("check", check)
            if self.type_list[variable_name] == 'boolean':
                if ctx.bool_expr():
                    print("works??", ctx.bool_expr().getText())
                    value = self.enterBool_expr(ctx.bool_expr())
                    declaration_code += f" = {value}"
                    self.intermediate_code.add_intermediate_output(declaration_code)
                    self.indentOpp()

    # Exit a parse tree produced by ZenithGrammarParser#booleanAssignment.
    def exitBooleanAssignment(self, ctx: ZenithGrammarParser.BooleanAssignmentContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#bool_expr.
    def enterBool_expr(self, ctx: ZenithGrammarParser.Bool_exprContext):
        # print("bool expr", ctx.getText())
        if ctx.VARIABLE_IDENTIFIER():
            variable_name = ctx.VARIABLE_IDENTIFIER().getText()
            # print(variable_name)
            check = self.does_variable_exist(variable_name)
            if check:
                if self.type_list[variable_name] == 'boolean':
                    declaration_code = f"{variable_name}"
                    if ctx.bool_expr():
                        value = self.enterBool_expr(ctx.bool_expr())
                        declaration_code += f" = {value}"
                        # print("enterNum declaration - ", declaration_code)
                        return declaration_code
                        # self.intermediate_code.add_intermediate_output(declaration_code)
        else:
            if ctx.bool_computation_expr():
                return self.enterBool_computation_expr(ctx.bool_computation_expr())

        pass

    # Exit a parse tree produced by ZenithGrammarParser#bool_expr.
    def exitBool_expr(self, ctx: ZenithGrammarParser.Bool_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#ternaryAssignment.
    def enterTernaryAssignment(self, ctx: ZenithGrammarParser.TernaryAssignmentContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#ternaryAssignment.
    def exitTernaryAssignment(self, ctx: ZenithGrammarParser.TernaryAssignmentContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#exprs.
    def enterExprs(self, ctx: ZenithGrammarParser.ExprsContext):
        return ctx.getText()
        # print("exprs", ctx.num_expr().getText()) 
        # if ctx.num_expr():
        #     declaration_code = f"{self.enterNum_expr(ctx.num_expr())}"
        # elif ctx.bool_expr():
        #     declaration_code = f"{self.enterBool_expr(ctx.bool_expr())}"

        # self.intermediate_code.add_intermediate_output(declaration_code)
        pass

    # Exit a parse tree produced by ZenithGrammarParser#exprs.
    def exitExprs(self, ctx: ZenithGrammarParser.ExprsContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#bool_computation_expr.
    def enterBool_computation_expr(self, ctx: ZenithGrammarParser.Bool_computation_exprContext):
        # print("bool computation", ctx.getText(), ctx.getChildCount())
        if ctx.bool_bracket_expr():
            return self.enterBool_bracket_expr(ctx.bool_bracket_expr())

        elif ctx.bool_computation_expr():

            value1 = self.enterBool_computation_expr(ctx.bool_computation_expr(0))
            value2 = self.enterBool_computation_expr(ctx.bool_computation_expr(1))
            # print("check this", value1, " and ", value2)

            if ctx.AND():
                return value1 + " and " + value2

            if ctx.OR():
                return value1 + " or " + value2

            if ctx.IS_EQUL_TO():
                return value1 + " == " + value2

            if ctx.NOT_EQUL_TO():
                return value1 + " != " + value2

        elif ctx.comp_expr():
            # print("comes to evaluation")
            return self.enterNumberComparisonExpression(ctx.comp_expr())

    # Enter a parse tree produced by ZenithGrammarParser#bool_bracket_expr.
    def enterBool_bracket_expr(self, ctx: ZenithGrammarParser.Bool_bracket_exprContext):
        if ctx.BOOLEAN():
            if ctx.BOOLEAN().getText() == 'false':
                return 'False'
            else:
                return 'True'

        elif ctx.VARIABLE_IDENTIFIER():
            variable_name = ctx.VARIABLE_IDENTIFIER().getText()
            check = self.does_variable_exist(variable_name)
            if check:
                return ctx.VARIABLE_IDENTIFIER().getText()
            else:
                print("Error: variable not found")
                sys.exit()

        elif ctx.bool_expr():
            # print("bool expr", ctx.bool_expr().getText())
            return '(' + self.enterBool_expr(ctx.bool_expr()) + ')'
        pass

    # Exit a parse tree produced by ZenithGrammarParser#bool_bracket_expr.
    def exitBool_bracket_expr(self, ctx: ZenithGrammarParser.Bool_bracket_exprContext):
        pass

    # Exit a parse tree produced by ZenithGrammarParser#bool_computation_expr.
    def exitBool_computation_expr(self, ctx: ZenithGrammarParser.Bool_computation_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#numberComparisonExpression.
    def enterNumberComparisonExpression(self, ctx: ZenithGrammarParser.NumberComparisonExpressionContext):
        # print("content", ctx.getText(), ctx.getChildCount())

        value1 = self.enterNum_expr(ctx.num_expr(0))
        value2 = self.enterNum_expr(ctx.num_expr(1))

        # print("check", value1, " and ", value2)

        if ctx.LESS_THAN():
            return value1 + " < " + value2

        elif ctx.GREATER_THAN():
            return value1 + " > " + value2

        elif ctx.MORE_THAN_OR_EQUL():
            return value1 + " >= " + value2

        elif ctx.LESS_THAN_OR_EQUL():
            return value1 + " <= " + value2

        elif ctx.NOT_EQUL_TO():
            return value1 + " != " + value2

        elif ctx.IS_EQUL_TO():
            # print("check-equal", value1, " and ", value2)

            return value1 + " == " + value2

    # Exit a parse tree produced by ZenithGrammarParser#numberComparisonExpression.
    def exitNumberComparisonExpression(self, ctx: ZenithGrammarParser.NumberComparisonExpressionContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#num_expr.
    def enterNum_expr(self, ctx: ZenithGrammarParser.Num_exprContext):
        # print("comes to number expression", ctx.getText(), ctx.getChildCount())

        if ctx.VARIABLE_IDENTIFIER():
            variable_name = ctx.VARIABLE_IDENTIFIER().getText()
            # print(variable_name)
            check = self.does_variable_exist(variable_name)
            if check:
                if self.type_list[variable_name] != 'boolean' and self.type_list[variable_name] != 'string':
                    declaration_code = f"{variable_name}"
                    if ctx.num_expr():
                        value = self.enterNum_expr(ctx.num_expr())
                        declaration_code += f" = {value}"
                        # print("enterNum declaration - ", declaration_code)
                        return declaration_code
                        # self.intermediate_code.add_intermediate_output(declaration_code)
        else:
            return self.enterAdd_sub_expr(ctx.add_sub_expr())

    # Exit a parse tree produced by ZenithGrammarParser#num_expr.
    def exitNum_expr(self, ctx: ZenithGrammarParser.Num_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#add_sub_expr.
    def enterAdd_sub_expr(self, ctx: ZenithGrammarParser.Add_sub_exprContext):
        # print("comes to add expression", ctx.getText(), ctx.getChildCount())  
        # print("comes to multiple children check", ctx.getText(), ctx.getChildCount())  
        if ctx.ADD():
            # print("comes to add specific")
            value1 = self.enterAdd_sub_expr(ctx.add_sub_expr())
            value2 = self.enterTerm_expr(ctx.term_expr())
            declaration_code = f" {value1}"
            declaration_code += f" + {value2}"
            return declaration_code

        elif ctx.SUB():
            value1 = self.enterAdd_sub_expr(ctx.add_sub_expr())
            value2 = self.enterTerm_expr(ctx.term_expr())
            declaration_code = f" {value1}"
            declaration_code += f" - {value2}"
            return declaration_code

        else:
            return self.enterTerm_expr(ctx.term_expr())

    # Exit a parse tree produced by ZenithGrammarParser#add_sub_expr.
    def exitAdd_sub_expr(self, ctx: ZenithGrammarParser.Add_sub_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#term_expr.
    def enterTerm_expr(self, ctx: ZenithGrammarParser.Term_exprContext):
        # print("comes to mult expression", ctx.getText(),  ctx.getChildCount())  

        if ctx.MUL():
            # print("comes to mult specific")
            value1 = self.enterTerm_expr(ctx.term_expr())
            value2 = self.enterBracket_expr(ctx.bracket_expr())
            declaration_code = f" {value1}"
            declaration_code += f" * {value2}"
            return declaration_code

        elif ctx.DIV():
            value1 = self.enterTerm_expr(ctx.term_expr())
            value2 = self.enterBracket_expr(ctx.bracket_expr())
            declaration_code = f" {value1}"
            declaration_code += f" / {value2}"
            return declaration_code

        else:
            return self.enterBracket_expr(ctx.bracket_expr())

    # Exit a parse tree produced by ZenithGrammarParser#term_expr.
    def exitTerm_expr(self, ctx: ZenithGrammarParser.Term_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#bracket_expr.
    def enterBracket_expr(self, ctx: ZenithGrammarParser.Bracket_exprContext):
        # print("bracket expr", ctx.getText())
        if ctx.num_expr():
            # print("num_expr", ctx.num_expr().getText())  
            return '(' + self.enterNum_expr(ctx.num_expr()) + ' )'

        elif ctx.DIGITS():
            # print("digits", ctx.DIGITS().getText()) 
            return ctx.DIGITS().getText()

        elif ctx.DECIMAL_VALUE():
            # print("decimal value", ctx.DECIMAL_VALUE().getText()) 
            return ctx.DECIMAL_VALUE().getText()

        elif ctx.VARIABLE_IDENTIFIER():
            # print("variable identifier", ctx.VARIABLE_IDENTIFIER().getText()) 
            variable_name = ctx.VARIABLE_IDENTIFIER().getText()
            check = self.does_variable_exist(variable_name)
            if check:
                return ctx.VARIABLE_IDENTIFIER().getText()
            else:
                print("Error: variable not defined")
                sys.exit()

    # Exit a parse tree produced by ZenithGrammarParser#bracket_expr.
    def exitBracket_expr(self, ctx: ZenithGrammarParser.Bracket_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#cond_expr.
    def enterCond_expr(self, ctx: ZenithGrammarParser.Cond_exprContext):
        return self.enterBool_expr(ctx.bool_expr())
        pass

    # Exit a parse tree produced by ZenithGrammarParser#cond_expr.
    def exitCond_expr(self, ctx: ZenithGrammarParser.Cond_exprContext):
        pass

        # Enter a parse tree produced by ZenithGrammarParser#if_expr.
    def enterIf_expr(self, ctx: ZenithGrammarParser.If_exprContext):
        i = 0
        # print("entered if", ctx.getText())
        # print("count", ctx.block().atomic_block(0).getChildCount())

        value = f"if {self.enterCond_expr(ctx.cond_expr())}:"
        value += "\n{"

        self.intermediate_code.add_intermediate_output(value)
        self.indentOppCond()
        # print("list_check ---- ", self.indent_list)

        # print("This is exclusively from if", ctx.block().atomic_block(0).getText())
        self.indent_list.append(ctx.block().atomic_block(0).getChildCount())
        pass

    # Exit a parse tree produced by ZenithGrammarParser#if_expr.
    def exitIf_expr(self, ctx: ZenithGrammarParser.If_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#else_if_expr.
    def enterElse_if_expr(self, ctx: ZenithGrammarParser.Else_if_exprContext):
        i = 0
        # print("entered elif", ctx.getText())
        # print("count", ctx.block().atomic_block(0).getChildCount())

        value = f"elif {self.enterCond_expr(ctx.cond_expr())}:"
        value += "\n{"
        
        self.intermediate_code.add_intermediate_output(value)
        self.indentOppCond()
        # print("list_check ---- ", self.indent_list)

        self.indent_list.append(ctx.block().atomic_block(0).getChildCount())
        pass

    # Exit a parse tree produced by ZenithGrammarParser#else_if_expr.
    def exitElse_if_expr(self, ctx: ZenithGrammarParser.Else_if_exprContext):
        
        pass

    # Enter a parse tree produced by ZenithGrammarParser#else_expr.
    def enterElse_expr(self, ctx: ZenithGrammarParser.Else_exprContext):
        i = 0
        # print("entered elif", ctx.getText())
        # print("count", ctx.block().atomic_block(0).getChildCount())

        value = f"else:"
        value += "\n{"
        
        self.intermediate_code.add_intermediate_output(value)
        self.indentOppCond()
        self.indent_list.append(ctx.block().atomic_block(0).getChildCount())

        # print("list_check ---- ", self.indent_list)

        pass

    # Exit a parse tree produced by ZenithGrammarParser#else_expr.
    def exitElse_expr(self, ctx: ZenithGrammarParser.Else_exprContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#while_expr.
    def enterWhile_expr(self, ctx: ZenithGrammarParser.While_exprContext):
        # print("entered while", ctx.getText())
        value = f"while {self.enterCond_expr(ctx.cond_expr())}:"
        value += "\n{"
        # print("value", value)
        self.intermediate_code.add_intermediate_output(value)
        self.indentOppCond()
        self.indent_list.append(ctx.block().atomic_block(0).getChildCount())  
        pass

    # Exit a parse tree produced by ZenithGrammarParser#while_expr.
    def exitWhile_expr(self, ctx: ZenithGrammarParser.While_exprContext):
        pass


    # Enter a parse tree produced by ZenithGrammarParser#for_enhanced.
    def enterFor_enhanced(self, ctx: ZenithGrammarParser.For_enhancedContext):
        # print("entered for", ctx.getText())
        # print("range", ctx.rangeVal()[0].getText())
        value = f"for {ctx.VARIABLE_IDENTIFIER().getText()} in range({self.enterRangeVal(ctx.rangeVal()[0])}, {self.enterRangeVal(ctx.rangeVal()[1])}):"
        value += "\n{"
        # print("value", value)
        self.intermediate_code.add_intermediate_output(value)
        self.indentOppCond()
        self.indent_list.append(ctx.block().atomic_block(0).getChildCount())
        pass

    # Exit a parse tree produced by ZenithGrammarParser#for_enhanced.
    def exitFor_enhanced(self, ctx: ZenithGrammarParser.For_enhancedContext):
        pass

    # Enter a parse tree produced by ZenithGrammarParser#rangeVal.
    def enterRangeVal(self, ctx: ZenithGrammarParser.RangeValContext):
        if ctx.VARIABLE_IDENTIFIER():
            variable_name = ctx.VARIABLE_IDENTIFIER().getText()
            check = self.does_variable_exist(variable_name)
            if check:
                return ctx.VARIABLE_IDENTIFIER().getText()
            else:
                print("Error: variable not defined")
                sys.exit()

        elif ctx.DIGITS():
            return ctx.DIGITS().getText()
        pass

    # Exit a parse tree produced by ZenithGrammarParser#rangeVal.
    def exitRangeVal(self, ctx: ZenithGrammarParser.RangeValContext):
        pass

    # def get_value_after_equals(self, ctx):
    # # Get the assignment expression
    #     assignment_expr = ctx.assignment_expr().getText()

    #     # Split the string on the "=" sign
    #     _, value = assignment_expr.split("#=")

    #     # Remove leading and trailing whitespace and return the first character
    #     return value.strip()[0]
    
    # def get_id_after_equals(self, ctx):
    # # Get the assignment expression
    #     assignment_expr = ctx.assignment_expr().getText()

    #     # Split the string on the "=" sign
    #     id, _ = assignment_expr.split("#=")

    #     # Remove leading and trailing whitespace and return the first character
    #     return id.strip()[0]
    
    def get_value_after_operator(self, ctx):
    # Get the boolean expression
        bool_expr = ctx.bool_expr().getText()

        # Split the string on the space character
        _, value = re.split("<=|>=|<|>", bool_expr)
        # print("value", value)

        # Return the value converted to an integer
        return value
    
    def get_operator_and_value(self, ctx):
    # Get the variable change expression
        var_change_expr = ctx.variable_change_part().getText()

    # Use a regular expression to find the operator and the number
        match = re.search(r'(?:\w+=\w+\+)?(\d+)|(?:\w+=\w+-)?(\d+)|(\+\+)|(--)', var_change_expr)

        if match:
            # If a match was found, return the appropriate number
            if match.group(3) == '++':
                return 1
            elif match.group(4) == '--':
                return -1
            elif match.group(1):
                return int(match.group(1))
            elif match.group(2):
                return -int(match.group(2))

        # If no match was found, return None
        return None

    # Enter a parse tree produced by ZenithGrammarParser#for_loop.
    def enterFor_loop(self, ctx: ZenithGrammarParser.For_loopContext):
        # print("entered for", ctx.getText())
        # print("id value inside for", self.get_id_after_equals(ctx))
        # print("ctx bool", ctx.bool_expr().getText())
        value = f"{ctx.VARIABLE_IDENTIFIER().getText()} = {ctx.DIGITS()} \nfor {ctx.VARIABLE_IDENTIFIER().getText()} in range({ctx.DIGITS()},{self.get_value_after_operator(ctx)},{self.get_operator_and_value(ctx)}):"
        value += "\n{"
        # print("value for loop shit", value)
        self.intermediate_code.add_intermediate_output(value)
        self.indentOppCond()
        # print("This is exclusively from for", ctx.block().getChild(0).getText())
        # print("This is exclusively from for", ctx.block().getChild(1).getText())
        # print("This is exclusively from for", ctx.block().getChild(2).getText())
        # print("This is exclusively from for", ctx.block().getChild(3).getText())
        # print("This is exclusively from for", ctx.block().atomic_block(0).getChild(0).getText())
        self.indent_list.append(ctx.block().atomic_block(0).getChildCount())
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
        # print("ternary", ctx.getText())
        # print("exprs in ternary", ctx.exprs(0).getText())
        value = ""
        if ctx.exprs(0):
            value = f"{self.enterExprs(ctx.exprs(0))} if {self.enterCond_expr(ctx.cond_expr())} else {self.enterExprs(ctx.exprs(1))}"
        elif ctx.BOOLEAN(0):
            if ctx.BOOLEAN(0).getText() == "false":
                if ctx.BOOLEAN(1).getText() == "false":
                    value = f"False if {self.enterCond_expr(ctx.cond_expr())} else False"
                else:
                    value = f"False if {self.enterCond_expr(ctx.cond_expr())} else True"
            else:
                if ctx.BOOLEAN(1).getText() == "false":
                    value = f"True if {self.enterCond_expr(ctx.cond_expr())} else False"
                else:
                    value = f"True if {self.enterCond_expr(ctx.cond_expr())} else True"
            # print("value", value)
        else:
            # print("valid string", ctx.VALID_STRING(0))
            value = f"{(ctx.VALID_STRING(0))} if {self.enterCond_expr(ctx.cond_expr())} else {(ctx.VALID_STRING(1))}"
            # print("value", value)
        # value = f"{self.enterExprs(ctx.exprs(0))} if {self.enterCond_expr(ctx.cond_expr())} else {self.enterExprs(ctx.exprs(1))}"
        # print("value", value)
        return value
        # self.intermediate_code.add_intermediate_output(value)
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
        # print("print", ctx.getText())
        # print("print parameters length", ctx.getChild(2).getText())
        value = f"print({ctx.getChild(2).getText()}"
        # print("from child",value)
        # value = ""
        i = 3
        while i < ctx.getChildCount() - 1:
            value += f"{ctx.getChild(i).getText()}"
            i += 1
        value += ")"
        # print("value from print", value)
        self.intermediate_code.add_intermediate_output(value)
        self.indentOpp()
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
