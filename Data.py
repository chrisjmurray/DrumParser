from StringToDrum import *
from copy import deepcopy

drumdict1 = {'x': 36, 'o': 38, '-': 42, '=': 46, ' ': 0}

strTest1 = "xo[xo](xo)"
strTest2 = "[x[xo](xo)]([xoo][xo])[x -=]x"
s = DrumParser(strTest2, drumdict1)
p1 = MeasureParser(s.measure)
p1.printevents()