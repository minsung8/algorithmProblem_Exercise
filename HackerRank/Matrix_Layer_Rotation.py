import math
import os
import random
import re
import sys

def matrixRotation(matrix, rotate_cnt, m, n):

    num_rings = min(m, n) // 2

    if rotate_cnt >= ((n + m) * 2) - 4:
        rotate_cnt = rotate_cnt % (((n + m) * 2) - 4)

    for cnt in range(rotate_cnt):

        start_n = 0  # 가로
        start_m = 0  # 세로

        for i in range(num_rings):

            # top
            for k in range(start_n, n - start_n - 1):
                temp = matrix[start_n][k]
                matrix[start_n][k] = matrix[start_n][k + 1]
                matrix[start_n][k + 1] = temp

            # right
            for k in range(start_m, m - start_m - 1):
                temp = matrix[k][n - start_n - 1]
                matrix[k][n - start_n - 1] = matrix[k + 1][n - start_n - 1]
                matrix[k + 1][n - start_n - 1] = temp

            # bottom
            for k in range(n - start_n - 1, start_n, -1):
                temp = matrix[m - start_m - 1][k]
                matrix[m - start_m - 1][k] = matrix[m - start_m - 1][k - 1]
                matrix[m - start_m - 1][k - 1] = temp

            # left
            for k in range(m - start_m - 1, start_m + 1, -1):
                temp = matrix[k][start_n]
                matrix[k][start_n] = matrix[k - 1][start_n]
                matrix[k - 1][start_n] = temp

            start_n += 1
            start_m += 1

    return matrix

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])         # 세로

    n = int(mnr[1])         # 가로

    rotate_cnt = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    answer = matrixRotation(matrix, rotate_cnt, m, n)

    for i in range(len(answer)):
        temp = ""
        for j in range(len(answer[0])):
            temp += str(answer[i][j]) + " "
        print(temp)