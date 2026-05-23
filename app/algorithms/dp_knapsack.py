from typing import Dict, List


def solve_knapsack(
    capacity: int, weights: List[int], values: List[int], names: List[str]
) -> Dict:
    """
    Solves the 0/1 Knapsack problem using Dynamic Programming.
    Returns the maximum value, the total weight used, and the list of selected items.
    """
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking to find selected items
    res = dp[n][capacity]
    w = capacity
    selected_indices = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res != dp[i - 1][w]:
            selected_indices.append(i - 1)
            res -= values[i - 1]
            w -= weights[i - 1]

    selected_items = [
        {"name": names[idx], "weight": weights[idx], "value": values[idx]}
        for idx in selected_indices
    ]

    return {
        "max_value": dp[n][capacity],
        "total_weight": capacity - w,
        "selected_items": selected_items,
    }
