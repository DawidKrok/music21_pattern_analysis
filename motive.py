from music21 import *
from realization import *
import itertools

'''
How similiar two realizaitons must be to be included in a motive ( `range<0, 2>` )
'''
B_PARAM = 1.3


def get_motive(s: stream.Stream, k: int) -> list[Realization]:
    '''
    Goes trough the whole `Stream` (musical score) and makes a set of realizations of length `k`.
    Only the realizations that are similiar enough between each other (similiarity score stronger than `B_PARAM`) are included.
    '''
    reals = []  # all Realizations of length k in given Stream s
    motive = [] # all Realizations that are similiar to any other realization with score greater than B_PARAM

    # get rid of all the wrappers around notes
    notes = s.flatten()
    notes = list(filter(lambda n: 
                type(n) == note.Note
            , notes))

    for i in range(len(notes) - k + 1):
        reals.append(Realization(notes[i:i+k]))
    # if score == 2 we shall discard a realization as an equal realization already exists and a copy would misrepresent the final similiarity
    pairs = [(a, b) for idx, a in enumerate(reals) for b in reals[idx + 1:]]

    for pair in pairs:
        if realization_similiarity(*pair) >= B_PARAM:
            if pair[0] not in motive: motive.append(pair[0])
            if pair[1] not in motive: motive.append(pair[1])

    return motive

def motive_similiarity(m1: list[Realization], m2: list[Realization]) -> float:
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
