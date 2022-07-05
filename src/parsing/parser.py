# Create class Parser parse list of tokens into a graph represent our diagrams:
#  - Input: List of tokens
#  - Output: A graph:
#   - Node: Actor, usecase, class
#   - Edges: Different kinds of arrow
from ds.umlGraph.umlEdge import EdgeFactory
from ds.umlGraph.umlGraph import UMLGraph
from ds.umlGraph.umlNode import NodeFactory
from ds.umlGraph.umlGraphConfig import ACTOR_TYPE, USECASE_TYPE, ARROW_TYPE, CLASS_TYPE
class Parser:
    tokenToFactory = {
        ACTOR_TYPE: NodeFactory,
        USECASE_TYPE: NodeFactory,
        ARROW_TYPE: EdgeFactory,
        CLASS_TYPE: NodeFactory
    }
    @staticmethod
    def parse(tokens):
        graph = UMLGraph()
        for token in tokens:
            factory = Parser.tokenToFactory[token.type]
            graphObj = factory.create(token)
            graph.add(graphObj)
        return graph
