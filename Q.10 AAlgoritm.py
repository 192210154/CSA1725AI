import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

    def astar(self, start, goal):
        open_list = [(0, start)]  # Priority queue
        came_from = {}
        g_score = {node: float('inf') for node in self.edges}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.edges}
        f_score[start] = self.heuristic(start, goal)

        while open_list:
            current_cost, current_node = heapq.heappop(open_list)

            if current_node == goal:
                path = self.reconstruct_path(came_from, current_node)
                return path

            for neighbor, weight in self.edges[current_node]:
                tentative_g_score = g_score[current_node] + weight
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

        return None  # No path found

    def heuristic(self, node, goal):
        # This heuristic function can be replaced with a better one depending on the problem
        # For simplicity, this example uses Manhattan distance as a heuristic
        x1, y1 = node
        x2, y2 = goal
        return abs(x2 - x1) + abs(y2 - y1)

    def reconstruct_path(self, came_from, current_node):
        path = [current_node]
        while current_node in came_from:
            current_node = came_from[current_node]
            path.append(current_node)
        return list(reversed(path))

# Example Usage:
if __name__ == "__main__":
    graph = Graph()
    # Example graph: grid with weights
    graph.add_edge((0, 0), (0, 1), 1)
    graph.add_edge((0, 0), (1, 0), 1)
    graph.add_edge((1, 0), (1, 1), 1)
    graph.add_edge((1, 1), (0, 1), 1)
    graph.add_edge((0, 1), (0, 2), 1)
    graph.add_edge((0, 2), (1, 2), 1)
    graph.add_edge((1, 2), (2, 2), 1)
    graph.add_edge((2, 2), (2, 1), 1)
    graph.add_edge((2, 1), (2, 0), 1)

    start_node = (0, 0)
    goal_node = (2, 2)

    path = graph.astar(start_node, goal_node)
    if path:
        print("Shortest Path:", path)
    else:
        print("No path found.")
