import heapq

class GreedyBFS:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def search(self, start, goal):
        visited = set()
        heap = []
        heapq.heappush(heap, (self.heuristic[start], start))
        parent = {start: None}

        while heap:
            _, current = heapq.heappop(heap)
            visited.add(current)

            if current == goal:
                print("Goal found!")
                return self._reconstruct_path(parent, goal)

            for neighbor in self.graph.get(current, []):
                if neighbor not in visited and neighbor not in parent:
                    heapq.heappush(heap, (self.heuristic[neighbor], neighbor))
                    parent[neighbor] = current

        return None

    def _reconstruct_path(self, parent, goal):
        path = []
        while goal is not None:
            path.append(goal)
            goal = parent[goal]
        path.reverse()
        return path

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 7,
    'E': 2,
    'F': 0
}

start = 'A'
goal = 'F'

gbfs = GreedyBFS(graph, heuristic)
result = gbfs.search(start, goal)

if result:
    print("Path found:", " → ".join(result))
else:
    print("No path found.")
