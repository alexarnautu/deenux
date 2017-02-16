from random import shuffle


class Sequence:

    def __init__(self, n, k, random, cyclic):

        seq = [None] * n
        inv_seq = [None] * n
        perm = list(range(n))

        if random:
            shuffle(perm)

        for i in range(n - 1):
            seq[perm[i]] = perm[i + 1]
            inv_seq[perm[i + 1]] = perm[i]
        seq[perm[-1]] = perm[0] if cyclic else None
        inv_seq[perm[0]] = perm[-1] if cyclic else None

        self.seq = seq
        self.inv_seq = inv_seq
        self.__current = k

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

