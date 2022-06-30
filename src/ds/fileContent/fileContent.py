# abstract class FileContent
# Define how content read from file is stored

import json
from functools import singledispatch
from ds.object.flexible import FlexibleObject
class JSONFileContent(FlexibleObject):
    def __init__(self):
        super().__init__()

    def __read__():
        pass

class FileContent(FlexibleObject):
    instance = dict()
    def __init__(self, file_type):
        super().__init__()
        self.type = "FileContent"
        self['file_type'] = file_type
        self['content'] =  None
        self.read = singledispatch(self.read)

        self.read.register(JSONFileContent, JSONFileContent.__read__)

    def read(self, s):
        raise TypeError("This type isn't supported: {}".format(type(s)))

    

