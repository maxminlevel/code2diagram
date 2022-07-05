# Create class Lexer parse codes to tokens:
# - For applying Visitor pattern, we use FileContent concrete classes as visitors
# - Has different overload parse methods for every FileContent concrete class
# - Input: Code content (FileContent)
# - Output: List of tokens 

from parsing.lexerMethod import LexerMethod

obj = '{"attribute": {"name": "Simple", "type": "Usecase"}, "data": [{"name": "Man", "uniq": "1", "type": "actor", "group": "", "attribute": {}}, {"name": "do some thing", "uniq": "2", "type": "action", "group": "", "attribute": {}}, {"source": 1, "target": 2, "type": "arrow", "attribute": {}}]}'

class Lexer(object):
    def __init__(self, type):
        self.type = type
        self.lexerMethod = None
        
    def analyze(self, fileContent):
        self.setLexerMethod(self.select_type_lexer_method(self.type))
        return self.lexerMethod.analyze(fileContent)

    def setLexerMethod(self, method: LexerMethod):
        self.lexerMethod = method

    def select_type_lexer_method(self, typeFileContent: str):
        lexerMethod = LexerMethod.instance[typeFileContent]
        if not lexerMethod:
            raise TypeError("This type isn't supported: {}".format(type(typeFileContent)))
        return lexerMethod

lexer = Lexer("json")
listTokens = lexer.analyze(obj)
print(listTokens)




