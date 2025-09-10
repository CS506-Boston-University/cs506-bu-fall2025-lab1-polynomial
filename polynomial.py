class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x_value):
        # Return Int object with the given x_value
        return Int(x_value)

    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # X cannot be simplified further, so return self
        return self


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x_value):
        # Return Int object with the stored integer value
        return Int(self.i)

    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # Integer constants cannot be simplified further, so return self
        return self


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x_value):
        # Evaluate both operands and return their sum
        left = self.p1.evaluate(x_value)
        right = self.p2.evaluate(x_value)
        return Int(left.i + right.i)


    def simplify(self):
        left = self.p1.simplify()
        right = self.p2.simplify()
        # 0 + X -> X
        if isinstance(left, Int) and left.i == 0:
            return right
        # X + 0 -> X
        if isinstance(right, Int) and right.i == 0:
            return left
        # Both Int: 3 + 5 -> 8
        if isinstance(left, Int) and isinstance(right, Int):
            return Int(left.i + right.i)
        return Add(left, right)



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
        # Evaluate both operands and return their product
        left = self.p1.evaluate(x_value)
        right = self.p2.evaluate(x_value)
        return Int(left.i * right.i)


    def simplify(self):
        left = self.p1.simplify()
        right = self.p2.simplify()
        # 0 * X or X * 0 -> 0
        if (isinstance(left, Int) and left.i == 0) or (isinstance(right, Int) and right.i == 0):
            return Int(0)
        # 1 * X -> X
        if isinstance(left, Int) and left.i == 1:
            return right
        # X * 1 -> X
        if isinstance(right, Int) and right.i == 1:
            return left
        # Both Int: 3 * 5 -> 15
        if isinstance(left, Int) and isinstance(right, Int):
            return Int(left.i * right.i)
        return Mul(left, right)



class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # Parentheses for Add or Sub in operands
        left = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub)) else repr(self.p1)
        right = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub)) else repr(self.p2)
        return f"{left} - {right}"

    def evaluate(self, x_value):
        # Evaluate both operands and subtract
        left = self.p1.evaluate(x_value)
        right = self.p2.evaluate(x_value)
        return Int(left.i - right.i)

    def simplify(self):
        left = self.p1.simplify()
        right = self.p2.simplify()
        # X - 0 -> X
        if isinstance(right, Int) and right.i == 0:
            return left
        # Both Int: 5 - 3 -> 2
        if isinstance(left, Int) and isinstance(right, Int):
            return Int(left.i - right.i)
        return Sub(left, right)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # Parentheses for Add, Sub, or Mul in operands
        left = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub, Mul)) else repr(self.p1)
        right = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub, Mul)) else repr(self.p2)
        return f"{left} / {right}"

    def evaluate(self, x_value):
        # Evaluate both operands and integer-divide
        left = self.p1.evaluate(x_value)
        right = self.p2.evaluate(x_value)
        return Int(left.i // right.i)

    def simplify(self):
        # Simplify operands first
        left = self.p1.simplify()
        right = self.p2.simplify()
        # X / 1 -> X
        if isinstance(right, Int) and right.i == 1:
            return left
        # Both Int: 6 / 2 -> 3test
        if isinstance(left, Int) and isinstance(right, Int):
            return Int(left.i // right.i)
        return Div(left, right)
    
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
