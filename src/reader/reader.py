# class Reader (define how content is read with different file formats)
# - Read file module applied Flexible object (format - stategy to read). 
# - Input: file name
# - Output: instance of FileContent
# - Use Strategy design pattern to read the file (based on its extension).


from ds.fileContent.fileContent import FileContent
from ds.fileContent.method import FileContentMethod
from ds.object.flexible import FlexibleObject
import os

class Reader():
    def __init__(self, file_path):
        # super().__init__()
        self.type = "Reader"
        # input relative path with main.py
        # --> relative paht with reader.py
        self.file = file_path 
        self.file_name, self.extension = os.path.splitext(self.file)
        self.fileContent = None

    def stragety(self) -> None:
        self.fileContent = FileContent()
        self.fileContent.assing_method(Reader.select_type_file_content(self.extension))
        self.fileContent.read(self.file)       

    def select_type_file_content(extension: str):
        method = FileContentMethod.instance[extension[1:]]
        if not method:
            raise TypeError("This type isn't supported: {}".format(type(extension)))
        return method

    def get_output(self):
        return self.fileContent.data