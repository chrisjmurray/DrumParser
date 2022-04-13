from StringToDrum import *

strTest1 = "xo[xo]"

sHit = Hit([drumdict['o']])
kHit = Hit([drumdict['x']])
hHit = Hit([drumdict['-']])
sub1 = Subdivision()
sub1.additem(sHit)
sub1.additem(sHit)
sub1.additem(kHit)
sub2 = Subdivision()
sub2.additem(kHit)
sub2.additem(kHit)
sub3 = Subdivision()
sub3.additem(sub2)
sub3.additem(kHit)
sim1 = Simultaneous()
sim1.additem(sub1)
sim1.additem(sub2)
sim1.additem(hHit)

m1 = Measure([sub1, sub2, sim1, sub3])