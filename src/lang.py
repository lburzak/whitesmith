from random import randint

from util import random_element

vowels = ["a", "e", "y", "o", "u", "i"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "w", "z", "x"]
endings = ["chit", "ryt", "mit", "t", "ks"]


def noun_to_adj(noun: str) -> str:
    female = False
    if noun[-1] == 'a':
        female = True

    if noun[-1] in vowels:
        noun = noun[:-1]

    if female:
        return noun + "owa"
    else:
        return noun + "owy"


def generate_metal_name(max_length: int = 2) -> str:
    size = randint(0, max_length)
    temp = 0
    s = []
    while temp <= size:
        s.append(consonants[randint(0, len(consonants) - 1)] + vowels[randint(0, len(vowels) - 1)])
        temp += 1
    return (''.join(s) + random_element(endings)).capitalize()
