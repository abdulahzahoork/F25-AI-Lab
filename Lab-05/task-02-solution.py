import math
 
# Counts how many leaf nodes each algorithm evaluates
leaf_count = 0
 
 
# ---------------- Minimax ----------------
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global leaf_count
 
    if curDepth == targetDepth:
        leaf_count += 1
        return scores[nodeIndex]
 
    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )
 
 
# ---------------- Alpha-Beta Pruning ----------------
def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global leaf_count
 
    if depth == target:
        leaf_count += 1
        return scores[index]
 
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(depth + 1, index * 2 + i, False, scores, target, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(depth + 1, index * 2 + i, True, scores, target, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
 
 
# ---------------- Driver code: Minimax ----------------
scores = [3, 5, 2, 9, 0, 7]
treeDepth = math.ceil(math.log2(len(scores)))

scores += [0] * (2**treeDepth - len(scores))
 
leaf_count = 0
print("Minimax optimal value is:", minimax(0, 0, True, scores, treeDepth))
print("Minimax leaf nodes evaluated:", leaf_count)
 
# ---------------- Driver code: Alpha-Beta ----------------
scores = [3, 5, 2, 9, 3, 5, 2, 9]
depth = int(math.log2(len(scores)))
 
leaf_count = 0
print("Alpha-Beta optimal value is:", alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf')))
print("Alpha-Beta leaf nodes evaluated:", leaf_count, "out of", len(scores))