from os import stat
import sys

import numpy as np


class Gates:
    X = np.fliplr(np.eye(2, dtype=complex))
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    S = np.array([[1, 0], [0, 1j]], dtype=complex)
    T = np.array([[1, 0], [0, (1 + 1j) / np.sqrt(2)]], dtype=complex)
    H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)

    @staticmethod
    def get(key):
        return getattr(Gates, key)

class States:
    ZERO = np.array([[1], [0]], dtype=complex)
    ONE = np.array([[0], [1]], dtype=complex)

    @staticmethod
    def get(key):
        return {
            "0": States.ZERO,
            "1": States.ONE,
        }.get(key)


instructions = list(reversed(sys.argv[1]))
state = States.get(instructions.pop(0))
for gate in instructions:
    state = Gates.get(gate) @ state

print(state)
