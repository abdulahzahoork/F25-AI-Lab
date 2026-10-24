
import heapq
from itertools import count

GRAPH = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}

# Updated heuristic: h(C) = 10
H = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 10,
    "G": 0,
}


def astar(start, goal):
    tie = count()
    frontier = [
        (H[start], next(tie), 0, start, [start])
    ]
    best_cost = {start: 0}
    expanded = []

    while frontier:
        f, _, g, node, path = heapq.heappop(frontier)

        if g != best_cost.get(node):
            continue

        if node == goal:
            return path, g, expanded

        expanded.append(node)

        for neighbor, edge_cost in GRAPH[node]:
            new_g = g + edge_cost

            if new_g < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_g
                new_f = new_g + H[neighbor]

                heapq.heappush(
                    frontier,
                    (
                        new_f,
                        next(tie),
                        new_g,
                        neighbor,
                        path + [neighbor],
                    ),
                )

    return None, float("inf"), expanded


path, cost, expanded = astar("S", "G")

print("A* Search")
print("Path:", " -> ".join(path))
print("Cost:", cost)
print("Expanded:", expanded)
print("Expansion count:", len(expanded))
