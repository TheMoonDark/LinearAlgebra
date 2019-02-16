class Vector:
    def __init__(self, lst):
        self._values = list(lst)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values[item]

    def __iter__(self):
        return  self._values.__iter__()

    def __add__(self, other):
        assert len(self) == len(other)
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        assert len(self) == len(other)
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, other):
        return Vector([other * e for e in self])

    def __rmul__(self, other):
        return Vector([other * e for e in self])

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self