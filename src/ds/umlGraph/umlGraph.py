# class UMLGraph
# Contain information about our uml diagram relationships
from functools import singledispatchmethod
from ds.umlGraph.umlNode import Node
from ds.umlGraph.umlEdge import Edge
import graphviz
class UMLGraph:
    def __init__(self):
        # initial nodes, edges
        self.nodes = []
        self.edges = []
        self.mapNodeToGroupId = dict()
        self.groupIds = set()

    @singledispatchmethod
    def add(self, graphObj):
        raise TypeError("UML Graph doesn't support type: {}".format(graphObj.__class__.__name__))

    @add.register(Node)
    def add_node(self, node: Node):
        self.nodes.append(node)
        if node.groupId is not None:
            self.mapNodeToGroupId[node.id] = node.groupId
            self.groupIds.add(node.groupId)

    @add.register(Edge)
    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def isEdgeInGroup(self, edge: Edge, groupId: str):
        return self.mapNodeToGroupId[edge.srcId] == groupId and self.mapNodeToGroupId[edge.dstId] == groupId
        
    def toDotGraph(self):
        graph = graphviz.Digraph(comment="UML Graph")
        for node in self.nodes:
            graph.node(node.toDotArgs())
        for edge in self.edges:
            if self.mapNodeToGroupId[edge.srcId] and self.mapNodeToGroupId[edge.dstId]:
                continue
            graph.edge(edge.toDotArgs())
        for groupId in self.groupIds:
            with graph.subgraph(name=groupId) as subGraph:
                subGraph.attr(style='filled', color='lightgrey')
                subGraph.node_attr.update(style='filled', color='white')
                subGraph.edges([(edge.srcId, edge.dstId) for edge in self.edges if self.isEdgeInGroup(edge, groupId)])
                subGraph.attr(label=groupId)
        return graph
