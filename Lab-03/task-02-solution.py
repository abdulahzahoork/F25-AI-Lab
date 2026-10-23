
# DLS

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": ["G"],
    "G": []
}

FOUND = "FOUND"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"


def dls(node, goal, limit, depth=0, path=None):
    if path is None:
        path = []

    # Path-local cycle check
    if node in path:
        return FAILURE, []

    path = path + [node]

    # Goal test
    if node == goal:
        return FOUND, path

    # Depth limit reached
    if depth == limit:
        if graph[node]:
            return CUTOFF, []
        return FAILURE, []

    cutoff_occurred = False

    for child in graph[node]:
        status, result_path = dls(
            child, goal, limit, depth + 1, path
        )

        if status == FOUND:
            return FOUND, result_path

        if status == CUTOFF:
            cutoff_occurred = True

    if cutoff_occurred:
        return CUTOFF, []

    return FAILURE, []


# Test limits 1, 2, 3 and 4
for limit in [1, 2, 3, 4]:
    status, path = dls("A", "G", limit)

    print(f"Limit: {limit}")
    print(f"Status: {status}")
    print(f"Path: {' -> '.join(path) if path else 'None'}")
    print()
