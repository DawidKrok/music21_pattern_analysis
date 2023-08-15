from music21 import *
from realization import *
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import matplotlib.pyplot as plt

'''
How similiar two realizaitons must be to be included in a motive ( `range<0, 2>` )
'''
B_PARAM = 1.5


def get_motive(notes: list[note.Note], k: int) -> list[Realization]:
    '''
    Goes trough the list of notes from a `Stream` (musical score) and makes a set of realizations of length `k`.
    Only the realizations that are similiar enough between each other (similiarity score stronger than `B_PARAM`) are included.
    '''
    reals = []  # all Realizations of length k in given Stream s
    motive = [] # all Realizations that are similiar to any other realization with score greater than B_PARAM


    # get all realizations of length k
    for i in range(len(notes) - k + 1):
        reals.append(Realization(notes[i:i+k]))

    # get all the possible pairs of realizations
    pairs = [(a, b) for idx, a in enumerate(reals) for b in reals[idx + 1:]]

    # filter those pairs based on B_PARAM. Exclude duplicates
    for pair in pairs:
        if realization_similiarity(*pair) >= B_PARAM:
            if pair[0] not in motive: motive.append(pair[0])
            if pair[1] not in motive: motive.append(pair[1])

    return motive

def motive_similiarity(m1: list[Realization], m2: list[Realization]) -> float:
    '''
    Computes ratio of identical realizations to all realizations in both motives  (Jaccard's coefficient) 
    '''
    if len(m1) == 0 or len(m2) == 0:  return 0
    if len(m1[0]) != len(m2[0]):    raise Exception("Motives have different lengths")

    # count how many exactly equal Realizations are between two motives
    equals = 0
    for r1 in m1:
        for r2 in m2:
            if r1 == r2: equals+=1

    return equals / (len(m1) + len(m2) - equals)

def get_composition(s: stream.Stream) -> list[list[Realization]]:
    '''
    Makes a set of motives of different lenghts (2 to 7) out of given `Stream` (musical score)
    '''
    c = []
    # get rid of all the wrappers around notes
    notes = list(s.flatten().notes)
    notes = list(filter(lambda n: 
                type(n) == note.Note and n.duration.quarterLength != 0
            , notes))

    print("Notes in composition:", len(notes))
    for k in range(2, 7):
        c.append(get_motive(notes, k))

    return c

def composition_similiarity(c1: list[list[Realization]], c2: list[list[Realization]]) -> float:
    '''
    Arithmetic sum of motives similiarity

    There were supposed to be some v_matrix that filters only the best motives matches, 
    but for each k there's only one motive to match, so dunno what was meant by that
    '''

    similiarity = 0

    # Normally never gonna happen, but just in case 
    if len(c1) != len(c2): return 0

    # go trough all k lenghts
    for k in range(len(c1)):
        similiarity += motive_similiarity(c1[k], c2[k])

    return similiarity


def show_dendrogram(compositions: list[list[list[Realization]]], labels: list):
    # Make a matrix with similiarity scores between each composition (1 if it's the same composition, so it wouldn't have too big distances between each other)
    X: list[list[float]] = []
    for i in range(len(compositions)):
        X.append([])
        for j in range(len(compositions)):
            if i == j:
                X[-1].append(1)
                continue
            X[-1].append(composition_similiarity(compositions[i], compositions[j]))

    Z = linkage(X)
    fig = plt.figure(figsize=(15, 10))
    dn = dendrogram(Z, labels=labels)

    fig.show()
