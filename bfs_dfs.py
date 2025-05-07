# Function to build an undirected graph using adjacency list
def build_graph():
    graph = {}  # Initialize an empty dictionary to store the graph
    n = int(input("Enter number of vertices: "))  # Number of vertices (for reference)
    e = int(input("Enter number of edges: "))     # Number of edges to read
    print("Enter edges (u v) one per line:")
    for _ in range(e):
        u, v = input().split()  # Read edge between vertex u and vertex v
        if u not in graph:
            graph[u] = []  # Initialize adjacency list for vertex u if not present
        if v not in graph:
            graph[v] = []  # Initialize adjacency list for vertex v if not present
        graph[u].append(v)  # Add v to u's list
        graph[v].append(u)  # Add u to v's list (because the graph is undirected)
    return graph  # Return the constructed graph

# Depth-First Search (Recursive Version)
def dfs_recursive(graph, node, visited):
    if node not in visited:  # Process only unvisited nodes
        print(node, end=" ")  # Print the node
        visited.add(node)     # Mark node as visited
        for neighbor in graph.get(node, []):  # Explore all neighbors
            dfs_recursive(graph, neighbor, visited)  # Recur for each neighbor

# Depth-First Search (Non-Recursive Version using Stack)
def dfs_non_recursive(graph, start):
    visited = set()      # Keep track of visited nodes
    stack = [start]      # Use stack for DFS (LIFO)
    while stack:
        node = stack.pop()  # Pop the last inserted node
        if node not in visited:
            print(node, end=" ")  # Print node
            visited.add(node)     # Mark as visited
            # Add neighbors to the stack in reversed order to maintain left-to-right traversal
            stack.extend(reversed(graph.get(node, [])))

# Breadth-First Search (Non-Recursive Version using Queue)
def bfs_non_recursive(graph, start):
    visited = set()     # Track visited nodes
    queue = [start]     # Initialize queue with starting node
    while queue:
        node = queue.pop(0)  # Remove node from front of the queue
        if node not in visited:
            print(node, end=" ")  # Print node
            visited.add(node)     # Mark as visited
            # Add unvisited neighbors to the queue
            queue.extend([n for n in graph.get(node, []) if n not in visited])

# Breadth-First Search (Recursive Version)
def bfs_recursive(graph, queue, visited):
    if not queue:  # Base case: queue is empty
        return
    node = queue.pop(0)  # Process front of queue
    if node not in visited:
        print(node, end=" ")  # Print node
        visited.add(node)     # Mark as visited
        # Add unvisited neighbors to queue
        queue.extend([n for n in graph.get(node, []) if n not in visited])
    bfs_recursive(graph, queue, visited)  # Recursive call for next node in queue

# ----------- Main Driver Code -----------

# Build graph from user input
graph = build_graph()

# Read starting node for traversal
start_node = input("Enter starting node: ")

# Run and display DFS (Recursive)
print("\nDFS Recursive Traversal:")
dfs_recursive(graph, start_node, set())

# Run and display DFS (Non-Recursive)
print("\nDFS Non-Recursive Traversal:")
dfs_non_recursive(graph, start_node)

# Run and display BFS (Non-Recursive)
print("\nBFS Non-Recursive Traversal:")
bfs_non_recursive(graph, start_node)

# Run and display BFS (Recursive)
print("\nBFS Recursive Traversal:")
bfs_recursive(graph, [start_node], set())



# DFS:

# Time Complexity: O(b^d), where b is the branching factor and d is the depth of the solution. The algorithm might explore all nodes in the worst case.

# Space Complexity: O(d), because it only needs to store the current path (depth) in memory.

# BFS:

# Time Complexity: O(b^d), where b is the branching factor and d is the depth of the solution. BFS explores all nodes at a given depth level before moving to the next.

# Space Complexity: O(b^d), because BFS needs to store all nodes at a particular depth level in memory, which can grow exponentially with the branching factor.

# Use Case in AI: DFS is used in game tree search for problems like puzzles where deeper levels of the tree are more important than the breadth of possible actions. It's also used in constraint satisfaction problems when you need to try every possible path.
# Use Case in AI: BFS is often used in shortest pathfinding, such as finding the optimal solution in unweighted problems like maze-solving or pathfinding in grids.
# DFS: Used in game tree exploration where the AI needs to evaluate possible future states. It might be used in minimax algorithms for decision-making in two-player games.
# BFS: Used to find the shortest path in grid-based games (like pathfinding in games, or determining optimal moves in puzzles).
