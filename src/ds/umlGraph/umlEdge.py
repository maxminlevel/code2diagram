from functools import singledispatch
from uuid import uuid4

from ds.token.token import ArrowToken
class Edge:
    def __init__(self, name, type, attributes):
        self.srcId = attributes.srcId
        self.dstId = attributes.dstId
        self.type = type
        self.name = name
        self.id = str(uuid4())
    def __str__(self):
        return self.srcId + " " + self.name + " " + self.dstId
    def __repr__(self):
        return self.srcId + " " + self.name + " " + self.dstId

class EdgeFactory:
    @staticmethod
    @singledispatch
    def create(self, token):
        raise NotImplementedError
    @create.register(ArrowToken)
    def _(self, token):
        return Edge(token)