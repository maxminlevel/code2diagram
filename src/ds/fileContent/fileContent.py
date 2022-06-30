# abstract class FileContent
# Define how content read from file is stored

from ds.object.flexible import FlexibleObject
class FileContent(FlexibleObject):
    def __init__(self):
        super().__init__()
        self.type = "FileContent"
        self['__file_type__'] = ""
        

class JSONFileContent(FileContent):
    def __init__(self):
        super().__init__()
