from realization import *
from music21 import *
from motive  import *

###   ===== WHEN RUNNING FOR THE FIRST TIME =====   ###
# configure.run()
###   ===========================================   ###

### REALIZATION - Tuple with features of notes sequence of length k
### MOTIVE      - Set of similiar realizations of length k
### COMPOSITION - Set of motives in a score with different lengths k

l = [note.Note("A2"), note.Note("A#2", type="16th"), note.Note("C2", type="half"), note.Note("G#2"), note.Note("G#2"), note.Note("C2", type="eighth"), note.Note("G2", type="16th")]
l2 = [note.Note("A#2"), note.Note("A#2", type="16th"), note.Note("C2"), note.Note("G#2", type="half"), note.Note("G#2"), note.Note("F2", type="eighth"), note.Note("G2")]
r = Realization(l)
r2 = Realization(l2)

s = corpus.parse("bwv57.8")
s2= corpus.parse("bwv256")
# s.show()
k=4

m = get_motive(s, k)
m2 = get_motive(s2, k)
# print(realization_similiarity(r, r2))
print(motive_similiarity(m, m2))