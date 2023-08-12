from music21 import *


class Realization:

    def __init__(self, notes: list[note.Note]):
        '''
        contains notes sequence features

        (diatonic intervals, chromatic intervals, contour, rhytmic ratio)
        '''
        self.diatonic_interval = []
        self.chromatic_interval = []
        self.contour = []
        self.rhytmic_ratio = []
        
        for i in range(len(notes) - 1):
            inter = interval.Interval(notes[i], notes[i+1])

            # Chromatic interval
            self.diatonic_interval.append(inter.generic.staffDistance)

            # Diatonic interval
            self.chromatic_interval.append(inter.semitones)

            # Contour
            self.contour.append(inter.diatonic.direction.value)

            # Rhytmic ratio
            self.rhytmic_ratio.append(notes[i].duration.quarterLength / notes[i+1].duration.quarterLength)


def realization_similiarity(r1: Realization, r2: Realization) -> float:
    '''
    Computes similiarity coefficient of two realizations (should be the same length)

    range <0; 2>
    '''
    similiarity = 0.
    # The shorter length is used as all similiarity scoring is done on values that are relative to their consecutive notes
    k = len(r1.chromatic_interval)
    
    if k != len(r2.chromatic_interval): raise Exception("Realizations have different lenghts")

    for i in range(k):
        if r1.rhytmic_ratio[i] == r2.rhytmic_ratio[i]:  similiarity += 1.

        # Compare melodic characteristic and assign similiarity score based on Laskowska's model
        if (r1.diatonic_interval[i] == r2.diatonic_interval[i]) or (r1.chromatic_interval[i] == r2.chromatic_interval[i]):
            if r1.contour[i] == r2.contour[i]:          similiarity += 1.
            else:                                       similiarity += 1. / 2
        elif   r1.contour[i] == r2.contour[i]:          similiarity += 1. / 3

    # normalize to range <0; 2>
    return similiarity / k

