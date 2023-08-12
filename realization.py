from music21 import *


class Realization:

    def __init__(self, notes: list[note.Note]):
        '''
        returns a tuple of notes sequence features

        (diatonic intervals, chromatic intervals, contour, rhytmic value)
        '''
        self.diatonic_interval = []
        self.chromatic_interval = []
        self.contour = []
        self.rhytmic_values = []
        
        for i in range(len(notes) - 1):
            inter = interval.Interval(notes[i], notes[i+1])

            # Chromatic interval
            self.diatonic_interval.append(inter.generic.staffDistance)

            # Diatonic interval
            self.chromatic_interval.append(inter.semitones)

            # Contour
            self.contour.append(inter.diatonic.direction.value)

            # Rhytmic value
            self.rhytmic_values.append(notes[i].duration.quarterLength)

        # get the last note's rhytmic value
        self.rhytmic_values.append(notes[-1].duration.quarterLength)


def realization_similiarity(r1: Realization, r2: Realization) -> float:
    '''
    Computes similiarity coefficient of two realizations (should be the same length)
    '''
    similiarity = 0.
    # The shorter length is used as all similiarity scoring is done on values that are relative to their consecutive notes
    k = len(r1.chromatic_interval)
    
    if k != len(r2.chromatic_interval): raise Exception("Realizations have different lenghts")

    # Compare ratio of consecutive rhytmic values (max 1 point)
    for rv1, rv2 in zip(
        zip(r1.rhytmic_values, r1.rhytmic_values[1:]),
        zip(r2.rhytmic_values, r2.rhytmic_values[1:])
    ):
        if rv1[0]/rv1[1] == rv2[0]/rv2[1]:
            similiarity += 1./k

    # Compare melodic characteristic and assign similiarity score based on Laskowska's model
    for i in range(k):
        if (r1.diatonic_interval[i] == r2.diatonic_interval[i]) or (r1.chromatic_interval[i] == r2.chromatic_interval[i]):
            if r1.contour[i] == r2.contour[i]:      similiarity += 1./ k
            else:                                   similiarity += 1./ k / 2
        elif   r1.contour[i] == r2.contour[i]:      similiarity += 1./ k / 3

    return similiarity

