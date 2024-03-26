from itertools import permutations

def solve_cryptarithmetic(puzzle):
    letters = {ch for ch in puzzle if ch.isalpha()}
    if len(letters) > 10:
        return "Invalid puzzle: More than 10 unique letters"

    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if all(mapping[ch] != 0 for ch in puzzle if ch.isalpha()):
            expression = puzzle.translate(str.maketrans(mapping))
            if eval(expression):
                return mapping
    return "No solution found"

# Example usage:
puzzle = "SEND + MORE == MONEY"
solution = solve_cryptarithmetic(puzzle)
if isinstance(solution, dict):
    print("Solution found:")
    for key, value in solution.items():
        print(f"{key} = {value}")
else:
    print(solution)
