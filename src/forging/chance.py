from dataclasses import dataclass


@dataclass
class Threshold:
    min_relative_level: int
    base_chance: float
    chance_gain: float

# has to be sorted by min_relative_level desc
thresholds = [
    Threshold(60, 0.9, 0.005),
    Threshold(20, 0.5, 0.01),
    Threshold(0, 0, 0.025)
]


def get_threshold(relative_level: int) -> Threshold:
    i = 0
    while relative_level < thresholds[i].min_relative_level:
        i += 1
    return thresholds[i]


def get_relative_level(level: int, difficulty: int) -> int:
    if level < difficulty - 40:
        return 0
    elif level > difficulty + 40:
        return 80
    else:
        return level - (difficulty - 40)


def calculate_forging_success_chance(level: int, difficulty: int):
    rel_level = get_relative_level(level, difficulty)
    threshold = get_threshold(rel_level)
    return threshold.base_chance + (rel_level - threshold.min_relative_level) * threshold.chance_gain
