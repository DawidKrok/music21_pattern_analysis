from lib import *
from music21 import *

l = [note.Note("A2"), note.Note("A#2", type="16th"), note.Note("C2", type="half"), note.Note("G#2"), note.Note("G#2"), note.Note("F2", type="eighth"), note.Note("G2")]
r = get_realization(l)
print(r)

s = stream.Stream(l)
# s.show()