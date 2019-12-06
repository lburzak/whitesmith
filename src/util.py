from random import randint


def random_element(l: list):
    return l[randint(0, len(l) - 1)]
