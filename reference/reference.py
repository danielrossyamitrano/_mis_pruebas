from math import sqrt


class Reference:
    def __init__(self, value):
        self._value = value


class Top(Reference):
    def __init__(self, y=0):
        super().__init__(y)

    @property
    def y(self):
        return self._value

    @y.setter
    def y(self, value):
        self._value = value

    @y.deleter
    def y(self):
        self._value = 0


class Bottom(Reference):
    def __init__(self, y=0):
        super().__init__(y)

    @property
    def y(self):
        return self._value

    @y.setter
    def y(self, value):
        self._value = value

    @y.deleter
    def y(self):
        self._value = 0


class Left(Reference):
    def __init__(self, x=0):
        super().__init__(x)

    @property
    def x(self):
        return self._value

    @x.setter
    def x(self, value):
        pass

    @x.deleter
    def x(self):
        self._value = 0


class Right(Reference):
    def __init__(self, x=0):
        super().__init__(x)

    @property
    def x(self):
        return self._value

    @x.setter
    def x(self, value):
        pass

    @x.deleter
    def x(self):
        self._value = 0


class Radial(Reference):
    def __init__(self, origin_x, origin_y):
        super().__init__()
        self.a = origin_x
        self.b = origin_y
        self.center = self.a,self.b

    def r(self, x, y):
        a, b = self.a, self.b
        r = sqrt((x-a)**2+(y-b)**2)
        return r
