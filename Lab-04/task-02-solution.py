
import heapq
from itertools import count

GRAPH = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": [],
}

H = {
    "S": 0,
    "A": 0,
    "B": 3,
    "C": 0,
    "G": 0,
}


def search(start, goal, heuristic=None):
    # Use zero heuristic for UCS
    if heuristic is None:
        heuristic = {}

    tie = count()
    frontier = [
        (heuristic.get(start, 0), next(tie), 0, start, [start])
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
                new_f = new_g + heuristic.get(neighbor, 0)

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


# UCS
ucs_path, ucs_cost, ucs_expanded = search("S", "G")

# A*
astar_path, astar_cost, astar_expanded = search("S", "G", H)

print("UCS")
print("Path:", " -> ".join(ucs_path))
print("Cost:", ucs_cost)
print("Expanded:", ucs_expanded)
print("Expansion count:", len(ucs_expanded))

print("\nA*")
print("Path:", " -> ".join(astar_path))
print("Cost:", astar_cost)
print("Expanded:", astar_expanded)
print("Expansion count:", len(astar_expanded))
