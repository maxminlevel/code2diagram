from functools import singledispatch
import os
from pathlib import Path
from uuid import uuid4
from ds.token.token import ArrowToken, ClassToken, UsecaseToken, ActorToken
import graphviz
class Node:
    def __init__(self, id, name, groupId, attributes):
        self.name = name
        self.id = id
        self.groupId = groupId
        self.attributes = attributes
    def __str__(self):
        return self.name
    def toDotArgs(self):
        return self.id, self.name, {}
class ActorNode(Node):
    def __init__(self, id, name, groupId, attributes):
        super().__init__(id, name, groupId, attributes)
    def __str__(self):
        return self.name
    def toDotArgs(self):
        basedir = Path(os.path.abspath(os.path.dirname(__file__)))
        
        return self.id, self.name, {
            'image': os.path.join(basedir.parent, 'umlGraph/images', 'actor.png'),
            'shape': 'none',
            'height': '1.9',
            'width': '1.9',
        }
class UsecaseNode(Node):
    def __init__(self, id, name, groupId, attributes):
        super().__init__(id, name, groupId, attributes)
    def __str__(self):
        return self.name
    def toDotArgs(self):
        return self.id, self.name, {}

class NodeFactory:
    @singledispatch
    def create(token):
        raise NotImplementedError
    @create.register(UsecaseToken)
    def _(token: UsecaseToken):
        return UsecaseNode(token.id, token.name, token.groupId, None)
    @create.register(ActorToken)
    def _(token: ActorToken):
        return ActorNode(token.id, token.name, token.groupId, None)
    @create.register(ClassToken)
    def _(token: ClassToken):
        return Node(token.id, token.name, token.groupId, token.attributes)
