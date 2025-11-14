import math

class AlphaBetaPruning:
    def __init__(self, values):
        self.values = values
        self.max_depth = int(math.log2(len(values)))

    def alphabeta(self, depth, node_index, maximizing_player, alpha, beta):
        # If leaf node, return its value
        if depth == self.max_depth:
            return self.values[node_index]

        if maximizing_player:
            max_eval = -math.inf
            for i in range(2):  # Left and right child
                eval = self.alphabeta(depth + 1, node_index * 2 + i, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval
        else:
            min_eval = math.inf
            for i in range(2):  # Left and right child
                eval = self.alphabeta(depth + 1, node_index * 2 + i, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, min_eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval


if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("Leaf Nodes =", values)

    alpha_beta = AlphaBetaPruning(values)
    optimal_value = alpha_beta.alphabeta(0, 0, True, -math.inf, math.inf)

    print("Optimal Value =", optimal_value)
