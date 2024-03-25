import itertools

def tsp(graph, start):
    num_cities = len(graph)
    vertices = list(range(num_cities))
    min_cost = float('inf')
    min_path = None

    for path in itertools.permutations(vertices):
        if path[0] == start:
            cost = 0
            for i in range(num_cities - 1):
                if graph[path[i]][path[i + 1]] == 0:  # Check if path is invalid
                    break
                cost += graph[path[i]][path[i + 1]]
            else:
                if graph[path[-1]][path[0]] != 0:
                    cost += graph[path[-1]][path[0]]  # Complete the cycle
                    if cost < min_cost:
                        min_cost = cost
                        min_path = path

    return min_path, min_cost

# Example Usage:
if __name__ == "__main__":
    # Example graph representation: adjacency matrix
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    start_city = 0  # Starting city
    min_path, min_cost = tsp(graph, start_city)
    if min_path:
        print("Minimum Cost Path:", min_path)
        print("Minimum Cost:", min_cost)
    else:
        print("No Hamiltonian cycle found.")
