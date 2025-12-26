from RelationalLangVisitor import RelationalLangVisitor
from RelationalLangParser import RelationalLangParser


class SemanticError(Exception):
    pass


class SemanticAnalyzer(RelationalLangVisitor):
    def __init__(self):
        # Таблица символов (храним типы переменных и функции)
        self.functions = {}
        self.current_scope = {}
        self.in_function = False

    def visitSubprogram(self, ctx):
        func_name = ctx.ID().getText()
        if func_name in self.functions:
            raise SemanticError(f"Ошибка: Функция '{func_name}' уже объявлена.")

        # Считаем количество параметров
        params = []
        if ctx.params():
            params = [p.getText() for p in ctx.params().ID()]

        self.functions[func_name] = len(params)

        # Входим в область видимости функции
        self.in_function = True
        old_scope = self.current_scope.copy()

        # Добавляем параметры в локальную область видимости
        for p in params:
            self.current_scope[p] = "unknown"  # Тип определится при использовании

        result = self.visitChildren(ctx)

        # Выходим из области видимости (очищаем локальные переменные)
        self.current_scope = old_scope
        self.in_function = False
        return result

    def visitAssignment(self, ctx):
        var_name = ctx.varName().getText()
        # Неявное объявление: просто добавляем в текущую область видимости
        if var_name not in self.current_scope:
            self.current_scope[var_name] = "defined"
        return self.visitChildren(ctx)

    def visitFunctionCall(self, ctx):
        # Если это пользовательская функция (есть ID)
        if ctx.ID():
            func_name = ctx.ID().getText()
            if func_name not in self.functions:
                raise SemanticError(f"Ошибка: Вызов необъявленной функции '{func_name}'.")

            # Проверка количества аргументов
            args_count = len(ctx.expr()) if ctx.expr() else 0
            expected = self.functions[func_name]
            if args_count != expected:
                raise SemanticError(f"Ошибка в '{func_name}': ожидалось {expected} аргументов, получено {args_count}.")

        return self.visitChildren(ctx)

    def visitPrimary(self, ctx):
        if ctx.varName():
            var_name = ctx.varName().getText()
            # Проверка использования необъявленной переменной
            if var_name not in self.current_scope and var_name not in ['table', 'row', 'column', 'int', 'float',
                                                                       'string']:
                raise SemanticError(f"Ошибка: Переменная '{var_name}' используется до присваивания.")
        return self.visitChildren(ctx)