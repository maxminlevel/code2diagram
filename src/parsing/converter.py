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
    def convert(self, inputFile, outputFile) -> None:
        fileFormat, fileContent = self.readFile(inputFile)
        listTokens = self.parseToTokens(fileFormat, fileContent)
        umlGraph = self.convertToGraph(listTokens)
        graph = umlGraph.toDotGraph()
        graph.render(outputFile, view=False)
    
    @abstractmethod
    def readFile(self, inputFile) -> FileContent:
        pass

    @abstractmethod
    def parseToTokens(self, fileFormat: str, fileContent: FileContent) -> List[Token]:
        pass

    @abstractmethod
    def convertToGraph(self, tokens: List[Token]) -> UMLGraph:
        pass


class DotConverter(Converter):
    def readFile(self, inputFile) -> FileContent:
        fileReader = Reader(inputFile)
        fileReader.stragety()
        return fileReader.extension[1:], fileReader.get_output()

    def parseToTokens(self, fileFormat: str, fileContent) -> List[Token]:
        lexer = Lexer(fileFormat)
        return lexer.analyze(fileContent)

    def convertToGraph(self, tokens: List[Token]) -> UMLGraph:
        return Parser.parse(tokens)