from typing import Callable, Tuple, Dict, Any

def solve_marketing_optimization(
    func: Callable[[float, float], float],
    grad_func: Callable[[float, float], Tuple[float, float]],
    budget: float,
    x1_init: float = 0.0,
    x2_init: float = 0.0,
    learning_rate: float = 0.01,
    iterations: int = 1000,
    penalty_factor: float = 100.0
) -> Dict[str, Any]:
    """
    Solves Non-Linear maximization problem with Gradient Ascent and Penalty.
    Maximize f(x1, x2) subject to x1 + x2 <= budget, x1 >= 0, x2 >= 0.
    """
    x1, x2 = x1_init, x2_init
    
    for _ in range(iterations):
        # Calculate gradients of the objective function
        g1, g2 = grad_func(x1, x2)
        
        # Add penalty for budget constraint: x1 + x2 <= budget
        # Constraint g(x1, x2) = x1 + x2 - budget <= 0
        if x1 + x2 > budget:
            violation = (x1 + x2 - budget)
            # Derivative of penalty (penalty_factor * violation^2) is 2 * penalty_factor * violation
            penalty_grad = 2 * penalty_factor * violation
            g1 -= penalty_grad
            g2 -= penalty_grad
            
        # Add penalty for non-negativity: x1 >= 0, x2 >= 0
        if x1 < 0:
            g1 -= 2 * penalty_factor * x1
        if x2 < 0:
            g2 -= 2 * penalty_factor * x2
            
        # Update variables (Ascent because it's maximization)
        x1 += learning_rate * g1
        x2 += learning_rate * g2
        
        # Simple projection to non-negative space as a backup
        x1 = max(0, x1)
        x2 = max(0, x2)
        
        # Budget projection if needed
        if x1 + x2 > budget:
            scale = budget / (x1 + x2)
            x1 *= scale
            x2 *= scale

    return {
        "x1": round(x1, 4),
        "x2": round(x2, 4),
        "max_value": round(func(x1, x2), 4)
    }

def create_quadratic_model(a: float, b: float, c: float, d: float, e: float, f: float):
    """
    Creates f(x1, x2) = a*x1 + b*x2 - c*x1^2 - d*x2^2 + e*x1*x2 + f
    And its gradient.
    Example: 4x1 + 5x2 - 0.2x1^2 - 0.3x2^2
    a=4, b=5, c=0.2, d=0.3, e=0, f=0
    """
    def func(x1, x2):
        return a*x1 + b*x2 - c*(x1**2) - d*(x2**2) + e*x1*x2 + f
    
    def grad(x1, x2):
        # df/dx1 = a - 2*c*x1 + e*x2
        # df/dx2 = b - 2*d*x2 + e*x1
        df1 = a - 2*c*x1 + e*x2
        df2 = b - 2*d*x2 + e*x1
        return df1, df2
        
    return func, grad
