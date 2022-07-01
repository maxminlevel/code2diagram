# Contain information about each token of our language
import enum

class TypeToken(enum.Enum):
    Actor = 1
    Usecase = 2
    Class = 3
    Arrow = 4

class TypeRelation(enum.Enum):
    ISA = 1
    Extend = 2
    Include = 3
    OneToOne = 4
    OneToMany = 5
    ManyToMany = 6

class Token(object):
    __typeToken = None
    def __init__(self, typeToken : TypeToken):
        self.__typeToken = typeToken

    @property
    def getTypeToken(self):
        return self.__typeToken

    def __str__(self) -> str:
        pass

class ActorToken(Token):
    __name = None
    __groupId = None
    def __init__(self, typeToken, name, groupId):
        super().__init__(typeToken)
        self.__name = name
        self.__groupId = groupId

    @property
    def getName(self):
        return self.__name

    @property
    def getGroupId(self):
        return self.__groupId

    def __str__(self) -> str:
        return self.getTypeToken + " " + self.getName + " " + self.getGroupId

class ArrowToken(Token):
    __source = None
    __target = None      
    __typeRelation = None   #Type of relation of arrow
    def __init__(self, typeToken, source, target, typeRelation: TypeRelation):
        super().__init__(typeToken)
        self.__source = source
        self.__target = target
        self.__typeRelation = typeRelation

    @property
    def getSource(self):
        return self.__source

    @property
    def getTarget(self):
        return self.__target

    @property
    def getTypeRelation(self):
        return self.__typeRelation

    def __str__(self) -> str:
        return self.getTypeToken + " " + str(self.getSource) + " " + str(self.getTarget) + " " + str(self.getTypeRelation)

class UsecaseToken(Token):
    __name = None         #Name of usecase
    __groupId = None        #Group ID
    def __init__(self, typeToken, name, groupId):
        super().__init__(typeToken)
        self.__name = name
        self.__groupId = groupId

    @property
    def getName(self):
        return self.__name

    @property
    def getGroupId(self):
        return self.__groupId
    
    def __str__(self) -> str:
        return self.getTypeToken + " " + self.getName + " " + self.getGroupId

    

class ClassToken(Token):
    __name = None         #Name of class
    __groupId = None        #Group ID of classes
    __attributes = None   #List attributes of a class
    def __init__(self, typeToken, name, groupId, attributes):
        super().__init__(typeToken)
        self.__name = name
        self.__groupId = groupId
        self.__attributes = attributes

    @property
    def getName(self):
        return self.__name

    @property
    def getGroupId(self):
        return self.__groupId

    @property
    def getAttributes(self):
        return self.__attributes  
    
    def __str__(self) -> str:
        return self.getTypeToken() + " " + self.getName() + " " + self.getGroupId() + " " + self.getAttributes()
