class TimeStamp:
    def __init__(self, h=0, m=0, s=0):
        self._h = h
        self._m = m
        self._s = s

    # read-only properties
    @property
    def h(self):
        """Read-only hour value"""
        return self._h

    @property
    def m(self):
        """Read-only minute value"""
        return self._m

    @property
    def s(self):
        """Read-only second value"""
        return self._s

    # rich comparison methods
    def __lt__(self, other):
        if hasattr(other, '_h') and hasattr(other, '_m') and hasattr(other, '_s'):
            if self._h < other.h:
                return True

            if self._m < other.m:
                return True

            if self._s < other.s:
                return True

        return False

    def __le__(self, other):
        if hasattr(other, '_h') and hasattr(other, '_m') and hasattr(other, '_s'):
            if self._h <= other.h:
                if self._m <= other.m:
                    if self._s <= other.s:
                        return True
        return False

    def __eq__(self, other):
        if hasattr(other, '_h') and hasattr(other, '_m') and hasattr(other, '_s'):
            return self._h == other.h and self._m == other.m and self._s == other.s
        return False

    def __ne__(self, other):
        if hasattr(other, '_h') and hasattr(other, '_m') and hasattr(other, '_s'):
            if self._h != other.h:
                if self._m != other.m:
                    if self._s != other.s:
                        return True
            return False
        return True

    def __gt__(self, other):
        if hasattr(other, '_h') and hasattr(other, '_m') and hasattr(other, '_s'):
            if self._h > other.h:
                return True
            if self._m > other.m:
                return True
            if self._s > other.s:
                return True
        return False

    def __ge__(self, other):
        if hasattr(other, '_h') and hasattr(other, '_m') and hasattr(other, '_s'):
            if self._h >= other.h:
                if self._m >= other.m:
                    if self._s >= other.s:
                        return True
        return False

    # operations, add, sub, mul
    @staticmethod
    def _convert(s):
        m = 0
        h = 0
        if s > 59:
            m += s // 60
            s %= 60
        if m > 59:
            h += m // 60
            m %= 60

        return TimeStamp(h, m, s)

    def __add__(self, other):
        s = (self._h * 3600 + self._m * 60 + self._s) + (other.h * 3600 + other.m * 60 + other.s)
        return self._convert(s)

    def __sub__(self, other):
        s = (self._h * 3600 + self._m * 60 + self._s) - (other.h * 3600 + other.m * 60 + other.s)
        return self._convert(s)

    def __mul__(self, factor):
        if not isinstance(factor, int):
            raise NotImplementedError('Solo puede multiplicarse por un factor')
        s = (self._h * 3600 + self._m * 60 + self._s) * factor
        return self._convert(s)

    def __repr__(self):
        return ':'.join([str(self._h), str(self._m).rjust(2, '0')])