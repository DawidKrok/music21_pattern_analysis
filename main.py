from lib import *
from music21 import *

l = [note.Note("A2"), note.Note("B2"), note.Note("C2"), note.Note("D2"), note.Note("E2"), note.Note("F2"), note.Note("G2")]
r = get_realization(l)
print(r)

s = stream.Stream(l)
# s.show()

i = interval.Interval(note.Note("a2"), note.Note("b#2"))
print(i.semitones)