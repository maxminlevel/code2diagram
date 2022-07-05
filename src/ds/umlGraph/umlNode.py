from functools import singledispatch
from uuid import uuid4
from ds.token.token import ArrowToken, ClassToken, UsecaseToken, ActorToken
import graphviz
class Node:
    def __init__(self, name, groupId, attributes):
        self.name = name
        self.id = str(uuid4())
        self.groupId = groupId
        self.attributes = attributes
    def __str__(self):
        return self.name

class ActorNode(Node):
    def __init__(self, name, groupId, attributes):
        super().__init__(name, groupId, attributes)
    def __str__(self):
        return self.name
    def toUMLAgrs(self):
        return self.id, self.name
class UsecaseNode(Node):
    def __init__(self, name, groupId, attributes):
        super().__init__(name, groupId, attributes)
    def __str__(self):
        return self.name
    def toUMLAgrs(self):
        return self.id, self.name

class NodeFactory:
    @singledispatch
    def create(token):
        raise NotImplementedError
    @create.register(UsecaseToken)
    def _(token: UsecaseToken):
        return Node(token.name, token.groupId, None)
    @create.register(ActorToken)
    def _(token: ActorToken):
        return Node(token.name, token.groupId, None)
    @create.register(ClassToken)
    def _(token: ClassToken):
        return Node(token.name, token.groupId, token.attributes)
