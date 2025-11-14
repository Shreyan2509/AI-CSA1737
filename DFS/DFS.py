class DFS:
    def __init__(self, graph):
        self.graph = graph

    def traverse(self, start):
        visited = set()
        stack = [start]
        traversal_order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                traversal_order.append(node)
                # Add neighbors in reverse order to visit in original order
                for neighbor in reversed(self.graph.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
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

dfs_instance = DFS(graph)
result = dfs_instance.traverse('A')

print("Depth-First Search traversal:")
print(" ".join(result))
