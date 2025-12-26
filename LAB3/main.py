import sys
from antlr4 import *
from RelationalLangLexer import RelationalLangLexer
from RelationalLangParser import RelationalLangParser


def main(filename):
    input_stream = FileStream(filename, encoding='utf-8')
    lexer = RelationalLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RelationalLangParser(stream)

    # Запускаем парсинг с самого верхнего правила (program)
    tree = parser.program()

    # Если в процессе возникли ошибки, ANTLR сам выведет их в консоль
    if parser.getNumberOfSyntaxErrors() == 0:
        print(f"Файл {filename} успешно прошел проверку!")
    else:
        print(f"В файле {filename} найдено ошибок: {parser.getNumberOfSyntaxErrors()}")


if __name__ == '__main__':
    # Тестируем на правильном коде и на коде с ошибками
    main('correct_code.txt')
    main('error_code.txt')