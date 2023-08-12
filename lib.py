from music21 import *

###   ===== WHEN RUNNING FOR THE FIRST TIME =====   ###
# configure.run()
###   ===========================================   ###

### REALIZATION - Tuple with features of notes sequence of length k
### MOTIVE      - Set of similiar realizations of length k
### COMPOSITION - Set of motives in a score with different lengths k


'''
How similiar two realizaitons must be to be included in a motive ( `range<0, 2>` )
'''
B_PARAM = 1.5

def get_realization(notes: list[note.Note]) -> tuple:
    '''
    returns a tuple of notes sequence features

    (diatonic intervals, chromatic intervals, contour, rhytmic value)
    '''
    di = []
    ci = []
    co = []
    rv = []
    for i in range(len(notes) - 1):
        inter = interval.Interval(notes[i], notes[i+1])

        # Chromatic interval
        di.append(inter.generic.staffDistance)

        # Diatonic interval
        ci.append(inter.semitones)

        # Contour
        co.append(inter.diatonic.direction.value)

        # Rhytmic value
        rv.append(notes[i].duration.quarterLength)

    # get the last note's rhytmic value
    rv.append(notes[-1].duration.quarterLength)

    return (ci, di, co, rv)
 
def realization_similiarity(r1: tuple, r2: tuple) -> float:
    '''
    Computes similiarity coefficient of two realizations (should be the same length)
    '''
    pass

def get_motive(s: stream.Stream, k: int) -> list[tuple]:
    '''
    Goes trough the whole `Stream` (musical score) and makes a set of realizations of length `k`.
    Only the realizations that are similiar enough between each other (similiarity score stronger than `B_PARAM`) are included.
    '''
    pass

def motive_similiarity(m1: list[tuple], m2: list[tuple]) -> float:
    '''
    Computes ratio of identical realizations to all realizations in both motives  (Jaccard's coefficient) 
    '''
    pass

def get_composition(s: stream.Stream) -> list[list[tuple]]:
    '''
    Makes a set of motives of different lenghts (2 to 7) out of given `Stream` (musical score)
    '''
    pass

def composition_similiarity(c1: list[list[tuple]], c2: list[list[tuple]]) -> float:
    '''
    Arithmetic sum of motives similiarity, but only the best ones

    TODO: Compute similiarities of all motives beforehand and include the best one from each column/row?
    It should maximize the similiarity output keeping the constraint:
    Each motive has only one best fitted motive from the other composition (compared between motives of the same length)
    '''
    pass
