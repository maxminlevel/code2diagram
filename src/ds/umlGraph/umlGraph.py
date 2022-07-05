# class UMLGraph
# Contain information about our uml diagram relationships
from functools import singledispatch
from ds.umlGraph.umlNode import Node
from ds.umlGraph.umlEdge import Edge
import graphviz
class UMLGraph:
    def __init__(self):
        # initial nodes, edges
        self.nodes = []
        self.edges = []

    @singledispatch
    def add(self, graphObj):
        raise TypeError("UML Graph doesn't support type: {}").format(type(graphObj))

    @add.register(Node)
    def add_node(self, node):
        self.nodes.append(node)

    @add.register(Edge)
    def add_edge(self, edge):
        self.edges.append(edge)

    def toDotGraph(self):
        graph = graphviz.Digraph(comment="UML Graph")
        for node in self.nodes:
            graph.node(node.toDotArgs())
        for edge in self.edges:
            graph.edge(edge.toDotArgs())
        return graph
