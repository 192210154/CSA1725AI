from collections import deque

def water_jug_problem(x, y, z):
    if z > max(x, y):
        return "Target volume can't be greater than the capacity of both jugs"
    
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        jug1, jug2 = queue.popleft()
        if jug1 == z or jug2 == z or jug1 + jug2 == z:
            return f"Solution found: ({jug1}, {jug2})"
        
        # Fill jug1
        if (x, jug2) not in visited:
            queue.append((x, jug2))
            visited.add((x, jug2))
        
        # Fill jug2
        if (jug1, y) not in visited:
            queue.append((jug1, y))
            visited.add((jug1, y))
        
        # Empty jug1
        if (0, jug2) not in visited:
            queue.append((0, jug2))
            visited.add((0, jug2))
        
        # Empty jug2
        if (jug1, 0) not in visited:
            queue.append((jug1, 0))
            visited.add((jug1, 0))
        
        # Pour water from jug1 to jug2
        pour_amount = min(jug1, y - jug2)
        if (jug1 - pour_amount, jug2 + pour_amount) not in visited:
            queue.append((jug1 - pour_amount, jug2 + pour_amount))
            visited.add((jug1 - pour_amount, jug2 + pour_amount))
        
        # Pour water from jug2 to jug1
        pour_amount = min(jug2, x - jug1)
        if (jug1 + pour_amount, jug2 - pour_amount) not in visited:
            queue.append((jug1 + pour_amount, jug2 - pour_amount))
            visited.add((jug1 + pour_amount, jug2 - pour_amount))
    
    return "No solution found"

# Example usage:
x_capacity = 4  # capacity of the first jug
y_capacity = 3  # capacity of the second jug
target_volume = 2  # target volume to be measured
print(water_jug_problem(x_capacity, y_capacity, target_volume))
