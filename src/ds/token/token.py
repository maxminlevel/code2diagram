# Contain information about each token of our language

class Token(object):
    __typeToken = None
    def __init__(self, typeToken):
        self.__typeToken = typeToken

    def getTypeToken(self):
        return self.__typeToken

class ActorToken(Token):
    __name = None
    __group = None
    def __init__(self, typeToken, name, group):
        super().__init__(typeToken)
        self.__name = name
        self.__group = group

    def getName(self):
        return self.__name

    def getGroup(self):
        return self.__group

class ArrowToken(Token):
    __source = None
    __target = None
    __attributes = None
    def __init__(self, typeToken, source, target, attributes):
        super().__init__(typeToken)
        self.__source = source
        self.__target = target
        self.__attributes = attributes

    def getSource(self):
        return self.__source

    def getTarget(self):
        return self.__target

    def getAttributes(self):
        return self.__attributes


class ClassToken(Token):
    __name = None
    __group = None
    __attributes = None
    def __init__(self, typeToken, name, group, attributes):
        super().__init__(typeToken)
        self.__name = name
        self.__group = group
        self.__attributes = attributes

    def getName(self):
        return self.__name

    def getGroup(self):
        return self.__group

    def getAttributes(self):
        return self.__attributes
    
    
        
