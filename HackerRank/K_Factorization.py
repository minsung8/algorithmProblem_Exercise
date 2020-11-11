
# K Factorization

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kFactorization function below.
from collections import defaultdict

def kFactorization(n, A):

    A_copy = A.copy()
    answer = -1
    while A_copy:

        temp = A_copy.pop(0)
        temp_list = []
        for x in A:

            if x != temp:
                temp_list.append([temp * x, [temp, x]])
        answer = bfs(temp_list, n, A)

        if answer: return answer

    return -1

def bfs(temp_list, n, A):

    result = []
    for temp in temp_list:

        if temp[0] == n: return temp

        for x in A:

            if x not in temp[1] and x * temp[0] <= n:

                result.append([temp[0] * x, temp[1] + [x]])

    if len(result) > 0: return bfs(result, n, A)

    return

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = kFactorization(n, A)
    if result == -1: print(-1)
    else:
        temp = 1
        answer = "1 "
        for x in result[1]:
            temp *= x
            answer += str(temp) + " "
        print(answer)