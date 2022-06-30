# class Reader (define how content is read with different file formats)
# - Read file module applied Flexible object (format - stategy to read). 
# - Input: file name
# - Output: instance of FileContent
# - Use Strategy design pattern to read the file (based on its extension).

from ds.fileContent.fileContent import FileContent
from ds.object.flexible import FlexibleObject


class Reader(FlexibleObject):
    def __init__(self, file_path):
        super().__init__()
        self['input'] = self.absolute_path(file_path)
        self['input_type'] = self.get_extension(file_path)
        self['output'] = FileContent()

    def absolute_path(self, file):
        return ""

    def get_extension(self, file):
        return "json"

    def stragety(self):
        pass
        
        
        

    