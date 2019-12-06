from random import randint


def random_element(l: list):
    return l[randint(0, len(l) - 1)]


def float_as_percent(value: float) -> str:
    return "%2.2f%%" % (value * 100)

print(float_as_percent(0.123))
