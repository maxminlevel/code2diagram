# Create class Lexer parse codes to tokens:
# - For applying Visitor pattern, we use FileContent concrete classes as visitors
# - Has different overload parse methods for every FileContent concrete class
# - Input: Code content (FileContent)
# - Output: List of tokens 
from ds.token import *

class Lexer(object):
    pass