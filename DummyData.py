from StringToDrum import *
from copy import deepcopy



sHit = Hit(drumdict1['o'])
kHit = Hit(drumdict1['x'])
hHit = Hit(drumdict1['-'])
sub1 = Subdivision()
sub1.additem(deepcopy(sHit))
sub1.additem(deepcopy(sHit))
sub1.additem(deepcopy(kHit))
sub2 = Subdivision()
sub2.additem(deepcopy(kHit))
sub2.additem(deepcopy(kHit))
sub3 = Subdivision()
sub3.additem(deepcopy(sub2))
sub3.additem(deepcopy(kHit))
sim1 = Simultaneous()
sim1.additem(deepcopy(sub1))
sim1.additem(deepcopy(sub2))
sim1.additem(deepcopy(hHit))

#m1 = Measure([sHit, sub1, kHit, sub2, sim1, sub3])

#p = MeasureParser(m1)
#p.printevents()
strTest1 = "xo[xo](xo)"
strTest2 = "[x[xo](xo)]([xoo][xo])"
s = DrumParser(strTest2, drumdict1)
p1 = MeasureParser(s.measure)
p1.printevents()