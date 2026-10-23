# BFS


graph = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["F"],
    "D" : [],
    "E" : [],
    "F" : ["G"],
    "G" : []
}

visited = []
queue = []

def bfs(node):
    queue.append(node)
    
    while queue:
        print(f"Queue: {queue}, Visited: {visited}")
        temp = queue.pop(0)
        visited.append(temp)

        for child in graph[temp]:
            queue.append(child)

bfs("A")

# DFS

visited = []
stack = []

def dfs(node):
    stack.append(node)
    
    while stack:
        print(f"Stack: {stack}, Visited: {visited}")
        temp = stack.pop()
        visited.append(temp)

        for child in graph[temp]:
            stack.append(child)

dfs("A")