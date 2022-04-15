# DrumParser
Output a midi file that plays a drum groove. 
## Usage
```python
from StringToDrum import std

drumstring = "xoxo[([--]x)=][([--]o)=]"*20

std(drumstring)
```

x kick drum
o snare drum
- closed hihat
= open hihat

In the above example, the first four symbols, xoxo, will land on quarter notes. Symbols nested in parenthesis are played simultaneously. Symbols nested in brackets will divide the beat/subdivision into equal parts. The grammar allows for some interesting possibilities. All the string examples are multiplied simply to increase the duration of the output midi file.

### Examples
```python
string = "(xo)"*100
```
play the snare and kick together on every beat

```python
string = "[xo]"*100
```
play the kick on the downbeat and the snare on the eighth.

```python
string = "([xx][ooo])"*100
```
play eighth note kicks and triplet eighth note snares on top of each other.

