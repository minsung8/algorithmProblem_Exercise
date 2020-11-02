# K Factorization

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kFactorization function below.
def kFactorization(n, A):

    temp = []

    for i in A:
        temp.append([[i], n - i])

    while temp:

        start = temp.pop(0)

        if start[1] == 0: return start[0]
        if start[1] < 0: continue

        for i in A:
            if i not in start[0]:
                temp_list = start[0] + [i]
                temp.append([temp_list, start[1] - (i * start[1])])

    return -1


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = kFactorization(n, A)
    print(result)

