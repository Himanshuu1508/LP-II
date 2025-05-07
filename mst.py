''' Implement Greedy Search Algorithm for Minimum Spanning Tree (MST). '''

# Class to represent an Edge in the Undirected Graph
# This class stores information about an edge, including the two vertices it connects (u and v) and its weight.
class Edge:
    def __init__(self, u, v, weight):
        self.u = u  # First vertex of the edge
        self.v = v  # Second vertex of the edge
        self.weight = weight  # Weight of the edge

#<------------------------------------------------------------------------------  

# Function to find the root of a set using path compression
# This function is part of the Union-Find (Disjoint Set) data structure.
# It helps to find the "parent" of a node, i.e., the root of the set that the node belongs to.
def find_parent(parent, node):
    if (parent[node] != node):  # If the node is not its own parent (not the root)
        parent[node] = find_parent(parent, parent[node])  # Recursively find the root and apply path compression
    return parent[node]  # Return the root of the set

#<------------------------------------------------------------------------------  

# Function to join two sets using union by rank
# This function is part of the Union-Find (Disjoint Set) data structure.
# It joins two sets (the sets of vertices u and v) into one, ensuring the tree structure remains balanced.
def union(parent, rank, u, v):
    root_u = find_parent(parent, u)  # Find root of u
    root_v = find_parent(parent, v)  # Find root of v

    if (root_u != root_v):  # If u and v belong to different sets, they are merged
        if (rank[root_u] < rank[root_v]):  # Union by rank: attach the smaller tree under the larger tree
            parent[root_u] = root_v
        elif (rank[root_u] > rank[root_v]):
            parent[root_v] = root_u
        else:  # If both have the same rank, make one root the parent of the other and increase rank
            parent[root_v] = root_u
            rank[root_u] += 1

#<------------------------------------------------------------------------------  

# Kruskal's Algorithm to find the Minimum Spanning Tree (MST)
# Kruskal's algorithm is a greedy algorithm that finds the MST of a graph by selecting edges in order of increasing weight
# and ensuring no cycles are formed.
def kruskal_mst(vertices, edges):
    # Sort edges based on weight in ascending order (greedy step)
    edges.sort(key=lambda edge: edge.weight)

    parent = []  # List to store the parent of each node
    for i in range(vertices):  # Initially, each node is its own parent
        parent.append(i)

    rank = [0] * vertices  # List to store the rank (or depth) of each node's tree
    mst = []  # List to store the edges of the MST

    print("\n Selected Edges in MST : \n")

    for edge in edges:  # Iterate through the edges in sorted order
        u, v = edge.u, edge.v

        # If u and v belong to different sets (i.e., adding the edge won't form a cycle)
        if find_parent(parent, u) != find_parent(parent, v):
            union(parent, rank, u, v)  # Join their sets
            mst.append(edge)  # Add the edge to the MST
            print(f"    Edge ({u} - {v}) with weight {edge.weight}")  # Print the selected edge

        # If the MST already has (vertices - 1) edges, it is complete, so we can stop
        if len(mst) == vertices - 1:
            break

    # Calculate the total weight of the MST
    total_cost = sum(edge.weight for edge in mst)
    print("\n Total weight of MST:", total_cost)  # Print the total weight of the MST
    print("\n Thank You! (-_-)\n")

#<------------------------------------------------------------------------------  

# Driver Code
# This is the main function that interacts with the user and initiates the Kruskal's algorithm to find the MST.
def driver():
    print("\n <--- Minimum Spanning Tree (MST) using Kruskal's Algorithm --->\n")

    print("\n Main Graph Details : ")
    # Ask user for number of vertices and edges in the graph
    vertices = int(input("\n Enter number of Vertices : "))
    e = int(input("\n Enter number of Edges : "))

    edges = []  # List to store edges

    print("\n Enter each Edge in the format : u v weight (eg., 0 1 7  is the edge (0,1) with Weight 7)")
    print("\n Note : Vertex numbering should be from 0 to", vertices - 1,".")  # Prompt user on how to enter edges

    for i in range(e):  # For each edge, get its details and add to the edges list
        u, v, w = map(int, input(f"\n    Edge {i + 1} : ").split())
        edges.append(Edge(u, v, w))  # Create Edge object and add to edges list

    kruskal_mst(vertices, edges)  # Call Kruskal's algorithm to find the MST

#<------------------------------------------------------------------------------  

# Run the program
# This block ensures that the code is only run when this script is executed directly, not when imported.
if __name__ == "__main__":  # This checks if the script is being run directly
    driver()  # Run the driver function to start the program


#A Minimum Spanning Tree (MST) is a subset of the edges in a weighted, connected, undirected graph that connects all the vertices together, without any cycles, and with the minimum possible total edge weight.
#Network Design: MST can be used to design least-cost networks such as telecommunication, electrical grids, or road networks, where you want to connect all nodes with the minimum cost.
#Cluster Analysis: MST can be used in clustering algorithms to minimize the distance between clusters.
#Kruskal’s Algorithm (Greedy) Time Complexity: 𝑂(𝐸log𝐸)
#Prim’s Algorithm (Greedy)Time Complexity:With a simple priority queue: O(ElogV)
# python
# Copy code
# def prim_mst(graph):
#     visited = set()
#     min_edges = [(0, 0)]  # Start with an arbitrary vertex
#     while min_edges:
#         weight, vertex = min_edges.pop(0)
#         if vertex not in visited:
#             visited.add(vertex)
#             for neighbor, edge_weight in graph[vertex]:
#                 if neighbor not in visited:
#                     min_edges.append((edge_weight, neighbor))
# Sample Graph :-

# Vertices = 7

# Edges = 11

# Edge 1: 0 1 7
# Edge 2: 0 3 5
# Edge 3: 1 2 8
# Edge 4: 1 3 9
# Edge 5: 1 4 7
# Edge 6: 2 4 5
# Edge 7: 3 4 15
# Edge 8: 3 5 6
# Edge 9: 4 5 8
# Edge 10: 4 6 9
# Edge 11: 5 6 11
