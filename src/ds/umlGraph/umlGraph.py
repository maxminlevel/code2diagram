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
        self.defaultGraphStyles = {
            'graph': {
                'rankdir': 'TB',
                'bgcolor': 'white',
                'fontsize': '16',
                'fontcolor': 'black',
                'fontname': 'Arial',
                'splines': 'ortho',
                'nodesep': '0.5',
                'ranksep': '0.5'
            },
            'node': {
                'fontsize': '16',
                'fontcolor': 'black',
                'fontname': 'Arial',
                'style': 'filled',
                'fillcolor': 'white',
                'height': '0.5',
                'width': '0.5'
            },
            'edge': {
                'fontsize': '16',
                'fontcolor': 'black',
                'fontname': 'Arial',
                'arrowsize': '0.5'
            }
        }
        self.defaultSubgraphStyles = {
            'graph': {
                'color': 'blue',
            },
            'node': {
            },
            'edge': {
                'color': 'black'
            }
        }
        

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
        if edge.srcId in self.mapNodeToGroupId and edge.dstId in self.mapNodeToGroupId:
            return self.mapNodeToGroupId[edge.srcId] == self.mapNodeToGroupId[edge.dstId] and self.mapNodeToGroupId[edge.srcId] == groupId
        return False
        
    def toDotGraph(self):
        graph = graphviz.Digraph(comment="UML Graph", format="png")
        graph.graph_attr.update(self.defaultGraphStyles['graph'])
        graph.node_attr.update(self.defaultGraphStyles['node'])
        graph.edge_attr.update(self.defaultGraphStyles['edge'])
        for node in self.nodes:
            id, name, attributes = node.toDotArgs()
            graph.node(id, label=name, **attributes)
        for edge in self.edges:
            if edge.srcId in self.mapNodeToGroupId and edge.dstId in self.mapNodeToGroupId:
                continue
            src, target, styles = edge.toDotArgs()
            graph.edge(src, target, **styles)
        for groupId in self.groupIds:
            subgraphName = "cluster_" + groupId
            with graph.subgraph(name=subgraphName) as subGraph:
                subGraph.attr(**self.defaultSubgraphStyles['graph'])
                subGraph.node_attr.update(**self.defaultSubgraphStyles['node'])
                subGraph.edge_attr.update(**self.defaultSubgraphStyles['edge'])
                edges = []
                for edge in self.edges:
                    if self.isEdgeInGroup(edge, groupId):
                        src, target, styles = edge.toDotArgs()
                        subGraph.edge(src, target, **styles)
        return graph

    def withGraphStyles(self, graphStyles):
        newStyles = {**self.defaultGraphStyles['graph'], **graphStyles}
        self.defaultGraphStyles['graph'] = newStyles
        return self
    
    def withNodeStyles(self, nodeStyles):
        newStyles = {**self.defaultGraphStyles['node'], **nodeStyles}
        self.defaultGraphStyles['node'] = newStyles
        return self
    
    def withEdgeStyles(self, edgeStyles):
        newStyles = {**self.defaultGraphStyles['edge'], **edgeStyles}
        self.defaultGraphStyles['edge'] = newStyles
        return self
    
