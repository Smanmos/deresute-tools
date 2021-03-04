import numpy as np

WEIGHT_RANGE = np.array(
    [[0, 1.0], [5, 1.1], [10, 1.2], [25, 1.3], [50, 1.4], [70, 1.5], [80, 1.7], [90, 2.0], [100, -1.0]])

DIFF_MULTIPLIERS = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1.025,
    7: 1.05,
    8: 1.075,
    9: 1.1,
    10: 1.2,
    11: 1.225,
    12: 1.25,
    13: 1.275,
    14: 1.3,
    15: 1.4,
    16: 1.425,
    17: 1.45,
    18: 1.475,
    19: 1.5,
    20: 1.6,
    21: 1.65,
    22: 1.7,
    23: 1.75,
    24: 1.8,
    25: 1.85,
    26: 1.9,
    27: 1.95,
    28: 2,
    29: 2.1,
    30: 2.2,
    31: 2.3,
    32: 2.4
}
