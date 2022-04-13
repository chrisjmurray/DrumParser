# bass drum 36
# snare 38
# closed hi hat 42
# open hi hat 46

from dataclasses import dataclass

drumdict = {'x': 36, 'o': 38, '-': 42, '=': 46}

@dataclass
class Hit:
    instNums: list
    start: float
    stop: float

class Subdivision:
    def __init__(self):
        self.items = []
    def additem(self, item):
        self.items.append(item)

class Simultaneous:
    def __init__(self):
        self.items = []
    def additem(self, item):
        self.items.append(item)

class Measure:
    def __init__(self, items = None):
        if items:
            self.items = items
        else:
            self.items = []
    def additem(self, item):
        self.items.append(item)


class StringStream:
    def __init__(self, s):
        self.s = list(s)
    def getnext(self):
        return self.s.pop(0)
    def putback(self):
        self.s.insert(0)
    def isempty(self):
        return (len(self.s) != 0)

class MeasureParser:
    def __init__(self, measure):
        self.measure = measure
        