from abc import abstractmethod
from ds.object.flexible import FlexibleObject
import json
from ds.token.token import*

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
        contentJson = json.loads(fileContent)
        listTokens = []
        for item in contentJson["data"]:
            token = None
            if item['type'] == "actor":
                groupId = item['group']
                if groupId is None:
                    token = ActorToken(item["type"], item["name"])
                else:
                    token = ActorToken(item["type"], item["name"], groupId)
            elif item["type"] == "arrow":
                token = ArrowToken(item["type"], item["source"], item["target"], item['attribute'])
            elif item["type"] == "usecase":
                token = UsecaseToken(item["type"], item["name"], item["group"])
            elif item["type"] == "class":
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
