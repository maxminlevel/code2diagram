# class UMLGraph
# Contain information about our uml diagram relationships
from uuid import uuid4
from functools import singledispatch

class Edge:
    def __init__(self, name, type, attributes):
        self.srcId = attributes.srcId
        self.dstId = attributes.dstId
        self.type = type
        self.name = name
        self.id = str(uuid4())
    def __str__(self):
        return self.source.name + " " + self.type + " " + self.target.name
    def __repr__(self):
        return self.source.name + " " + self.type + " " + self.target.name

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
