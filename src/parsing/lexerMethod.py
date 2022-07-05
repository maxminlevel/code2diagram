from abc import abstractmethod
from ds.object.flexible import FlexibleObject
import json
from ds.token.token import*
from ds.umlGraph.umlGraphConfig import ACTOR_TYPE, USECASE_TYPE, ARROW_TYPE, CLASS_TYPE

class LexerMethod(FlexibleObject):
    instance = dict()
    def __init__(self, type):
        super().__init__()
        self.type = "Analyze"
        self.file_type = type
        LexerMethod.instance[type] = self

    @abstractmethod
    def analyze(self, fileContent) -> list:
        pass

class JSON_input(LexerMethod): 
    def __init__(self):
        super().__init__('json')

    def analyze(self, fileContent):
        listTokens = []
        for item in fileContent["data"]:
            token = None
            if item['type'] == ACTOR_TYPE:
                groupId = item['group']
                if groupId is None:
                    token = ActorToken(item["type"], item["name"])
                else:
                    token = ActorToken(item["type"], item["name"], groupId)
            elif item["type"] == ARROW_TYPE:
                token = ArrowToken(item["type"], item["source"], item["target"], item['attribute'])
            elif item["type"] == USECASE_TYPE:
                token = UsecaseToken(item["type"], item["name"], item["group"])
            elif item["type"] == CLASS_TYPE:
                token = ClassToken(item["type"], item["name"], item["group"], item["attribute"])
            
            listTokens.append(token)
        
        return listTokens

class XML_input(LexerMethod): 
    def __init__(self):
        super().__init__('xml')

    def analyze(self, fileContent):
        pass

class CSV_input(LexerMethod): 
    def __init__(self):
        super().__init__('csv')

    def analyze(self, fileContent):
        pass

JSON_input()
XML_input()
CSV_input()
