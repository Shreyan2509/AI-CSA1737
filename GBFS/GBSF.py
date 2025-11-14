from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))
    path = []

    while not pq.empty():
        _, current = pq.get()
        path.append(current)
        visited.add(current)

        if current == goal:
            print("Goal found!")
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

    return None


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (estimated distance to goal)
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

result = greedy_best_first_search(graph, start, goal, heuristic)

if result:
    print("Path found:", " → ".join(result))
else:
    print("No path found.")
