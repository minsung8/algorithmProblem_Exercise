# https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true

from itertools import permutations

def biggerIsGreater(w):

    temp_list = sorted(list(set(permutations(list(w), len(w)))))
    idx = temp_list.index(tuple(w))

    if idx > len(temp_list) - 2:
        return "no answer"

    return "".join(temp_list[idx + 1])

print(biggerIsGreater("zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw"))

# print(biggerIsGreater("ab"))  # ba
# print(biggerIsGreater("bb"))  # no answer
# print(biggerIsGreater("hefg"))  # hegf
# print(biggerIsGreater("dhck"))  # dhkc
# print(biggerIsGreater("dkhc"))  # hcdk
# print(biggerIsGreater("abcd"))  # abdc

# print(biggerIsGreater("a"))