from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, visited):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in self.graph[node]:
                self.dfs(neighbor, visited)

    def dfs_traversal(self, start_node):
        visited = set()
        print("Depth-First Search (DFS) Traversal:")
        self.dfs(start_node, visited)
        print()

    def bfs_traversal(self, start_node):
        visited = set()
        queue = []
        print("Breadth-First Search (BFS) Traversal:")
        queue.append(start_node)
        visited.add(start_node)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        print()

# Create a graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Perform DFS and BFS traversals
g.dfs_traversal(2)
g.bfs_traversal(2)

# In this code:

# 1. We define a Graph class with methods to add edges (add_edge), perform DFS traversal (dfs_traversal), and perform BFS traversal (bfs_traversal). 
#2. The dfs function recursively explores nodes in a depth-first manner and marks them as visited.

# 3. The dfs_traversal method starts DFS traversal from a given node.

# 4. The bfs_traversal method performs BFS traversal using a queue.

# 5. We create a sample graph and perform both DFS and BFS traversals starting from node 2.