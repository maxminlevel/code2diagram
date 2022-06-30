from itertools import count
from typing import Any
class FlexibleObject():
    instance = dict()
    count = 0
    
    def __init__(self):
        self.attribute = dict()
        self.canAddNew = True
        self.id = count
        self.type = ""
        FlexibleObject.count += 1
        FlexibleObject.instance[self.id] = self

    def __disable_add_atrribute__(self):
        self.canAddNew = False

    def __getitem__(self, key: str) -> Any:
        if key in self.attribute:
            return self.attribute[key]
        else:
            return None
    
    def  __setitem__(self, key: str, value: Any) -> bool:
        if self.canAddNew or key in self.attribute.keys:
            self.attribute[key] = value
            return True
        else:
            return False

    def __str__(self):
        return str(self.attribute)
