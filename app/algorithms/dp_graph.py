from typing import Any, Dict, List


def solve_graph_routing(stages: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Finds the shortest path in a multi-stage graph using Backward Dynamic Programming.
    Stages is a list of dicts, where each dict maps source node to its destinations and costs.
    Example input format:
    stages = [
        {"A": {"B": 4, "C": 6, "D": 3}}, # Stage 1
        {"B": {"E": 7, "F": 5}, "C": {"E": 3, "F": 8, "G": 4}, "D": {"F": 6, "G": 9}}, # Stage 2
        ...
    ]
    """
    # Number of stages (from stage 1 to the last stage pointing to sink)
    # We assume the last stage points to the final destination node (e.g., J)

    # Cost to reach destination from current node
    # Initialize with the last stage costs to sink
    # Actually, it's easier to process from the last stage backwards

    # costs_to_end[node] = min cost to reach J from node
    costs_to_end: Dict[str, float] = {}
    next_node: Dict[str, str | None] = {}

    # Process from last stage to first
    for stage in reversed(stages):
        new_costs: Dict[str, float] = {}
        for source, destinations in stage.items():
            min_cost = float("inf")
            best_dest = None

            for dest, cost in destinations.items():
                # If dest is the sink (not in costs_to_end yet because it's the target)
                # or if it's already computed
                future_cost = costs_to_end.get(dest, 0.0)
                total = cost + future_cost
                if total < min_cost:
                    min_cost = total
                    best_dest = dest

            new_costs[source] = min_cost
            next_node[source] = best_dest

        costs_to_end.update(new_costs)

    # Reconstruct path starting from the first node of the first stage
    start_node = list(stages[0].keys())[0]  # Assume only one start node A
    path = [start_node]
    curr: str | None = start_node
    while curr is not None and curr in next_node:
        curr = next_node[curr]
        if curr is not None:
            path.append(curr)

    return {"min_latency": costs_to_end[start_node], "path": path}
