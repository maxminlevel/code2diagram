from abc import abstractmethod
from typing import Any
from xml.dom.minidom import Element
from ds.object.flexible import FlexibleObject


class FileContentMethod(FlexibleObject):
    instance = dict()
    def __init__(self, type):
        super().__init__()
        self.type = "FileContentMethod"
        self.file_type = type
        FileContentMethod.instance[type] = self

    @abstractmethod
    def read(self, filename) -> Any:
        pass

class JSON_input(FileContentMethod): 
    def __init__(self):
        super().__init__('json')

    def read(self, filename) -> dict:
        with open(filename, 'r') as f:
            import json
            data = json.load(f)
            return data

class XML_input(FileContentMethod): 
    def __init__(self):
        super().__init__('xml')

    def read(self, filename) -> Element:
        with open(filename, 'r') as f:
            import xml.etree.ElementTree as ET
            tree = ET.parse(filename)
            root = tree.getroot()
            # https://docs.python.org/3/library/xml.etree.elementtree.html
            return root

class TXT_input(FileContentMethod): 
    def __init__(self):
        super().__init__('txt')

    def read(self, filename):
        with open(filename, 'r') as f:
            pass

class CSV_input(FileContentMethod): 
    def __init__(self):
        super().__init__('csv')

    def read(self, filename):
        with open(filename, 'r') as f:
            pass

JSON_input()
XML_input()
TXT_input()
CSV_input()
