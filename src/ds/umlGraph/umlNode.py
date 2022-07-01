class Node:
    def __init__(self, name, type, attributes):
        self.name = name
        self.type = type
        self.id = str(uuid4())
        self.attributes = attributes
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

class NodeFactory:
    @singledispatch
    def create(self, token):
        raise NotImplementedError
    @create.register(UsecaseToken)
    def _(self, token):
        return Node(token)
    @create.register(ClassToken)
    def _(self, token):
        return Node(token)
    @create.register(ArrowToken)
    def _(self, token):
        return Node()