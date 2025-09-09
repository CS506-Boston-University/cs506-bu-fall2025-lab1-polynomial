class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x_value):
            # Should return an Int object with the given x_value
            return Int(x_value)

    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # X cannot be simplified further, so return self
        pass


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x_value):
            # Should return an Int object with the stored integer value
            return self
    
    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # Integer constants cannot be simplified further, so return self
        pass


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x_value):
            # Should evaluate both operands and return their sum
            val1 = self.p1.evaluate(x_value).i
            val2 = self.p2.evaluate(x_value).i
            return Int(val1 + val2)
    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # Examples: X + 0 -> X, 0 + X -> X, 3 + 5 -> 8
        # Hint: Simplify operands first, then apply simplification rules
        pass


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
# In class Mul
    def evaluate(self, x_value):
        val1 = self.p1.evaluate(x_value).i
        val2 = self.p2.evaluate(x_value).i
        return Int(val1 * val2)

    def simplify(self):
        # TODO (Optional Exercise): Implement simplification
        # Examples: X * 0 -> 0, X * 1 -> X, 3 * 5 -> 15
        # Hint: Simplify operands first, then apply simplification rules
        pass


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # Handles parentheses similar to the Mul class to ensure clarity.
        p1_repr = repr(self.p1)
        p2_repr = repr(self.p2)
        
        # Add parentheses around addition expressions to maintain order.
        if isinstance(self.p1, Add):
            p1_repr = f"( {p1_repr} )"
        if isinstance(self.p2, Add):
            p2_repr = f"( {p2_repr} )"
            
        return f"{p1_repr} - {p2_repr}"


# In class Sub
    def evaluate(self, x_value):
        val1 = self.p1.evaluate(x_value).i
        val2 = self.p2.evaluate(x_value).i
        return Int(val1 - val2)


    def simplify(self):
        # Optional exercise for simplification.
        pass


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # Handles parentheses similar to the Mul class.
        p1_repr = repr(self.p1)
        p2_repr = repr(self.p2)
        
        # Add parentheses around addition or subtraction expressions.
        if isinstance(self.p1, (Add, Sub)):
            p1_repr = f"( {p1_repr} )"
        if isinstance(self.p2, (Add, Sub)):
            p2_repr = f"( {p2_repr} )"

        return f"{p1_repr} / {p2_repr}"

# In class Div
    def evaluate(self, x_value):
        val1 = self.p1.evaluate(x_value).i
        val2 = self.p2.evaluate(x_value).i
        if val2 == 0:
            raise ValueError("Division by zero")
        return Int(val1 // val2)
    def simplify(self):
        # Optional exercise for simplification.
        pass


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
# hi
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
