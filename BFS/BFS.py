from collections import deque

class BFS:
    def __init__(self, graph):
        self.graph = graph

    def traverse(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        traversal_order = []

        while queue:
            node = queue.popleft()
            traversal_order.append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs_instance = BFS(graph)
result = bfs_instance.traverse('A')

print("Breadth-First Search traversal:")
print(" ".join(result))
