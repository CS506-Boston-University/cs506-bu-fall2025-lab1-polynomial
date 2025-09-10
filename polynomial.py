class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x_value):
        # TODO: Implement evaluation for variable X
        # Should return an Int object with the given x_value
        return Int(x_value)
        pass

    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # X cannot be simplified further, so return self
        return self
        pass


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x_value):
        # TODO: Implement evaluation for integer constant
        # Should return an Int object with the stored integer value
        return self
        pass

    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # Integer constants cannot be simplified further, so return self
        return self
        pass


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x_value):
        # TODO: Implement evaluation for addition
        # Should evaluate both operands and return their sum
        v1 = self.p1.evaluate(x_value)
        v2 = self.p2.evaluate(x_value)
        return Int(v1.i + v2.i)

        #Added subtraction and division
        #pass

    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # Examples: X + 0 -> X, 0 + X -> X, 3 + 5 -> 8
        # Hint: Simplify operands first, then apply simplification rules
        p1s = self.p1.simplify()
        p2s = self.p2.simplify()

        # Apply simplification rules
        if isinstance(p1s, Int) and p1s.i == 0:
            return p2s
        if isinstance(p2s, Int) and p2s.i == 0:
            return p1s
        if isinstance(p1s, Int) and isinstance(p2s, Int):
            return Int(p1s.i + p2s.i)
        return Add(p1s, p2s)
        #pass


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
        # TODO: Implement evaluation for multiplication
        # Should evaluate both operands and return their product
        v1 = self.p1.evaluate(x_value)
        v2 = self.p2.evaluate(x_value)
        return Int(v1.i * v2.i)
        pass

    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # Examples: X * 0 -> 0, X * 1 -> X, 3 * 5 -> 15
        # Hint: Simplify operands first, then apply simplification rules
        p1s = self.p1.simplify()
        p2s = self.p2.simplify()

        # Apply simplification rules
        if (isinstance(p1s, Int) and p1s.i == 0) or (isinstance(p2s, Int) and p2s.i == 0):
            return Int(0)
        if isinstance(p1s, Int) and p1s.i == 1:
            return p2s
        if isinstance(p2s, Int) and p2s.i == 1:
            return p1s
        if isinstance(p1s, Int) and isinstance(p2s, Int):
            return Int(p1s.i * p2s.i)
        return Mul(p1s, p2s)
        #pass


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # TODO: Implement string representation for subtraction
        # Should handle parentheses similar to Mul class
        # Hint: Look at how Mul class handles parentheses
        left = repr(self.p1)
        right = repr(self.p2)

        # Parentheses if operands are Add or Sub (lower precedence than Sub itself)
        if isinstance(self.p1, (Add, Sub)):
            left = f"( {left} )"
        if isinstance(self.p2, (Add, Sub)):
            right = f"( {right} )"

        return f"{left} - {right}"

    def evaluate(self, x_value):
        # TODO: Implement evaluation for subtraction
        # Should return the difference of the two operands
        v1 = self.p1.evaluate(x_value)
        v2 = self.p2.evaluate(x_value)
        return Int(v1.i - v2.i)
        pass

    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # Examples: X - 0 -> X, 5 - 3 -> 2
        # Hint: Simplify operands first, then apply simplification rules
        p1s = self.p1.simplify()
        p2s = self.p2.simplify()

        # Apply simplification rules
        if isinstance(p2s, Int) and p2s.i == 0:
            return p1s
        if isinstance(p1s, Int) and isinstance(p2s, Int):
            return Int(p1s.i - p2s.i)
        return Sub(p1s, p2s)
        #pass


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # TODO: Implement string representation for division
        # Should handle parentheses similar to Mul class
        # Hint: Look at how Mul class handles parentheses
        left = repr(self.p1)
        right = repr(self.p2)

        # Always parenthesize if numerator/denominator is Add or Sub
        if isinstance(self.p1, (Add, Sub)):
            left = f"( {left} )"
        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            right = f"( {right} )"

        return f"{left} / {right}"
        pass

    def evaluate(self, x_value):
        # TODO: Implement evaluation for division
        # Should return the quotient of the two operands (use integer division //)
        v1 = self.p1.evaluate(x_value)
        v2 = self.p2.evaluate(x_value)
        return Int(v1.i // v2.i)
        #pass

    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # Examples: X / 1 -> X, 6 / 2 -> 3
        # Hint: Simplify operands first, then apply simplification rules
        p1s = self.p1.simplify()
        p2s = self.p2.simplify()

        # Apply simplification rules
        if isinstance(p2s, Int):
            if p2s.i == 1:
                return p1s
            if isinstance(p1s, Int):
                return Int(p1s.i // p2s.i)
        return Div(p1s, p2s)
        #pass


# Original polynomial example
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print("Original polynomial:", poly)

# Test new Sub and Div classes (will fail until implemented)
print("\n--- Testing Sub and Div classes ---")
try:
    sub_poly = Sub(Int(10), Int(3))
    print("Subtraction:", sub_poly)
except Exception as e:
    print("❌ Subtraction test failed - Sub class not implemented yet")

try:
    div_poly = Div(Int(15), Int(3))
    print("Division:", div_poly)
except Exception as e:
    print("❌ Division test failed - Div class not implemented yet")

# Test evaluation (will fail until implemented)
print("\n--- Testing evaluation ---")
try:
    simple_poly = Add(Sub(Mul(Int(2), X()), Int(1)), Div(Int(6), Int(2)))
    print("Test polynomial:", simple_poly)
    result = simple_poly.evaluate(4)
    print(f"Evaluation for X=4: {result}")
except Exception as e:
    print("❌ Evaluation test failed - evaluate methods not implemented yet")

try:
    original_result = poly.evaluate(2)
    print(f"Original polynomial evaluation for X=2: {original_result}")
except Exception as e:
    print(
        "❌ Original polynomial evaluation failed - evaluate methods not implemented yet"
    )

# Option to run comprehensive tests
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("\n" + "=" * 60)
        print("Running comprehensive test suite...")
        print("=" * 60)
        from test_polynomial import run_all_tests

        run_all_tests()
    else:
        print("\n💡 To run comprehensive tests, use: python polynomial.py --test")
        print("💡 Or run directly: python test_polynomial.py")
