from .timestamp import TimeStamp
from datetime import datetime


class Clock:
    _h = 0
    _m = 0
    _s = 0
    real = False
    day_flag = False
    hour_flag = False
    minute_flag = False
    second_flag = False
    enabled = False

    def __init__(self, real=False, h=0, m=0, s=0, minute_lenght=60):
        """Nuevo Reloj Clock con capacidades superiores. Puede ser real o ficticio.
        Ahora con nuevas flags para minutos y segundos, además de horas y días.

        real determina si se usa un reloj real (que usa la hora del sistema)
        o uno ficticio. En caso de usar un reloj ficticio, es posible determinar
        la hora, minutos y segundos estableciendo valores para h, m y s.
        minute_lenght determina cuantos ticks (por defecto, 60 ticks = 1 segundo)
        dura un minuto de un reloj ficticio. Este valor es ignorado si el reloj
        es real.

        :param real: bool
        :param h: int
        :param m: int
        :param s: int
        :param minute_lenght: int
        """

        self.real = real

        if self.real:
            now = datetime.now().time()
            h = now.hour
            m = now.minute
            s = now.second
        else:
            self.ds = minute_lenght

        self._h = h
        self._m = m
        self._s = s

        # EventDispatcher.register(self.on_pause, 'Pause')

    def on_pause(self, event):
        self.enabled = not event.data['value']

    def __repr__(self):
        return ':'.join([str(self._h), str(self._m).rjust(2, '0')])

    def is_real(self):
        return self.real

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        if self.real:
            if value != self._h:
                self.hour_flag = True
            if value == 0:
                self.day_flag = True
        else:
            self.hour_flag = True
            if value > 23:
                self.day_flag = True
                value = 0

            self._h = value

    @h.deleter
    def h(self):
        self._h = 0

    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, value):
        if self.real:
            if value != self._m:
                self.minute_flag = True
        else:
            self.minute_flag = True
            if value > 59:
                self.h += 1
                value = 0

        self._m = value

    @m.deleter
    def m(self):
        self._m = 0

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        if self.real:
            if value != self._m:
                self.second_flag = True
        else:
            self.second_flag = True
            if value > 59:
                self.m += 1
                value = 0

        self._s = value

    @s.deleter
    def s(self):
        self._s = 0

    def timestamp(self, h=0, m=0, s=0):
        """Without arguments, returns current tiemstamp
        with arguments, returns the specified TimeStamp
        :param s: int
        :param m: int
        :param h: int
        """

        if h == 0 and m == 0 and s == 0:
            return TimeStamp(self._h, self._m, self._s)
        else:
            return TimeStamp(h, m, s)

    def update(self):
        if self.enabled:
            self.day_flag = False
            self.hour_flag = False
            self.minute_flag = False
            self.second_flag = False

            if self.real:
                _time = datetime.now().time()
                self.h = _time.hour
                self.m = _time.minute
                self.s = _time.second
            else:
                self.s += self.ds
