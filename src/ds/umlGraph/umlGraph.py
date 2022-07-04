# class UMLGraph
# Contain information about our uml diagram relationships
from functools import singledispatch
from ds.umlGraph.umlNode import Node
from ds.umlGraph.umlEdge import Edge
class UMLGraph:
    def __init__(self):
        # initial nodes, edges
        self.nodes = {}
        self.edges = {}
        self.relationships = []

    @singledispatch
    def add(self, graphObj):
        raise TypeError("UML Graph doesn't support type: {}").format(type(graphObj))

    @add.register(Node)
    def add_node(self, node):
        self.nodes[node.id] = node

    @add.register(Edge)
    def add_edge(self, edge):
        self.edges[edge.id] = edge
        self.relationships.append({
            "srcId": edge.srcId,
            "dstId": edge.dstId,
            "edgeId": edge.id
        })
