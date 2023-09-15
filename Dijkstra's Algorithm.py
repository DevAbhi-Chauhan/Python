import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start_node):
        # Initialize distances to all nodes as infinity, except the start node as 0
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0

        # Priority queue (min-heap) to store nodes and their distances
        pq = [(0, start_node)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            # Skip if we've already processed this node
            if current_distance > distances[current_node]:
                continue

            # Explore neighbors of the current node
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                # Update the distance if it's shorter than the current known distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

# Create a graph
g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'E', 3)
g.add_edge('E', 'A', 2)

# Find the shortest path distances from 'A' to all other nodes
start_node = 'A'
shortest_distances = g.dijkstra(start_node)

# Display the shortest path distances
for node, distance in shortest_distances.items():
    print(f'Shortest distance from {start_node} to {node}: {distance}')

# In this code:

# 1. The Graph class represents a weighted graph using an adjacency list.
# 2. The add_edge method allows you to add edges with weights to the graph.
# 3. The dijkstra method finds the shortest path distances from a specified start_node to all other nodes using Dijkstra's algorithm.
# 4. A priority queue (min-heap) is used to keep track of nodes and their distances while exploring the graph.
# 5. The shortest path distances are stored in the distances dictionary.