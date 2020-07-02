""" This is a JIT compiler that will take a sample High level language psedo code and transfear it to a bytecode that can be executed on the machine"""
from rply import LexerGenerator, ParserGenerator


class Lexer:
    def __init__(self):
        self.tokens = [
            ("CHARECTER",r'"A" | "B" | "C" | "D" | "E" | "F" | "G" \ \
                       | "H" | "I" | "J" | "K" | "L" | "M" | "N" \
                       | "O" | "P" | "Q" | "R" | "S" | "T" | "U" \
                       | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" \
                       | "c" | "d" | "e" | "f" | "g" | "h" | "i" \
                       | "j" | "k" | "l" | "m" | "n" | "o" | "p" \
                       | "q" | "r" | "s" | "t" | "u" | "v" | "w" \
                       | "x" | "y" | "z"'),
            ("DIGITS",r'"0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"'),
            ("SYMBOL",r'"[" | "]" | "{" | "}" | "(" | ")" | "<" | ">" \
                            | "'" | '"' | "=" | "|" | "." | "," | ";"'),
            ("WORD",r'\w'),
            ('VAR', r'var'), # a variable deceleration, the value will be saved in the machine memory
            ('CONST', r'const'), # constant that will be saved in the global storage of the machine
            ('ASSIGNMENT', r'='), # assignment
            ('EQUAL', r'=='), # equal
            ('GREATERTHAN', r'>'), # greater than
            ('GREATERTHANOREQUAL', r'>='),
            ('LESSERTHAN', r'<'),
            ('LESSERTHANOREQUAL', r'<='),
            ('NOTEQUAL', r'!='),
            ('AND', r'&'),
            ('ANDOPR', r'&&'),
            ('OR', r'|'),
            ('OROPR', r'||'),
            ('NOT', r'!'),
            ('NOTPR', r'!='),
            ('SHIFTLEFT', r'>>'),
            ('SHIFTRIGHT', r'<<'),
            ('INCREMENTBT', r'+='),
            ('DECREMENTBY', r'-='),
            ('PRINT', r'print'),
            ('IF', r'if'),
            ('ELSE', r'else'),
            ('EIF', r'eif'),
            ('OPEN_PAREN', r'\('),
            ('CLOSE_PAREN', r'\)'),
            ('OPEN_SQRBRACKETS', r'\['),
            ('CLOSE_SQRBRACKETS', r'\]'),
            ('OPEN_QURLYBRACES', r'\{'),
            ('CLOSE_QURLYBRACES', r'\]'),
            ('SEMI_COLON', r'\;'),
            ('COMMA', r'\,'),
            ('SUM', r'\+'),
            ('SUB', r'\-'),
            ('MULT', r'\*'),
            ('LEFTDIV', r'\\'),
            ('RIGHTDIV', r'\/'),
            ('REMINDER', r'\%'),
            ('NUMBER', r'\d+'),
            ('STRING', r'"\w+"'),
            ('BOOLEAN', r'[True|False]'),
            ('FOR', r'for'),
            ('TO', r'to'),
            ('STEP', r'step')
        ]
        lexer = LexerGenerator()
        for token, rtoken in self.tokens:
            lexer.add(token, rtoken)

        lexer.ignore('\s+')  # ignore any white space
        self.lexer = lexer.build()

    @property
    def getLexer(self):
        return self.lexer

    @property
    def getTokens(self):
        return [X for X, x in self.tokens]

    def generateTokens(self, text):
        return self.lexer.lex(text)
class Parser:
    class Number:
        """
        Number data type that represent an 8 bit integer
        """

        def __init__(self, value):
            self.value = value

        def eval(self):
            """ evaluate """
            return int(self.value)

        def generate(self):
            return [

            ]
    class String:
        """
        String data type
        """
        def __init__(self, value):
            self.value = value

        def eval(self):
            """ evaluate """
            return int(self.value)

        def generate(self):
            return [

            ]
    class Boolean:
        """
        Boolean data type
        """
        def __init__(self, value):
            self.value = value

        def eval(self):
            """ evaluate """
            return int(self.value)

        def generate(self):
            return [

            ]
    class BinaryOp():
        """
        Base class for any binary operations
        """
        def __init__(self, left, right):
            self.left = left
            self.right = right
    class Sum(BinaryOp):
        def eval(self):
            return self.left.eval() + self.right.eval()
    class Sub(BinaryOp):
        def eval(self):
            return self.left.eval() - self.right.eval()
    class Mult(BinaryOp):
        def eval(self):
            return self.left.eval() * self.right.eval()
    class LeftDiv(BinaryOp):
        def eval(self):
            return self.left.eval() / self.right.eval()
    class RightDiv(BinaryOp):
        def eval(self):
            return self.right.eval() / self.left.eval()
    class Print():
        def __init__(self, value):
            self.value = value

        def eval(self):
            print(self.value.eval())

    def __init__(self, tokens):
        self.pg = ParserGenerator(tokens)

    def parse(self):
        @self.pg.production('letter : "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" \
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U" \
       | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" \
       | "c" | "d" | "e" | "f" | "g" | "h" | "i" \
       | "j" | "k" | "l" | "m" | "n" | "o" | "p" \
       | "q" | "r" | "s" | "t" | "u" | "v" | "w" \
       | "x" | "y" | "z" ')
        def letter(p):
            """ evaluate letters """
            pass

        @self.pg.production('digit : "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ')
        def digit(p):
            pass

        @self.pg.production('symbol : "[" | "]" | "{" | "}" | "(" | ")" | "<" | ">" \
       | "'" | '"' | "=" | "|" | "." | "," | ";" ')
        def symbol(p):
            pass

        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return self.Print(p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return self.Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return self.Sub(left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return self.Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    @property
    def getParser(self):
        return self.pg.build()


class Compiler:
    def __init__(self, lexer):
        self.Lexer = lexer
        self.Parser = Parser(lexer.getTokens)
        self.Parser.parse()

    def Compile(self, text):
        tokens = self.Lexer.generateTokens(text)
        self.Parser.getParser.parse(tokens)

    def Evaluate(self, text):
        tokens = self.Lexer.generateTokens(text)
        self.Parser.getParser.parse(tokens).eval()

    def GenerateBytecode(self, text):
        """ Will take a line of code and generate its corespondent OpCode lines and return it as a list """
        tokens = self.Lexer.generateTokens(text)
        return self.Parser.getParser.parse(tokens).generate()
