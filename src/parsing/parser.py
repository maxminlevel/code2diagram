# Create class Parser parse list of tokens into a graph represent our diagrams:
#  - Input: List of tokens
#  - Output: A graph:
#   - Node: Actor, usecase, class
#   - Edges: Different kinds of arrow
from ds.umlGraph import UMLGraph, Node, Edge
from parsing.umlGraphConfig import ACTOR_TYPE, USECASE_TYPE, ARROW_TYPE
class Parser:
    tokenToGraphObjMapping = {
        ACTOR_TYPE: Node,
        USECASE_TYPE: Node,
        ARROW_TYPE: Edge,
    }
    @staticmethod
    def parse(tokens):
        graph = UMLGraph()
        for token in tokens:
            graphObj = Parser.tokenToGraphObjMapping[token.type](token.value, token.type, token.attributes)
            graph.add(graphObj)
        return graph
