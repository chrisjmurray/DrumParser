# bass drum 36
# snare 38
# closed hi hat 42
# open hi hat 46

class Hit:
    def __init__(self, instNum = 0, start = 0.0, stop = 0.0):
        self.instNum = instNum
        self.start = start
        self.stop = stop

    def getduration(self):
        return self.stop-self.stop


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

class MeasureParser:
    def __init__(self, measure):
        self.measure = measure
        self.events = [] 
        self.parse()

    def printevents(self):
        for e in self.events:
            print("Inst: ", e.instNum, ", Start: ", e.start, ", Stop: ", e.stop)
    
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

class DrumParser:
    def __init__(self, string, drumdict):
        self.s = list(string)
        self.dd = drumdict
        self.measure = Measure()
        self.parse()

    def simultaneous(self, parentitem):
        
        while(len(self.s)):
            ch = self.s.pop(0)
            if ch in self.dd.keys():
                parentitem.additem(Hit(self.dd[ch]))
            elif ch == '(':
                siml = Simultaneous()
                parentitem.additem(self.simultaneous(siml))
            elif ch == '[':
                subd = Subdivision()
                parentitem.additem(self.subdivision(subd))
            elif ch == ')':
                break
        return parentitem

    def subdivision(self, parentitem):
        while(len(self.s)):
            ch = self.s.pop(0)
            if ch in self.dd.keys():
                parentitem.additem(Hit(self.dd[ch]))
            elif ch == '[':
                subd = Subdivision()
                parentitem.additem(self.subdivision(subd))
            elif ch == '(':
                siml = Simultaneous()
                parentitem.additem(self.simultaneous(siml))
            elif ch == ']':
                break
            else:
                print("invalid character")
        return parentitem
        
    def parse(self):
        while(len(self.s)):
            ch = self.s.pop(0)
            if ch in self.dd.keys():
                self.measure.additem(Hit(instNum = self.dd[ch]))
            elif ch == '(':
                siml = Simultaneous()
                self.measure.additem(self.simultaneous(siml))
            elif ch == '[':
                subd = Subdivision()
                self.measure.additem(self.subdivision(subd))
            else:
                print("invalid character")
