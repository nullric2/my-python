import sympy as sp

def solve_problem(problem):
    try:
        # Parse the problem string into a SymPy expression
        expr = sp.sympify(problem)

        # Solve the expression
        solution = sp.solve(expr)

        # Return the solution
        return solution
    except:
        return "Invalid problem statement. Please check your input."

# Example usage
while True:
    problem = input("Enter a math problem (or 'q' to quit): ")
    if problem.lower() == 'q':
        break

    result = solve_problem(problem)
    print("Solution:", result)
