

from __future__ import division
from math import gcd
from math import sqrt


class Rational(object):
    def __init__(self, numer, denom):
        gcd = gcd(numer, denom)

        self.numer = int(numer / gcd)
        self.denom = int(denom / gcd)
        if denom == 0:
            raise Exception('Denominator of a fraction cannot be zero!')

        elif numer < 0 or denom < 0:

        else:
            self.numer = abs(int(numer / gcd(numer, denom)))
            self.denom = abs(int(denom / gcd(numer, denom)))

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = (self.numer * other.denom + self.denom * other.numer)
        denom = (self.denom * other.denom)

        self.numer = numer // gcd(numer, denom)
        self.denom = denom // gcd(numer, denom)

        return self

    def __sub__(self, other):

        numer = (self.numer * other.denom - self.denom * other.numer)
        denom = (self.denom * other.denom)
        self.numer = numer // gcd(numer, denom)
        self.denom = denom // gcd(numer, denom)

        return self

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        self.numer = numer // gcd(numer, denom)
        self.denom = denom // gcd(numer, denom)

        return self

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        self.numer = numer // gcd(numer, denom)
        self.denom = denom // gcd(numer, denom)
        return self

    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)
        return self

    def __pow__(self, power):
        if type(power) == int:

            if power >= 0:
                numer = self.numer ** power
                denom = self.denom ** power

                self.numer = numer // gcd(numer, denom)
                self.denom = denom // gcd(numer, denom)
                return self

            else:
                power = abs(power)
                numer = self.denom ** power
                denom = self.numer ** power

                self.numer = numer // gcd(numer, denom)
                self.denom = denom // gcd(numer, denom)
                return self

        elif type(power) == float:
            return (self.numer ** power) / (self.denom ** power)

        elif type(power) == Rational:
            print(power, 'is rational')

    def __rpow__(self, base):
        numer = self.denom ** abs(base)
        denom = self.numer ** abs(base)

        self.numer = numer // gcd(numer, denom)
        self.denom = denom // gcd(numer, denom)

        return self


if __name__ == '__main__':
    n1 = Rational(-1, 2)
    n2 = Rational(-1, -2)

    print(n1)
    print(n2)
