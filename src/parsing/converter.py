from abc import ABC, abstractmethod
from typing import List

from graphviz import Graph
from reader.reader import Reader
from ds.token.token import *
from ds.fileContent.fileContent import FileContent
from ds.umlGraph.umlGraph import UMLGraph
from parsing.parser import Parser
from parsing.lexer import Lexer

class Converter(ABC):
    def convert(self, filePath) -> None:
        fileFormat, fileContent = self.readFile(filePath)
        listTokens = self.parseToTokens(fileFormat, fileContent)
        umlGraph = self.convertToGraph(listTokens)
        graph = umlGraph.toDotGraph()
        graph.render('test-output/umlGraph.gv', view=True)
    
    @abstractmethod
    def readFile(self, filePath) -> FileContent:
        pass

    @abstractmethod
    def parseToTokens(self, fileFormat: str, fileContent: FileContent) -> List[Token]:
        pass

    @abstractmethod
    def convertToGraph(self, tokens: List[Token]) -> UMLGraph:
        pass


class DotConverter(Converter):
    def readFile(self, filePath) -> FileContent:
        fileReader = Reader(filePath)
        fileReader.stragety()
        return fileReader.extension[1:], fileReader.get_output()

    def parseToTokens(self, fileFormat: str, fileContent: FileContent) -> List[Token]:
        lexer = Lexer(fileFormat)
        return lexer.analyze(fileContent)

    def convertToGraph(self, tokens: List[Token]) -> UMLGraph:
        return Parser.parse(tokens)