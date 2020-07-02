from unittest import TestCase

from VM.Compiler.CodeCompiler import Lexer, Compiler


class TestLexer(TestCase):
    def test_get_lexer(self):
        lex = Lexer()
        lx = lex.getLexer
        assert lx is not None

    def test_generate_lexer_for_number(self):
        lex = Lexer()
        lx = lex.getLexer

        text_input = """
               var x:Number(4 + 4 - 2);
               """
        tokens = lex.generateTokens(text_input)


    def test_generate_lexer_tree(self):
        lex = Lexer()
        lx = lex.getLexer

        text_input = """
        print(4 + 4 - 2);
        """
        tokens = lex.generateTokens(text_input)

        for token in tokens:
            print(token)

        assert True

    def test_getTokens(self):
        lex = Lexer()
        tokens = lex.getTokens

        assert tokens[0] == "PRINT"


class TestCompiler(TestCase):
    def test_compile(self):
        cmp = Compiler(Lexer())
        text_input = """
        print(4 + 4 - 2);
        """
        cmp.Compile(text_input)

        assert True

    def test_evaluate(self):
        cmp = Compiler(Lexer())
        text_input = """
               print(4 + 4 - 2);
               """
        cmp.Evaluate(text_input)

        assert True

