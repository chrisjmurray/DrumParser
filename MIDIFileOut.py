from midiutil import MIDIFile
from StringToDrum import *

drumdict1 = {'x': 36, 'o': 38, '-': 42, '=': 46, ' ': 0}
degrees  = [36, 38, 36, 38, 36, 38, 36, 38]  # MIDI note number
track    = 0
channel  = 10
time     = 0    # In beats
duration = .1    # In beats
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)
strTest1 = "xo[xo](xo)"*10
strTest2 = "[x[xo](xo)]([xoo][xo])[x -=]x"*10
s = DrumParser(strTest2, drumdict1)
p1 = MeasureParser(s.measure)
p1.printevents()
for e in p1.events:
    MyMIDI.addNote(track, channel, e.instNum, e.start*.5, duration, volume)
    

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)