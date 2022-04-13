from StringToDrum import *
from copy import deepcopy

strTest1 = "xo[xo]"

sHit = Hit([drumdict['o']], 0, 0)
kHit = Hit([drumdict['x']], 0, 0)
hHit = Hit([drumdict['-']], 0, 0)
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

m1 = Measure([sHit, sub1, kHit, sub2, sim1, sub3])

p = MeasureParser(m1)
p.printevents()