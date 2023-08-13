from realization import *
from music21 import *
from motive  import *
import time

###   ===== WHEN RUNNING FOR THE FIRST TIME =====   ###
# configure.run()
###   ===========================================   ###

### REALIZATION - Tuple with features of notes sequence of length k
### MOTIVE      - Set of similiar realizations of length k
### COMPOSITION - Set of motives in a score with different lengths k

print("wait...")
t = time.time() 

s = corpus.parse("bwv57.8")
s2= corpus.parse("bwv256")

c = get_composition(s)
c2 = get_composition(s2)

print("done in", time.time() - t, "seconds")