from music21 import *


'''
How similiar two realizaitons must be to be included in a motive ( `range<0, 2>` )
'''
B_PARAM = 1.5

class Realization:
    diatonic_interval = []
    chromatic_interval = []
    contour = []
    rhytmic_value = []

    def __init__(self, notes: list[note.Note]):
        '''
        returns a tuple of notes sequence features

        (diatonic intervals, chromatic intervals, contour, rhytmic value)
        '''
        
        for i in range(len(notes) - 1):
            inter = interval.Interval(notes[i], notes[i+1])

            # Chromatic interval
            self.diatonic_interval.append(inter.generic.staffDistance)

            # Diatonic interval
            self.chromatic_interval.append(inter.semitones)

            # Contour
            self.contour.append(inter.diatonic.direction.value)

            # Rhytmic value
            self.rhytmic_value.append(notes[i].duration.quarterLength)

        # get the last note's rhytmic value
        self.rhytmic_value.append(notes[-1].duration.quarterLength)


def realization_similiarity(r1: Realization, r2: Realization) -> float:
    '''
    Computes similiarity coefficient of two realizations (should be the same length)
    '''
    if len(r1.diatonic_interval) != len(r2.diatonic_interval): raise Exception("Realizations have different lenghts")
