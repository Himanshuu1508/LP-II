import heapq  # Import the heapq module for priority queue (min-heap)

N, M = 5, 5  # Define the size of the maze (5 rows and 5 columns)

# Moves: Down, Left, Up, Right (coordinate changes)
row_moves = [1, 0, -1, 0]
col_moves = [0, -1, 0, 1]

# Node class represents a position in the maze with additional information
class Node:
    def __init__(self, x, y, level, cost, parent):
        self.x, self.y = x, y  # Store the node's coordinates
        self.level = level  # Number of steps taken from the start
        self.cost = cost  # The total estimated cost (g(n) + h(n)) for A* search
        self.parent = parent  # Reference to the parent node (for backtracking the path)

    def __lt__(self, other):
        # This method is used for comparison in the priority queue. It ensures that the node with the lower cost is given higher priority.
        return self.cost < other.cost  # Min-heap priority based on 'cost'

# Check if a given position is within bounds and not a wall ('#')
def is_safe(x, y, maze):
    return 0 <= x < N and 0 <= y < M and maze[x][y] != '#'

# Calculate the heuristic (Manhattan distance) between the current node and the goal node
def heuristic(x, y, goal_x, goal_y):
    return abs(x - goal_x) + abs(y - goal_y)  # Manhattan Distance

# Find the position of a specific character (start 'S' or goal 'G') in the maze
def find_position(maze, char):
    for i in range(N):
        for j in range(M):
            if maze[i][j] == char:  # If the character matches, return the position (i, j)
                return i, j  # Return (row, column)

# Function to print the maze with visited and path nodes highlighted
def print_maze(maze, visited=None, path=None):
    for i in range(N):
        for j in range(M):
            if path and (i, j) in path:
                print('P', end=' ')  # Mark the path nodes as 'P'
            elif visited and (i, j) in visited:
                print('V', end=' ')  # Mark the visited nodes as 'V'
            else:
                print(maze[i][j], end=' ')  # Print the original maze element (S, G, #, or .)
        print()  # Print a new line after each row of the maze
    print()  # Print a final newline for readability

# Function to backtrack and print the final path from the start to the goal
def print_solution(node, maze):
    path = set()  # A set to store the path nodes
    while node:
        path.add((node.x, node.y))  # Add the current node to the path set
        node = node.parent  # Move to the parent node
    print("Final Path:")
    print_maze(maze, path=path)  # Print the maze with the path highlighted

# The main function that solves the maze using A* algorithm
def solve_maze(maze):
    # Find the start and goal positions in the maze
    start_x, start_y = find_position(maze, 'S')
    goal_x, goal_y = find_position(maze, 'G')

    priority_queue = []  # A priority queue (min-heap) to store the nodes to explore
    visited = set()  # A set to keep track of visited nodes

    # Create the root node (start node) and push it into the priority queue
    root = Node(start_x, start_y, 0, heuristic(start_x, start_y, goal_x, goal_y), None)
    heapq.heappush(priority_queue, root)  # Push the start node into the priority queue

    # Main loop that runs until we find the solution or exhaust all nodes
    while priority_queue:
        # Pop the node with the lowest cost (f(n) = g(n) + h(n))
        min_node = heapq.heappop(priority_queue)
        
        # Mark the current node as visited and print the maze with visited nodes
        visited.add((min_node.x, min_node.y))
        print(f"Step {min_node.level}: Visited ({min_node.x}, {min_node.y})")
        print_maze(maze, visited=visited)  # Print visited nodes step by step

        # If we have reached the goal, print the solution and exit
        if (min_node.x, min_node.y) == (goal_x, goal_y):
            print("Solution Found!")
            print_solution(min_node, maze)  # Print the final path
            return  # Exit the function since the solution is found

        # Explore the neighbors (4 possible directions: down, left, up, right)
        for i in range(4):
            new_x, new_y = min_node.x + row_moves[i], min_node.y + col_moves[i]
            if is_safe(new_x, new_y, maze) and (new_x, new_y) not in visited:
                # If the new position is safe and not visited, create a new child node
                child = Node(new_x, new_y, min_node.level + 1, min_node.level + 1 + heuristic(new_x, new_y, goal_x, goal_y), min_node)
                heapq.heappush(priority_queue, child)  # Add the child node to the priority queue

    # If we exhaust the queue and don't find the goal, print "No solution found."
    print("No solution found.")

# Maze Configuration: A 5x5 grid with 'S' for start, 'G' for goal, '#' for walls, and '.' for empty spaces
maze = [
    ['S', '.', '.', '#', 'G'],
    ['#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['#', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '.']
]

# Print initial instructions and the maze
print("V- Visited, P- Path, S- Start, G- Goal")
print("#- Wall, .- Empty \n")
print("Initial Maze:")
print_maze(maze)

# Call the solve_maze function to start the A* algorithm and find the solution
solve_maze(maze)

#informed search algo, eg Greedy Best First Search (f(n) = h(n)) and astar.
#Pathfinding and Navigation, Route Planning, AI for Search Problems:, Puzzle Solvers:, AI Path Planning in Autonomous Vehicles.
# g(n): The cost from the start node to the current node.

# h(n): The heuristic estimated cost from node n to the goal.

# f(n): The total estimated cost from the start to the goal through node n.

# This algorithm is used in AI for problems like pathfinding in a maze or game, where both cost and heuristic are important factors.
#Manhattan Distance: Used for grid-based problems where diagonal movement is not allowed.

#Euclidean Distance: Used when diagonal movement is allowed, as it calculates the straight-line distance between two points.

#Octile Distance: A variant of the Manhattan or Euclidean distance for grids that allows diagonal movement.
