import math
orders = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [5, 6, 7, 8, 1, 2, 3, 4],
    [8, 7, 6, 5, 4, 3, 2, 1]
]

treeDepth = math.log2(len(orders[0]))
leafCount = 0

def minMax(curDepth, nodeIndex, isMaxTurn):
    global leafCount

    if curDepth == treeDepth:
        leafCount = leafCount + 1
        return scores[nodeIndex]

    if isMaxTurn:
        return max(minMax(curDepth + 1, nodeIndex * 2, False),
                   minMax(curDepth + 1, nodeIndex * 2 + 1, False))
    else:
        return min(minMax(curDepth + 1, nodeIndex * 2, True),
                   minMax(curDepth + 1, nodeIndex * 2 + 1, True))


def alphaBeta(curDepth, nodeIndex, isMaxTurn, alpha, beta):
    global leafCount

    if curDepth == treeDepth:
        leafCount = leafCount + 1
        return scores[nodeIndex]

    if isMaxTurn:
        best = -1000
        for i in range(2):
            value = alphaBeta(curDepth + 1, nodeIndex * 2 + i, False, alpha, beta)
            if value > best:
                best = value
            if best > alpha:
                alpha = best
            if alpha >= beta:
                break
        return best
    else:
        best = 1000
        for i in range(2):
            value = alphaBeta(curDepth + 1, nodeIndex * 2 + i, True, alpha, beta)
            if value < best:
                best = value
            if best < beta:
                beta = best
            if alpha >= beta:
                break
        return best



for order in orders:
    scores = order

    leafCount = 0
    minimaxValue = minMax(0, 0, True)
    minimaxLeaves = leafCount

    leafCount = 0
    alphaBetaValue = alphaBeta(0, 0, True, -1000, 1000)
    alphaBetaLeaves = leafCount

    print("Scores:", scores)
    print("Minimax value:", minimaxValue, "| Leaves:", minimaxLeaves)
    print("Alpha-Beta value:", alphaBetaValue, "| Leaves:", alphaBetaLeaves)
    print()