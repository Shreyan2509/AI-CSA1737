import heapq

def uniform_cost_search(graph, start, goal):
    # Priority queue -> (cost, node, path)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        # Goal test
        if node == goal:
            return cost, path

        # Expand neighbors
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                total_cost = cost + edge_cost
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))

    return float('inf'), []  # if goal not reachable

# Example graph (adjacency list with weights)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_node = 'A'
goal_node = 'D'

cost, path = uniform_cost_search(graph, start_node, goal_node)

print("Uniform Cost Search Result:")
print("Path:", " -> ".join(path))
print("Total Cost:", cost)
