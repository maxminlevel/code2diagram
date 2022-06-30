from collections import UserDict
from typing import Any

class FlexibleObject(UserDict):
    def _lookup(self, name):
        for item in self.data:
            if item.id == name:
                return item

    def __getitem__(self, name):
        return self._lookup(name)

    def __call__(self, name):
        return self._lookup(name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        return super().__setattr__(__name, __value)

a = FlexibleObject()

