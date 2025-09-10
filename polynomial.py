class X:
    def __repr__(self):
        return "X"

    def evaluate(self, x_value):
        return Int(x_value)

    def simplify(self):
        return self


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x_value):
        return self

    def simplify(self):
        return self


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x_value):
        return Int(self.p1.evaluate(x_value).i + self.p2.evaluate(x_value).i)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self, x_value):
        return Int(self.p1.evaluate(x_value).i * self.p2.evaluate(x_value).i)


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        left = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub)) else repr(self.p1)
        right = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub)) else repr(self.p2)
        return f"{left} - {right}"

    def evaluate(self, x_value):
        return Int(self.p1.evaluate(x_value).i - self.p2.evaluate(x_value).i)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        left = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub)) else repr(self.p1)
        right = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub)) else repr(self.p2)
        return f"{left} / {right}"

    def evaluate(self, x_value):
        denominator = self.p2.evaluate(x_value).i
        if denominator == 0:
            raise ZeroDivisionError("Division by zero in polynomial")
        return Int(self.p1.evaluate(x_value).i // denominator)

