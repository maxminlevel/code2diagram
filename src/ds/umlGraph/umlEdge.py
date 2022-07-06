from functools import singledispatch
from uuid import uuid4

from ds.token.token import ArrowToken, TypeRelation
class Edge:
    def __init__(self, type, srcId, dstId):
        self.srcId = srcId
        self.dstId = dstId
        self.type = type
        self.id = str(uuid4())
    def __str__(self):
        return self.srcId + " " + self.dstId
    def toDotArgs(self):
        return self.srcId, self.dstId

class ArrowEdge(Edge):
    def __init__(self, type, srcId, dstId):
        super().__init__(type, srcId, dstId)
    def __str__(self):
        return self.srcId + " " + self.type + " " + self.dstId
    def toDotArgs(self):
        return self.srcId, self.dstId

class EdgeFactory:
    @singledispatch
    def create(token):
        raise NotImplementedError
    @create.register(ArrowToken)
    def _(token: ArrowToken):
        return Edge(token.typeRelation, token.source, token.target)