class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        
        # if numerator is a string
        if isinstance(numerator,str):
            fraction_values = numerator.split("/")
            if len(fraction_values) > 2:
                self._numerator = 0
                self._denominator = denominator
            else:
                self._numerator = fraction_values[0]
                self._denominator = fraction_values[1]

        else:
            self._numerator = numerator
            self._denominator = denominator

        # if the number provided is a float / double
        if numerator != int(numerator):
            self._numerator = 0

        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        pass

    def gcd(a, b):
        #TODO
        pass

    def get_numerator(self):
        #TODO
        pass

    def get_denominator(self):
        #TODO
        pass

    def get_fraction(self):
        #TODO
        pass