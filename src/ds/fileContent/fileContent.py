# abstract class FileContent
# Define how content read from file is stored

# from functools import singledispatch

from ds.fileContent.method import FileContentMethod
class FileContent():
    def __init__(self):
        self.type = "FileContent"
        self.method = None
        # self.read = singledispatch(self.read)
        # self.read.register(JSON, JSON.__read__)
        self.data = None

    def read(self, file_path):
        self.data = self.method.read(file_path)
        return self.data

    def assing_method(self, method: FileContentMethod):
        self.method = method

    def __str__(self) -> str:
        return str(self.data)