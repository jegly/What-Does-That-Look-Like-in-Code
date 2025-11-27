"""
codegen/mathematics.py - Mathematics code generation
"""


class MathematicsGenerator:
    """Generates code for mathematical scenarios"""
    
    @staticmethod
    def generate_pseudo(ir) -> str:
        """Generate pseudo-code for math scenario"""
        pseudo = []
        pseudo.append("// MATHEMATICAL MODEL")
        pseudo.append("// Symbolic and numeric computation")
        pseudo.append("")
        pseudo.append("Define Variables:")
        pseudo.append("  x, y, z = symbols")
        pseudo.append("")
        pseudo.append("Define Function:")
        pseudo.append("  f(x) = expression_in_x")
        pseudo.append("")
        pseudo.append("Operations:")
        pseudo.append("  derivative = df/dx")
        pseudo.append("  integral = ∫f(x)dx")
        pseudo.append("  solve = find x where f(x) = 0")
        pseudo.append("")
        pseudo.append("Optimization (if applicable):")
        pseudo.append("  critical_points = solve(derivative = 0)")
        pseudo.append("  classify: minimum, maximum, or saddle point")
        
        return "\n".join(pseudo)
    
    @staticmethod
    def generate_python(ir) -> str:
        """Generate executable Python code for math scenario"""
        code = []
        code.append('"""')
        code.append(f'Mathematical Computation: {ir.raw_text}')
        code.append('"""')
        code.append('import sympy as sp')
        code.append('import numpy as np')
        code.append('')
        code.append('')
        code.append('class MathematicalSystem:')
        code.append('    """Symbolic and numeric mathematics"""')
        code.append('    ')
        code.append('    def __init__(self):')
        code.append('        self.x = sp.Symbol(\'x\')')
        code.append('        self.y = sp.Symbol(\'y\')')
        code.append('        self.z = sp.Symbol(\'z\')')
        code.append('    ')
        code.append('    def analyze_function(self, expr):')
        code.append('        """Analyze a mathematical function"""')
        code.append('        print(f"Function: f(x) = {expr}")')
        code.append('        ')
        code.append('        # Derivative')
        code.append('        derivative = sp.diff(expr, self.x)')
        code.append('        print(f"Derivative: f\'(x) = {derivative}")')
        code.append('        ')
        code.append('        # Integral')
        code.append('        integral = sp.integrate(expr, self.x)')
        code.append('        print(f"Integral: ∫f(x)dx = {integral}")')
        code.append('        ')
        code.append('        # Critical points')
        code.append('        critical_points = sp.solve(derivative, self.x)')
        code.append('        print(f"Critical points: {critical_points}")')
        code.append('        ')
        code.append('        return derivative, integral, critical_points')
        code.append('    ')
        code.append('    def optimize(self, expr, bounds=(-10, 10)):')
        code.append('        """Find minimum and maximum of function"""')
        code.append('        derivative = sp.diff(expr, self.x)')
        code.append('        critical_points = sp.solve(derivative, self.x)')
        code.append('        ')
        code.append('        # Filter real critical points in bounds')
        code.append('        real_points = [')
        code.append('            float(pt) for pt in critical_points')
        code.append('            if pt.is_real and bounds[0] <= float(pt) <= bounds[1]')
        code.append('        ]')
        code.append('        ')
        code.append('        if real_points:')
        code.append('            # Evaluate function at critical points')
        code.append('            f_lambda = sp.lambdify(self.x, expr, "numpy")')
        code.append('            values = [(pt, f_lambda(pt)) for pt in real_points]')
        code.append('            ')
        code.append('            min_point = min(values, key=lambda v: v[1])')
        code.append('            max_point = max(values, key=lambda v: v[1])')
        code.append('            ')
        code.append('            print(f"\\nOptimization in [{bounds[0]}, {bounds[1]}]:")')
        code.append('            print(f"Minimum: f({min_point[0]:.3f}) = {min_point[1]:.3f}")')
        code.append('            print(f"Maximum: f({max_point[0]:.3f}) = {max_point[1]:.3f}")')
        code.append('        ')
        code.append('        return real_points')
        code.append('    ')
        code.append('    def probability_demo(self):')
        code.append('        """Demonstrate probability calculations"""')
        code.append('        print("\\nProbability Example: Coin flips")')
        code.append('        n, k, p = 10, 6, 0.5')
        code.append('        ')
        code.append('        # Binomial probability: P(X = k) for n trials')
        code.append('        from scipy.special import comb')
        code.append('        prob = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))')
        code.append('        ')
        code.append('        print(f"P(exactly {k} heads in {n} flips) = {prob:.4f}")')
        code.append('')
        code.append('')
        code.append('# Run demonstrations')
        code.append('if __name__ == "__main__":')
        code.append('    math_sys = MathematicalSystem()')
        code.append('    ')
        code.append('    # Example 1: Polynomial function')
        code.append('    print("="*50)')
        code.append('    print("EXAMPLE 1: Polynomial Analysis")')
        code.append('    print("="*50)')
        code.append('    expr1 = math_sys.x**3 - 3*math_sys.x**2 + 2')
        code.append('    math_sys.analyze_function(expr1)')
        code.append('    math_sys.optimize(expr1, bounds=(-2, 4))')
        code.append('    ')
        code.append('    # Example 2: Trigonometric function')
        code.append('    print("\\n" + "="*50)')
        code.append('    print("EXAMPLE 2: Trigonometric Analysis")')
        code.append('    print("="*50)')
        code.append('    expr2 = sp.sin(math_sys.x) * math_sys.x')
        code.append('    math_sys.analyze_function(expr2)')
        code.append('    ')
        code.append('    # Example 3: Probability')
        code.append('    print("\\n" + "="*50)')
        code.append('    print("EXAMPLE 3: Probability")')
        code.append('    print("="*50)')
        code.append('    math_sys.probability_demo()')
        
        return "\n".join(code)


if __name__ == "__main__":
    from ir import IntermediateRepresentation
    
    ir = IntermediateRepresentation(
        raw_text="Find the derivative and minimum of a quadratic function.",
        category="mathematics"
    )
    
    gen = MathematicsGenerator()
    print(gen.generate_python(ir))
