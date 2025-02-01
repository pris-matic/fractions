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

    def gcd(a, b):
        
        if a == 0 or b == 0:
            return 0

        while b != 0:
            (a, b) = (b, a % b)
        return a

    def get_numerator(self):
        greatest_divisor = Fraction.gcd(self._numerator,self._denominator)
        if greatest_divisor == 0:
            return "0"
        return str(int(self._numerator / greatest_divisor))

    def get_denominator(self):
        greatest_divisor = Fraction.gcd(self._numerator,self._denominator)
        if greatest_divisor == 0:
            return "0"
        return str(int(self._denominator / greatest_divisor))

    def get_fraction(self):
        if self._denominator == 1 or self._numerator == 0:
            return self.get_numerator()
        return self.get_numerator() + "/" + self.get_denominator()