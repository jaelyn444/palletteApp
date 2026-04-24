# base paints:
#   white = (255, 255, 255)  weight = 0.6
#   blue  = (0,   0,   255)  weight = 0.3
#   black = (0,   0,   0)    weight = 0.1
#                                     ---
#                                     1.0  ← must always add up to 1

# result:
#   r = (255 × 0.6) + (0 × 0.3) + (0 × 0.1)   = 153
#   g = (255 × 0.6) + (0 × 0.3) + (0 × 0.1)   = 153
#   b = (255 × 0.6) + (255 × 0.3) + (0 × 0.1) = 228

# mixed color = (153, 153, 228) ← a light blue

import numpy as np
from scipy.optimize import minimize

BASE_PAINTS = {
    "red":    [255, 0,   0],
    "blue":   [0,   0,   255],
    "yellow": [255, 255, 0],
    "white":  [255, 255, 255],
    "black":  [0,   0,   0],
}

def mix_paints(weights: list, base_colors: list) -> np.ndarray:
    weights = np.array(weights)
    base_colors = np.array(base_colors)
    return np.dot(weights, base_colors)

def loss_function(weights: list, base_colors: list, target: list) -> float:
    mixed = mix_paints(weights, base_colors)
    return np.sum((mixed - target) ** 2)

def find_paint_mix(target_color: list) -> dict:
    base_colors = list(BASE_PAINTS.values())
    base_names = list(BASE_PAINTS.keys())
    n = len(base_colors)

    initial_weights = [1/n] * n

    constraints = {"type": "eq", "fun": lambda w: np.sum(w) - 1}
    # all weights must add up to 1
    # (100% total paint, no more no less)
    bounds = [(0, 1)] * n
    # every weight must be between 0 and 1
    # (can't use -20% of a paint)

    result = minimize(
        loss_function,
        initial_weights,
        args=(base_colors, target_color),
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    mix = {}
    for i, weight in enumerate(result.x):
        if weight > 0.01:
            mix[base_names[i]] = round(float(weight), 2)

    return mix

