import sys
from antlr4 import *
from RelationalLangLexer import RelationalLangLexer
from RelationalLangParser import RelationalLangParser
from SemanticAnalyzer import SemanticAnalyzer, SemanticError

def run_analysis(filename):
    print(f"\n--- Анализ файла: {filename} ---")
    input_stream = FileStream(filename, encoding='utf-8')
    lexer = RelationalLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RelationalLangParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Синтаксические ошибки найдены. Семантический анализ прерван.")
        return

    # Запуск семантического анализатора
    analyzer = SemanticAnalyzer()
    try:
        analyzer.visit(tree)
        print("Семантических ошибок не обнаружено.")
    except SemanticError as e:
        print(f"СЕМАНТИЧЕСКАЯ ОШИБКА: {e}")

if __name__ == '__main__':
    run_analysis('correct_code.txt')
    run_analysis('semantic_errors.txt')