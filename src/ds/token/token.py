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
    __attribute = None   #Type of relation of arrow
    def __init__(self, typeToken, source, target, attributes):
        super().__init__(typeToken)
        self.__source = source
        self.__target = target
        self.__attribute = attributes

    def getSource(self):
        return self.__source

    def getTarget(self):
        return self.__target

    def getAttributes(self):
        return self.__attribute

class UsecaseToken(Token):
    __name = None         #Name of usecase
    __group = None        #Group ID
    def __init__(self, typeToken, name, group, attributes):
        super().__init__(typeToken)
        self.__name = name
        self.__group = group
        self.__attributes = attributes

    def getName(self):
        return self.__name

    def getGroup(self):
        return self.__group

class ClassToken(Token):
    __name = None         #Name of class
    __group = None        #Group ID of classes
    __attributes = None   #List attributes of a class
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
    
    
        
