from functools import singledispatch
from uuid import uuid4

from ds.token.token import ArrowToken, TypeRelation
class Edge:
    def __init__(self, type, srcId, dstId, attrs):
        self.srcId = srcId
        self.dstId = dstId
        self.type = type
        self.attrs = attrs
        self.id = str(uuid4())
    def __str__(self):
        return self.srcId + " " + self.dstId
    def toDotArgs(self):
        return self.srcId, self.dstId

class ArrowEdge(Edge):
    def __init__(self, type, srcId, dstId, attrs):
        super().__init__(type, srcId, dstId, attrs)
    def __str__(self):
        return self.srcId + " " + self.type + " " + self.dstId
    def toDotArgs(self):
        relationType = self.attrs['relation']
        if relationType == TypeRelation.Extend or relationType == TypeRelation.Include:
            return self.srcId, self.dstId, { 'style': 'dashed' }
        elif relationType == TypeRelation.OneToOne:
            return self.srcId, self.dstId, { 'style': 'solid' }
        elif relationType == TypeRelation.OneToMany:
            return self.srcId, self.dstId, { 'style': 'dashed' }
        elif relationType == TypeRelation.ManyToMany:
            return self.srcId, self.dstId, { 'style': 'solid' }
        else:
            return self.srcId, self.dstId, { }

class EdgeFactory:
    @singledispatch
    def create(token):
        raise NotImplementedError
    @create.register(ArrowToken)
    def _(token: ArrowToken):
        return Edge(token.typeRelation, token.source, token.target)