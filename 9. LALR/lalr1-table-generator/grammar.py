from parsing.grammar import *


def get_sample_1():
    return Grammar([
        NonTerminal('S', [
            "a A"
        ]),
        NonTerminal('A', [
            " '=' B"
        ]),
        NonTerminal('B', [
            "b '+' C"
        ]),
        NonTerminal('C', [
            "c '*' d", "'(' C ')'"
        ])
    ])

def get_len_1():
    return 4
    

# S -> a A
# A -> = B
# B -> b + C
# C -> c * d | ( C )
