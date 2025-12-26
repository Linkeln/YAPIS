# Generated from RelationalLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RelationalLangParser import RelationalLangParser
else:
    from RelationalLangParser import RelationalLangParser

# This class defines a complete generic visitor for a parse tree produced by RelationalLangParser.

class RelationalLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RelationalLangParser#program.
    def visitProgram(self, ctx:RelationalLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#subprogram.
    def visitSubprogram(self, ctx:RelationalLangParser.SubprogramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#params.
    def visitParams(self, ctx:RelationalLangParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#block.
    def visitBlock(self, ctx:RelationalLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#statement.
    def visitStatement(self, ctx:RelationalLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#ifStmt.
    def visitIfStmt(self, ctx:RelationalLangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#whileStmt.
    def visitWhileStmt(self, ctx:RelationalLangParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#untilStmt.
    def visitUntilStmt(self, ctx:RelationalLangParser.UntilStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#forStmt.
    def visitForStmt(self, ctx:RelationalLangParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#assignment.
    def visitAssignment(self, ctx:RelationalLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#varName.
    def visitVarName(self, ctx:RelationalLangParser.VarNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#returnStmt.
    def visitReturnStmt(self, ctx:RelationalLangParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#expr.
    def visitExpr(self, ctx:RelationalLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#primary.
    def visitPrimary(self, ctx:RelationalLangParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RelationalLangParser#functionCall.
    def visitFunctionCall(self, ctx:RelationalLangParser.FunctionCallContext):
        return self.visitChildren(ctx)



del RelationalLangParser