import sys
from antlr4 import *
# Проверьте, что названия файлов соответствуют вашим сгенерированным ANTLR
from RelationalLangLexer import RelationalLangLexer
from RelationalLangParser import RelationalLangParser
from RelationalLangVisitor import RelationalLangVisitor


class LLVMCompiler(RelationalLangVisitor):
    def __init__(self):
        self.code = []
        self.reg_count = 0
        self.label_count = 0
        self.locals = {}  # Хранит адреса переменных (%var.addr)
        self.global_code = []

    def _next_reg(self):
        self.reg_count += 1
        return f"%{self.reg_count}"

    def _next_label(self, name="label"):
        self.label_count += 1
        return f"{name}_{self.label_count}"

    def visitProgram(self, ctx):
        # Внешние функции
        self.global_code.append('declare i32 @printf(i8*, ...)')
        self.global_code.append('@fmt_int = private unnamed_addr constant [4 x i8] c"%d\\0A\\00"')

        # 1. Компилируем подпрограммы (в начало)
        subs = ""
        for sub in ctx.subprogram():
            subs += self.visit(sub) + "\n"

        # 2. Компилируем основную часть
        self.code = []
        for stmt in ctx.statement():
            self.visit(stmt)

        main_body = "\n".join(self.code)

        return "\n".join(self.global_code) + "\n\n" + subs + \
            "define i32 @main() {\n" + main_body + "\n  ret i32 0\n}"

    def visitSubprogram(self, ctx):
        f_name = ctx.ID().getText()
        params = []
        if ctx.params():
            params = [f"i32* %arg_{p.getText()}" for p in ctx.params().ID()]

        header = f"define void @{f_name}({', '.join(params)}) {{"
        old_locals = self.locals.copy()
        temp_code = self.code
        self.code = []

        if ctx.params():
            for p in ctx.params().ID():
                self.locals[p.getText()] = f"%arg_{p.getText()}"

        self.visit(ctx.block())
        self.code.append("  ret void")

        func_body = "\n".join(self.code)
        self.code = temp_code
        self.locals = old_locals
        return f"{header}\n{func_body}\n}}"

    def visitAssignment(self, ctx):
        var_name = ctx.varName().getText()
        if var_name not in self.locals:
            addr = f"%{var_name}.addr"
            self.code.append(f"  {addr} = alloca i32")
            self.locals[var_name] = addr

        val_reg = self.visit(ctx.expr())
        self.code.append(f"  store i32 {val_reg}, i32* {self.locals[var_name]}")
        return val_reg

    def visitIfStatement(self, ctx):
        cond_reg = self.visit(ctx.expr())
        bool_reg = self._next_reg()
        self.code.append(f"  {bool_reg} = icmp ne i32 {cond_reg}, 0")

        l_then = self._next_label("if_then")
        l_else = self._next_label("if_else")
        l_end = self._next_label("if_end")

        self.code.append(f"  br i1 {bool_reg}, label %{l_then}, label %{l_else}")
        self.code.append(f"{l_then}:")
        self.visit(ctx.block(0))
        self.code.append(f"  br label %{l_end}")
        self.code.append(f"{l_else}:")
        if ctx.block(1): self.visit(ctx.block(1))
        self.code.append(f"  br label %{l_end}")
        self.code.append(f"{l_end}:")

    def visitUntilStatement(self, ctx):
        l_cond = self._next_label("until_cond")
        l_body = self._next_label("until_body")
        l_end = self._next_label("until_end")

        self.code.append(f"  br label %{l_cond}")
        self.code.append(f"{l_cond}:")
        cond_reg = self.visit(ctx.expr())
        bool_reg = self._next_reg()
        self.code.append(f"  {bool_reg} = icmp ne i32 {cond_reg}, 0")
        self.code.append(f"  br i1 {bool_reg}, label %{l_end}, label %{l_body}")
        self.code.append(f"{l_body}:")
        self.visit(ctx.block())
        self.code.append(f"  br label %{l_cond}")
        self.code.append(f"{l_end}:")

    def visitPrimary(self, ctx):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        if ctx.varName():
            var_name = ctx.varName().getText()
            reg = self._next_reg()
            self.code.append(f"  {reg} = load i32, i32* {self.locals[var_name]}")
            return reg
        return self.visitChildren(ctx)

    def visitFunctionCall(self, ctx):
        f_name = ctx.getChild(0).getText()
        if f_name == "write":
            val_reg = self.visit(ctx.expr(0))
            fmt = "getelementptr inbounds ([4 x i8], [4 x i8]* @fmt_int, i32 0, i32 0)"
            self.code.append(f"  call i32 (i8*, ...) @printf(i8* {fmt}, i32 {val_reg})")
        return None


# --- БЛОК ЗАПУСКА ---
if __name__ == '__main__':
    # 1. Укажите имя вашего файла с кодом
    input_filename = 'correct_code.txt'
    try:
        input_stream = FileStream(input_filename, encoding='utf-8')
        lexer = RelationalLangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = RelationalLangParser(token_stream)
        tree = parser.program()

        # 2. Запуск компилятора
        compiler = LLVMCompiler()
        result_llvm = compiler.visit(tree)

        # 3. Сохранение в файл
        with open('output.ll', 'w', encoding='utf-8') as f:
            f.write(result_llvm)

        print(f"Успех! Файл 'output.ll' создан в папке {sys.path[0]}")
    except Exception as e:
        print(f"Ошибка при компиляции: {e}")