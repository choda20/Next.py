import operator
import winsound
from collections.abc import Iterable
import itertools


def ex512():  # 5.1.2
    freqs = {"la": 220, "si": 247, "do": 261, "re": 293, "mi": 329, "fa": 349, "sol": 392}
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    note_and_len = notes.split("-")
    print("list is iterable: " + str(isinstance(note_and_len, Iterable)))
    for note in note_and_len:
        note = note.split(",")
        winsound.Beep(freqs[note[0]], int(note[1]))


def ex522():  # 5.2.2
    numbers = iter(list(range(1, 101)))
    while True:
        try:
            next(numbers)
            next(numbers)
            print(next(numbers))
        except StopIteration:
            break


def ex523():  # 5.2.3
    cash_list = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    combi_list = []

    for r in range(1, len(cash_list) + 1):  # the size of the combination
        for combination in itertools.combinations(cash_list, r): # generates all combinations for size r and
            # iterates through them
            if sum(combination) == 100: # sums the combinations
                combi_list.append(list(combination))
    combi_set = {tuple(combi) for combi in combi_list}

    print("There are " + str(len(combi_set)) + " possible combinations: ")
    for combi in combi_set:
        print("\t" + str(combi))


class MusicNote:  # 5.3.2
    def __init__(self, freqs):
        self._freqs = freqs
        self._iter_index = 0

    @property
    def freqs(self):
        return self._freqs

    @property
    def iter_index(self):
        return self._iter_index

    def __next__(self):
        if self.iter_index < len(self.freqs):
            return_value = self.freqs[self.iter_index]
            self._iter_index += 1
            return return_value
        else:
            raise StopIteration

    def __iter__(self):
        return self


class MusicNotes:  # 5.2.3
    def __init__(self,note_freqs):
        self._note_freqs = note_freqs
        self._iter_index = 0

    @property
    def iter_index(self):
        return self._iter_index

    @property
    def note_freqs(self):
        return self._note_freqs

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.iter_index >= len(self.note_freqs):
                self._iter_index = 0
            return_value = next(self.note_freqs[self.iter_index])
            self._iter_index += 1
            return return_value
        except StopIteration:
            raise StopIteration


def ex532():  # 5.2.3
    la = MusicNote([55, 110, 220, 440, 880])
    si = MusicNote([61.74, 123.48, 246.96, 493.92, 987.84])
    do = MusicNote([65.41, 130.82, 261.64, 523.28, 1046.56])
    re = MusicNote([73.42, 146.84, 293.68, 587.36, 1174.72])
    mi = MusicNote([82.41, 164.82, 329.64, 659.28, 1318.56])
    fa = MusicNote([87.31, 174.62, 349.24, 698.48, 1396.96])
    sol = MusicNote([98, 196, 392, 784, 1568])
    note_table = MusicNotes([la, si, do, re, mi, fa, sol])
    for note in note_table:
        print(note)


if __name__ == "__main__":
    ex512()  # 5.1.2
    print("-"*15)
    ex522()  # 5.2.2
    print("-" * 15)
    ex523()  # 5.2.3
    print("-" * 15)
    ex532()  # 5.3.2

