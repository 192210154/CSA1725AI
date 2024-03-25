class MapColoring:
    def __init__(self, vertices, edges, colors):
        self.vertices = vertices
        self.edges = edges
        self.colors = colors
        self.color_map = {}

    def is_safe(self, vertex, color, color_map):
        for neighbor in self.edges[vertex]:
            if neighbor in color_map and color_map[neighbor] == color:
                return False
        return True

    def solve(self, vertex_index):
        if vertex_index == len(self.vertices):
            return True

        vertex = self.vertices[vertex_index]
        for color in self.colors:
            if self.is_safe(vertex, color, self.color_map):
                self.color_map[vertex] = color
                if self.solve(vertex_index + 1):
                    return True
                del self.color_map[vertex]
        return False

    def map_coloring(self):
        if self.solve(0):
            return self.color_map
        else:
            return None

# Example Usage:
if __name__ == "__main__":
    # Example map represented as a graph
    vertices = ['WA', 'NT', 'SA', 'QL', 'NSW', 'V', 'T']
    edges = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'QL'],
        'SA': ['WA', 'NT', 'QL', 'NSW', 'V'],
        'QL': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'QL', 'V'],
        'V': ['SA', 'NSW', 'T'],
        'T': ['V']
    }
    colors = ['Red', 'Green', 'Blue']

    map_coloring_solver = MapColoring(vertices, edges, colors)
    color_map = map_coloring_solver.map_coloring()

    if color_map:
        print("Map Coloring Solution:")
        for vertex, color in color_map.items():
            print(f"{vertex}: {color}")
    else:
        print("No solution exists for map coloring.")
