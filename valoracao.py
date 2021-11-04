# DONE
from bitset import Bitset


class Valoracao(Bitset):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return str(super().asInt())

    def __repr__(self):
        return str(super().asInt())