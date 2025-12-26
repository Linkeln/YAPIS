# Generated from RelationalLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RelationalLangParser import RelationalLangParser
else:
    from RelationalLangParser import RelationalLangParser

# This class defines a complete listener for a parse tree produced by RelationalLangParser.
class RelationalLangListener(ParseTreeListener):

    # Enter a parse tree produced by RelationalLangParser#program.
    def enterProgram(self, ctx:RelationalLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#program.
    def exitProgram(self, ctx:RelationalLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#subprogram.
    def enterSubprogram(self, ctx:RelationalLangParser.SubprogramContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#subprogram.
    def exitSubprogram(self, ctx:RelationalLangParser.SubprogramContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#params.
    def enterParams(self, ctx:RelationalLangParser.ParamsContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#params.
    def exitParams(self, ctx:RelationalLangParser.ParamsContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#block.
    def enterBlock(self, ctx:RelationalLangParser.BlockContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#block.
    def exitBlock(self, ctx:RelationalLangParser.BlockContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#statement.
    def enterStatement(self, ctx:RelationalLangParser.StatementContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#statement.
    def exitStatement(self, ctx:RelationalLangParser.StatementContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#ifStmt.
    def enterIfStmt(self, ctx:RelationalLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#ifStmt.
    def exitIfStmt(self, ctx:RelationalLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#whileStmt.
    def enterWhileStmt(self, ctx:RelationalLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#whileStmt.
    def exitWhileStmt(self, ctx:RelationalLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#untilStmt.
    def enterUntilStmt(self, ctx:RelationalLangParser.UntilStmtContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#untilStmt.
    def exitUntilStmt(self, ctx:RelationalLangParser.UntilStmtContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#forStmt.
    def enterForStmt(self, ctx:RelationalLangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#forStmt.
    def exitForStmt(self, ctx:RelationalLangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#assignment.
    def enterAssignment(self, ctx:RelationalLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#assignment.
    def exitAssignment(self, ctx:RelationalLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#varName.
    def enterVarName(self, ctx:RelationalLangParser.VarNameContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#varName.
    def exitVarName(self, ctx:RelationalLangParser.VarNameContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#returnStmt.
    def enterReturnStmt(self, ctx:RelationalLangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#returnStmt.
    def exitReturnStmt(self, ctx:RelationalLangParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#expr.
    def enterExpr(self, ctx:RelationalLangParser.ExprContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#expr.
    def exitExpr(self, ctx:RelationalLangParser.ExprContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#primary.
    def enterPrimary(self, ctx:RelationalLangParser.PrimaryContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#primary.
    def exitPrimary(self, ctx:RelationalLangParser.PrimaryContext):
        pass


    # Enter a parse tree produced by RelationalLangParser#functionCall.
    def enterFunctionCall(self, ctx:RelationalLangParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by RelationalLangParser#functionCall.
    def exitFunctionCall(self, ctx:RelationalLangParser.FunctionCallContext):
        pass



del RelationalLangParser