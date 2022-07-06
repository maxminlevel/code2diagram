from functools import singledispatch
from uuid import uuid4

import graphviz

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
        if self.attrs is not None and 'relation' in self.attrs:
            relationType = self.attrs['relation']
            if relationType == TypeRelation.Extend or relationType == TypeRelation.Include:
                return self.srcId, self.dstId, { 'style': 'dashed', 'label': graphviz.nohtml("<<{0}>>".format(relationType))}
            elif relationType == TypeRelation.OneToOne:
                return self.srcId, self.dstId, { 'style': 'solid' }
            elif relationType == TypeRelation.OneToMany:
                return self.srcId, self.dstId, { 'style': 'solid' }
            elif relationType == TypeRelation.ManyToMany:
                return self.srcId, self.dstId, { 'style': 'solid' }
        return self.srcId, self.dstId, { }

class EdgeFactory:
    @singledispatch
    def create(token):
        raise NotImplementedError
    @create.register(ArrowToken)
    def _(token: ArrowToken):
        return ArrowEdge(token.type, token.source, token.target, token.attribute)