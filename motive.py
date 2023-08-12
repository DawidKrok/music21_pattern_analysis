from music21 import *
from realization import *

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
