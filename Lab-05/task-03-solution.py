import math
orders = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [5, 6, 7, 8, 1, 2, 3, 4],
    [8, 7, 6, 5, 4, 3, 2, 1]
]

tree_depth = math.log2(len(orders[0]))
leaf_count = 0

def min_max(cur_depth, node_index, is_max_turn):
    global leaf_count

    if cur_depth == tree_depth:
        leaf_count = leaf_count + 1
        return scores[node_index]

    if is_max_turn:
        return max(min_max(cur_depth + 1, node_index * 2, False),
                   min_max(cur_depth + 1, node_index * 2 + 1, False))
    else:
        return min(min_max(cur_depth + 1, node_index * 2, True),
                   min_max(cur_depth + 1, node_index * 2 + 1, True))


def alpha_beta(cur_depth, node_index, is_max_turn, alpha, beta):
    global leaf_count

    if cur_depth == tree_depth:
        leaf_count = leaf_count + 1
        return scores[node_index]

    if is_max_turn:
        best = -1000
        for i in range(2):
            value = alpha_beta(cur_depth + 1, node_index * 2 + i, False, alpha, beta)
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
            value = alpha_beta(cur_depth + 1, node_index * 2 + i, True, alpha, beta)
            if value < best:
                best = value
            if best < beta:
                beta = best
            if alpha >= beta:
                break
        return best



for order in orders:
    scores = order

    leaf_count = 0
    minimax_value = min_max(0, 0, True)
    minimax_leaves = leaf_count

    leaf_count = 0
    alpha_beta_value = alpha_beta(0, 0, True, -1000, 1000)
    alpha_beta_leaves = leaf_count

    print("Scores:", scores)
    print("Minimax value:", minimax_value, "| Leaves:", minimax_leaves)
    print("Alpha-Beta value:", alpha_beta_value, "| Leaves:", alpha_beta_leaves)
    print()