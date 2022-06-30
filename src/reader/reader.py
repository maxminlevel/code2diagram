# class Reader (define how content is read with different file formats)
# - Read file module applied Flexible object (format - stategy to read). 
# - Input: file name
# - Output: instance of FileContent
# - Use Strategy design pattern to read the file (based on its extension).

import json
from ds.fileContent.fileContent import FileContent
from ds.object.flexible import FlexibleObject


class Reader(FlexibleObject):
    def __init__(self, file_path):
        super().__init__()
        self.input = self.absolute_path(file_path)
        self.input_type = self.get_extension(file_path)
        self.output = FileContent()

    def absolute_path(self, file):
        return ""

    def get_extension(self, file):
        return "json"

    def stragety(self):
        self.output

    def get_output(self):
        obj = {"attribute": {"name": "Simple","type": "Usecase"},"data": [{"name": "Man","uniq": "1","type": "actor","group": "","attribute": {}},{"name": "do some thing","uniq": "2","type": "usecase","group": "","attribute": {}},{"source": 1,"target": 2,"attribute": {}}]}        
        data = json.loads(obj)
        return data

        
        
        

    