from enum import Enum


class AddMode(Enum):
    DEFAULT = 0
    OPT_ARG = 1
    ENV = 2
    MATRIX = 3
    LIM = 4

class AddModes:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_mode_stack = [ AddMode.DEFAULT ]

    def pushAddMode(self, mode: AddMode):
        self.add_mode_stack.append(mode)

    def popAddMode(self) -> AddMode:
        return self.add_mode_stack.pop()

    def remAddMode(self, mode: AddMode):
        self.add_mode_stack.reverse()
        self.add_mode_stack.remove(mode)
        self.add_mode_stack.reverse()

    def topAddMode(self) -> AddMode:
        return self.add_mode_stack[-1]

    def hasAddMode(self, mode: AddMode) -> bool:
        return mode in self.add_mode_stack

