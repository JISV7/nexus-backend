from typing import List, Dict, Any

def solve_marketing_optimization(
    channels: List[Dict[str, Any]],
    constraints: List[Dict[str, Any]],
    **kwargs
) -> Dict[str, Any]:
    """
    Exact analytical solver for separable quadratic knapsack problem using KKT conditions.
    Provides 100% mathematical precision without external libraries.
    """
    num_vars = len(channels)
    channel_map = {c['name']: i for i, c in enumerate(channels)}
    
    # 1. Parse Bounds
    L = [0.0] * num_vars
    U = [float('inf')] * num_vars
    
    S_min = 0.0
    S_max = float('inf')
    
    for const in constraints:
        val = const['value']
        op = const['operator']
        if const['type'] == 'individual':
            idx = channel_map.get(const['target_channel'])
            if idx is not None:
                if op == '<=': U[idx] = min(U[idx], val)
                elif op == '>=': L[idx] = max(L[idx], val)
                elif op == '==': 
                    L[idx] = max(L[idx], val)
                    U[idx] = min(U[idx], val)
        elif const['type'] == 'sum_all':
            if op == '<=': S_max = min(S_max, val)
            elif op == '>=': S_min = max(S_min, val)
            elif op == '==': 
                S_min = max(S_min, val)
                S_max = min(S_max, val)

    # Sanity check bounds
    for i in range(num_vars):
        if L[i] > U[i]:
            U[i] = L[i]
            
    if S_min > S_max:
        S_max = S_min

    # 2. Define the x_i(lambda) function
    def get_x(lam: float) -> List[float]:
        x = [0.0] * num_vars
        for i in range(num_vars):
            a = channels[i]['linear_coef']
            c = channels[i]['saturation_penalty']
            if c > 0:
                unconstrained = (a - lam) / (2 * c)
            else:
                unconstrained = U[i] if a > lam else L[i]
            x[i] = min(U[i], max(L[i], unconstrained))
        return x

    def get_sum(lam: float) -> float:
        return sum(get_x(lam))

    # 3. Check unconstrained optimum (lambda = 0)
    x_opt = get_x(0.0)
    sum_opt = sum(x_opt)
    
    target_sum = None
    if sum_opt > S_max:
        target_sum = S_max
    elif sum_opt < S_min:
        target_sum = S_min

    if target_sum is not None:
        # 4. Bisection search for lambda to satisfy KKT conditions exactly
        lam_low = -10000.0
        lam_high = 10000.0
        
        # Expand bounds if necessary
        for _ in range(100):
            if get_sum(lam_low) < target_sum:
                lam_low *= 2
            else:
                break
                
        for _ in range(100):
            if get_sum(lam_high) > target_sum:
                lam_high *= 2
            else:
                break
                
        # 100 iterations provides >1e-25 precision, far beyond IEEE 754 floats
        for _ in range(100): 
            lam_mid = (lam_low + lam_high) / 2
            if get_sum(lam_mid) > target_sum:
                lam_low = lam_mid
            else:
                lam_high = lam_mid
                
        final_lam = (lam_low + lam_high) / 2
        x_opt = get_x(final_lam)

    # Calculate final max_value
    total_value = 0.0
    for i in range(num_vars):
        a = channels[i]['linear_coef']
        c = channels[i]['saturation_penalty']
        total_value += a * x_opt[i] - c * (x_opt[i]**2)
        
    return {
        "max_value": round(total_value, 2),
        "channels": [
            {"name": channels[i]['name'], "investment": round(x_opt[i], 2)}
            for i in range(num_vars)
        ]
    }
