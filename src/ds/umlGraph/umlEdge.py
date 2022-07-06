from functools import singledispatch
from uuid import uuid4

from ds.token.token import ArrowToken
class Edge:
    def __init__(self, type, srcId, dstId):
        self.srcId = srcId
        self.dstId = dstId
        self.type = type
        self.id = str(uuid4())
    def __str__(self):
        return self.srcId + " " + self.name + " " + self.dstId
    def toUMLArgs(self):
        return self.srcId, self.dstId, self.name

class ArrowEdge(Edge):
    def __init__(self, type, srcId, dstId):
        super().__init__(type, srcId, dstId)
    def __str__(self):
        return self.srcId + " " + self.name + " " + self.dstId + " " + self.typeRelation
    def toUMLArgs(self):
        if self.type 

class EdgeFactory:
    @singledispatch
    def create(token):
        raise NotImplementedError
    @create.register(ArrowToken)
    def _(token: ArrowToken):
        return Edge(token.typeRelation, token.source, token.target)