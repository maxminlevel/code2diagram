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
    @staticmethod
    @singledispatch
    def create(self, token):
        raise NotImplementedError
    @create.register(UsecaseToken)
    def _(self, token: UsecaseToken):
        return Node(token.getName, token.getGroupId, None)
    @create.register(ActorToken)
    def _(self, token: ActorToken):
        return Node(token.getName, token.getGroupId, None)
    @create.register(ClassToken)
    def _(self, token: ClassToken):
        return Node(token.getName, token.getGroupId, token.getAttributes)
