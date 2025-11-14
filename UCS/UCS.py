import heapq

class UniformCostSearch:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal):
        heap = []
        heapq.heappush(heap, (0, start))
        visited = set()
        parent = {start: None}
        cost_so_far = {start: 0}

        while heap:
            current_cost, current_node = heapq.heappop(heap)

            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == goal:
                path = self._reconstruct_path(parent, goal)
                return current_cost, path

            for neighbor, edge_cost in self.graph.get(current_node, []):
                new_cost = current_cost + edge_cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    parent[neighbor] = current_node
                    heapq.heappush(heap, (new_cost, neighbor))

        return float('inf'), []

    def _reconstruct_path(self, parent, goal):
        path = []
        while goal is not None:
            path.append(goal)
            goal = parent[goal]
        path.reverse()
        return path

# Example graph (adjacency list with weights)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
goal_node = 'D'

ucs = UniformCostSearch(graph)
cost, path = ucs.search(start_node, goal_node)

print("Uniform Cost Search Result:")
print("Path:", " -> ".join(path))
print("Total Cost:", cost)
