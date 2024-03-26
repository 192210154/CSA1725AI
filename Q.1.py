import heapq

class PuzzleNode:
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def __init__(self, state, parent=None, move=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.state == other.state

    def __lt__(self, other):
        return (self.depth + self.manhattan_distance()) < (other.depth + other.manhattan_distance())

    def __hash__(self):
        return hash(str(self.state))

    def generate_children(self):
        children = []
        i = self.state.index(0)
        if i not in [0, 1, 2]:
            children.append(self.make_move(i, i - 3))
        if i not in [0, 3, 6]:
            children.append(self.make_move(i, i - 1))
        if i not in [2, 5, 8]:
            children.append(self.make_move(i, i + 1))
        if i not in [6, 7, 8]:
            children.append(self.make_move(i, i + 3))
        return children

    def make_move(self, i, j):
        new_state = self.state[:]
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return PuzzleNode(new_state, self, (self.state[i], self.state[j]))

    def manhattan_distance(self):
        distance = 0
        for i in range(1, 9):
            current_row, current_col = self.state.index(i) // 3, self.state.index(i) % 3
            goal_row, goal_col = self.goal_state.index(i) // 3, self.goal_state.index(i) % 3
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

def a_star_search(initial_state):
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, initial_state)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == PuzzleNode.goal_state:
            return current_node
        closed_set.add(current_node)
        
        for child_node in current_node.generate_children():
            if child_node not in closed_set:
                heapq.heappush(open_list, child_node)

# Function to print the solution path
def print_solution(solution):
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    path.reverse()
    for i in range(len(path)):
        print("Move:", path[i].move if i != 0 else "Initial State")
        print_board(path[i].state)

# Function to print the current state of the board
def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()

if __name__ == "__main__":
    initial_state = PuzzleNode([0,8,7,6,5,4,3,2,1])
    solution = a_star_search(initial_state)
    print("Solution:")
    print_solution(solution)
