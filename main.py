from realization import *
from music21 import *
from motive  import *
import time
import os

###   ===== WHEN RUNNING FOR THE FIRST TIME =====   ###
# configure.run()
###   ===========================================   ###

### REALIZATION - Tuple with features of notes sequence of length k
### MOTIVE      - Set of similiar realizations of length k
### COMPOSITION - Set of motives in a score with different lengths k ( range<2;7> )

print("wait...")
t = time.time() 

compositions = [ get_composition(converter.parse("xmls/" + s)) for s in os.listdir("xlms") ]


show_dendrograf(compositions)

print("done in", time.time() - t, "seconds")
input()