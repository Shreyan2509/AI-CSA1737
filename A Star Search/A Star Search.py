import heapq

class AStarPathfinder:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics

    def find_path(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (self.heuristics[start], start))

        came_from = {}
        g_score = {node: float('inf') for node in self.graph}
        g_score[start] = 0

        while open_set:
            current_f, current = heapq.heappop(open_set)

            if current == goal:
                return self._reconstruct_path(came_from, current), g_score[current]

            for neighbor, cost in self.graph.get(current, []):
                tentative_g = g_score[current] + cost
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristics.get(neighbor, float('inf'))
                    heapq.heappush(open_set, (f_score, neighbor))

        return [], float('inf')  # Goal not reachable

    def _reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


# Example graph and heuristics (same as before)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 3,
    'G': 0
}

start_node = 'A'
goal_node = 'G'
pathfinder = AStarPathfinder(graph, heuristics)
path, cost = pathfinder.find_path(start_node, goal_node)

print("A* Search Result:")
print("Path:", " -> ".join(path))
print("Total Cost:", cost)
