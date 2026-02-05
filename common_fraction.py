from enum import Enum

class Sign(Enum):
    PLUS = 0
    MINUS = 1

class CommonFraction:
    def __init__(self, top = 1, bottom = 1, sign = Sign.PLUS):
        # знак числа
        

        self.top = abs(top)
        self.bottom = abs(bottom)


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
        cmn_divider = self.gcd(self.top, self.bottom)
        self.top /= cmn_divider
        self.bottom /= cmn_divider
        