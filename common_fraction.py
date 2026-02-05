from enum import Enum


class Sign(Enum):
    PLUS = 0
    MINUS = 1


class CommonFraction:
    def _change_sign(self):
        if self._sign == Sign.PLUS:
            self._sign = Sign.MINUS
        else:
            self._sign = Sign.PLUS

    def _normalize_sign(self):
        sign_counter = 0

        if self._top < 0:
            sign_counter += 1
        if self._bottom < 0:
            sign_counter += 1

        if sign_counter % 2:
            self._change_sign()
            sign_counter = 0

        self._top = abs(self._top)
        self._bottom = abs(self._bottom)

    def __init__(self, _top=1, _bottom=1, sign=Sign.PLUS):
        # числитель и знаменатель
        self._top = _top
        self._bottom = _bottom

        # знак числа
        self._sign = sign
        self._normalize_sign()

    @staticmethod
    def gcd(in_a, in_b):
        a = abs(in_a)
        b = abs(in_b)

        while b:
            temp = b
            b = a % b
            a = temp

        return a

    def reduce(self):
        cmn_divider = self.gcd(self._top, self._bottom)
        self._top /= cmn_divider
        self._bottom /= cmn_divider

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        if value < 0:
            self._change_sign()
        self._top = value

    @property
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self, value):
        if value < 0:
            self._change_sign()
        self._bottom = value

    @property
    def sign(self):
        return self._sign

    @sign.setter
    def sign(self, value):
        if value == Sign.MINUS:
            self._change_sign()
