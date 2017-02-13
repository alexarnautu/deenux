from random import shuffle


class Sequence:

    def __init__(self, n, k, random, cyclic):

        self.__n = n
        self.__random = random
        self.__current = k
        self.__cyclic = cyclic
        self.shuffle()

    def shuffle(self):
        
        n = self.__n
        seq = [None] * n
        inv_seq = [None] * n
        perm = list(range(n))

        if self.__random:
            shuffle(perm)

        for i in range(n - 1):
            seq[perm[i]] = perm[i + 1]
            inv_seq[perm[i + 1]] = perm[i]
        seq[perm[-1]] = perm[0] if self.__cyclic else None
        inv_seq[perm[0]] = perm[-1] if self.__cyclic else None

        self.seq = seq
        self.inv_seq = inv_seq

    @property
    def current(self):
        return self.__current
    @current.setter
    def current(self, val):
        self.__current = val

    @property
    def next(self):
        try:
            self.__current = self.seq[self.__current]
            return self.__current
        except TypeError:
            return None
    @property
    def prev(self):
        try:
            self.__current = self.inv_seq[self.__current]
            return self.__current
        except TypeError:
            return None

