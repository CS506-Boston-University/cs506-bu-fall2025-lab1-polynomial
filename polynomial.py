class X:
    def __init__(self):
        pass

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
        return Int(self.i)

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

    def simplify(self):
        p1_simp = self.p1.simplify()
        p2_simp = self.p2.simplify()
        
        
        if isinstance(p2_simp, Int) and p2_simp.i == 0:
            return p1_simp
        
        if isinstance(p1_simp, Int) and p1_simp.i == 0:
            return p2_simp
    
        if isinstance(p1_simp, Int) and isinstance(p2_simp, Int):
            return Int(p1_simp.i + p2_simp.i)
        
        return Add(p1_simp, p2_simp)


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

    def simplify(self):
        p1_simp = self.p1.simplify()
        p2_simp = self.p2.simplify()
        
    
        if isinstance(p2_simp, Int) and p2_simp.i == 0:
            return Int(0)
    
        if isinstance(p1_simp, Int) and p1_simp.i == 0:
            return Int(0)
    
        if isinstance(p2_simp, Int) and p2_simp.i == 1:
            return p1_simp
        
        if isinstance(p1_simp, Int) and p1_simp.i == 1:
            return p2_simp
        
        if isinstance(p1_simp, Int) and isinstance(p2_simp, Int):
            return Int(p1_simp.i * p2_simp.i)
        
        return Mul(p1_simp, p2_simp)


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p2, (Add, Sub)):
            return repr(self.p1) + " - ( " + repr(self.p2) + " )"
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self, x_value):
        return Int(self.p1.evaluate(x_value).i - self.p2.evaluate(x_value).i)

    def simplify(self):
        p1_simp = self.p1.simplify()
        p2_simp = self.p2.simplify()
        
    
        if isinstance(p2_simp, Int) and p2_simp.i == 0:
            return p1_simp
    
        if isinstance(p1_simp, Int) and isinstance(p2_simp, Int):
            return Int(p1_simp.i - p2_simp.i)
        
        return Sub(p1_simp, p2_simp)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            if isinstance(self.p2, (Add, Sub)):
                return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, (Add, Sub)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)

    def evaluate(self, x_value):
        p2_value = self.p2.evaluate(x_value).i
        if p2_value == 0:
            raise ValueError("Division by zero")
        return Int(self.p1.evaluate(x_value).i // p2_value)  

    def simplify(self):
        p1_simp = self.p1.simplify()
        p2_simp = self.p2.simplify()
        
        if isinstance(p2_simp, Int) and p2_simp.i == 1:
            return p1_simp
        if isinstance(p1_simp, Int) and isinstance(p2_simp, Int) and p2_simp.i != 0:
            return Int(p1_simp.i // p2_simp.i)
        
        return Div(p1_simp, p2_simp)
    


# Original polynomial example
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print("Original polynomial:", poly)

# Test new Sub and Div classes
print("\n--- Testing Sub and Div classes ---")
sub_poly = Sub(Int(10), Int(3))
print("Subtraction:", sub_poly)

div_poly = Div(Int(15), Int(3))
print("Division:", div_poly)

# Test evaluation
print("\n--- Testing evaluation ---")
simple_poly = Add(Sub(Mul(Int(2), X()), Int(1)), Div(Int(6), Int(2)))
print("Test polynomial:", simple_poly)
result = simple_poly.evaluate(4)
print(f"Evaluation for X=4: {result}")

original_result = poly.evaluate(2)
print(f"Original polynomial evaluation for X=2: {original_result}")

# Test simplification
print("\n--- Testing simplification ---")
expr = Add(Add(X(), Int(0)), Mul(Int(2), Int(3)))
print("Before simplification:", expr)
simplified = expr.simplify()
print("After simplification:", simplified)

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