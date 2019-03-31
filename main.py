
from string import ascii_lowercase as abc
from itertools import cycle
from operator import add, sub


def encrypt(key):
    key = cycle(ord(p) - 97 for p in key)
    return "".join(abc[(ord(i) + next(key) - 97) % 26] for i in abc)


def decrypt(key):
    key = cycle(ord(p) - 97 for p in key)
    return "".join(abc[(ord(i) - next(key) - 97) % 26] for i in abc)


def start_shift(key, op):
    return op(abc[abc.index(key):], abc[:abc.index(key)])


if __name__ == "__main__":
    print(add("Alphabet:\t\t", abc))
    print(add("Encrypt:\t\t", encrypt("k")))
    print(add("Decrypt:\t\t", decrypt("k")))
    print(add("Start-Shift:\t", start_shift("k", add)))
