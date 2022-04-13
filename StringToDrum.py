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
        self.events = [] 
        self.parse()

    def printevents(self):
        for e in self.events:
            print("Inst: ", e.instNums, ", Start: ", e.start, ", Stop: ", e.stop)
    
    def simultaneous(self, siml, start, stop):
        while(len(siml.items)):
            item = siml.items.pop(0)
            if isinstance(item, Hit):
                item.start = start
                item.stop = stop
                self.events.append(item)
                continue
            elif isinstance(item, Subdivision):
                self.subdivision(item, start, stop)
                continue
            elif isinstance(item, Simultaneous):
                self.simultaneous(item, start, stop)
                continue
            else:
                print("unknown type in MeasureParser.simultaneous")

    
    def subdivision(self, subd, start, stop):
        timestep = (stop - start)/len(subd.items)
        stop = start + timestep
        while(len(subd.items)):
            item = subd.items.pop(0)
            if isinstance(item, Hit):
                item.start = start
                item.stop = stop
                self.events.append(item)
                start += timestep
                stop += timestep
                continue
            elif isinstance(item, Subdivision):
                self.subdivision(item, start, stop)
                start += timestep
                stop += timestep
                continue
            elif isinstance(item, Simultaneous):
                self.simultaneous(item, start, stop)
                start += timestep
                stop += timestep
                continue
            else:
                print("unknown type in MeasureParser.subdivision")
            
    def parse(self):
        start = 0
        stop = 1
        while (len(self.measure.items)):
            item = self.measure.items.pop(0)
            if isinstance(item, Hit):
                item.start = start
                item.stop = stop
                self.events.append(item)
                start += 1
                stop += 1
                continue
            elif isinstance(item, Subdivision):
                self.subdivision(item, start, stop)
                start += 1
                stop += 1
                continue
            elif isinstance(item, Simultaneous):
                self.simultaneous(item, start, stop)
                start += 1
                stop += 1
                continue
            else:
                print("unknown type in MeasureParser.parse")