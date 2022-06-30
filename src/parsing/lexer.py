# Create class Lexer parse codes to tokens:
# - For applying Visitor pattern, we use FileContent concrete classes as visitors
# - Has different overload parse methods for every FileContent concrete class
# - Input: Code content (FileContent)
# - Output: List of tokens 

from ds.token.token import *
import json
from functools import singledispatch

obj = '{"attribute": {"name": "Simple","type": "Usecase"},"data": [{"name": "Man","uniq": "1","type": "actor","group": "","attribute": {}},{"name": "do some thing","uniq": "2","type": "usecase","group": "","attribute": {}},{"source": 1,"target": 2, "type":"arrow", "attribute": {}}]}'

class Content(object): pass
class JsonContent(object): pass
class CsvContent(Content): pass
class XmlContent(Content): pass


class Lexer(object):
    
    def __init__(self):
        self.contentToToken = singledispatch(self.contentToToken)
        self.contentToToken.register(str, self._contentToToken_Json)
        self.contentToToken.register(CsvContent, self._contentToToken_Csv)
        self.contentToToken.register(XmlContent, self._contentToToken_Xml)
        
    def contentToToken(self, s):
        raise TypeError("This type isn't supported: {}".format(type(s)))

    def _contentToToken_Json(self, obj):
        contentJson = json.loads(obj)
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

    def _contentToToken_Csv(self, obj):
        print("CSV" +  str(obj))

    def _contentToToken_Xml(self, obj):
        print("XML" + str(obj))



lexer = Lexer()
csv = CsvContent()
xml = XmlContent()
content = Content()
content = csv
listTokens = lexer.contentToToken(obj)

print(listTokens)
print("\n")
for token in listTokens:
    print(token)

lexer.contentToToken(content)


