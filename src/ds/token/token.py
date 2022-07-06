# Contain information about each token of our language
import enum
from itertools import count
from ds.umlGraph.umlGraphConfig import ACTOR_TYPE, USECASE_TYPE, ARROW_TYPE, CLASS_TYPE
class TypeToken(enum.Enum):
    Actor = ACTOR_TYPE
    Usecase = USECASE_TYPE
    Class = CLASS_TYPE
    Arrow = ARROW_TYPE

class TypeRelation(enum.Enum):
    ISA = 'isa'
    Extend = 'extend'
    Include = 'include'
    OneToOne = 'oneToOne'
    OneToMany = 'oneToMany'
    ManyToMany = 'manyToMany'

class Token(object):
    __typeToken = None
    __idToken = None
    def __init__(self, typeToken : TypeToken, uid = None):
        self.__typeToken = typeToken
        self.__idToken = uid

    @property
    def type(self):
        return self.__typeToken

    @property
    def id(self):
        return self.__idToken

    def __str__(self) -> str:
        pass

    

class ActorToken(Token):
    __name = None
    __groupId = None
    def __init__(self, typeToken, uid, name, groupId = None):
        super().__init__(typeToken, uid)
        self.__name = name
        self.__groupId = groupId

    @property
    def name(self):
        return self.__name

    @property
    def groupId(self):
        return self.__groupId

    def __str__(self) -> str:
        return self.type + " " + self.name + " " + self.groupId

class ArrowToken(Token):
    __source = None
    __target = None
    __typeRelation = None   #Type of relation of arrow
    def __init__(self, typeToken, source, target, typeRelation: TypeRelation, attribute = None):
        super().__init__(typeToken)
        self.__source = source
        self.__target = target
        self.__typeRelation = typeRelation
        self.__attribute = attribute

    @property
    def source(self):
        return self.__source

    @property
    def target(self):
        return self.__target

    @property
    def typeRelation(self):
        return self.__typeRelation

    @property
    def attribute(self):
        return self.__attribute

    def __str__(self) -> str:
        return self.type + " " + str(self.source) + " " + str(self.target) + " " + str(self.typeRelation)

class UsecaseToken(Token):
    __name = None         #Name of usecase
    __groupId = None        #Group ID
    def __init__(self, typeToken, uid, name, groupId):
        super().__init__(typeToken, uid)
        self.__name = name
        self.__groupId = groupId

    @property
    def name(self):
        return self.__name

    @property
    def groupId(self):
        return self.__groupId
    
    def __str__(self) -> str:
        return self.type + " " + self.name + " " + self.groupId

    

class ClassToken(Token):
    __name = None         #Name of class
    __groupId = None        #Group ID of classes
    __attributes = None   #List attributes of a class
    def __init__(self, typeToken, uid, name, groupId, attributes):
        super().__init__(typeToken, uid)
        self.__name = name
        self.__groupId = groupId
        self.__attributes = attributes

    @property
    def name(self):
        return self.__name

    @property
    def groupId(self):
        return self.__groupId

    @property
    def attributes(self):
        return self.__attributes  
    
    def __str__(self) -> str:
        return self.type + " " + self.name + " " + self.groupId + " " + self.attributes
