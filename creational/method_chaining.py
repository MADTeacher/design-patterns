class MegaCalculation():

    def __init__(self, value):
        self.value = value

    def add(self, a):
        self.value += a
        return self

    def mul(self, a):
        self.value *= a
        return self

    def pow(self, a):
        self.value = self.value ** a
        return self

    def sub(self, a):
        self.value -= a
        return self

    def div(self, a):
        self.value = self.value // a
        return self


if __name__ == "__main__":
    my_calc = MegaCalculation(100)
    print(my_calc.add(100).div(20).mul(3).value)
