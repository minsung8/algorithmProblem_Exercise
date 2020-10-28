import math
import os
import random
import re
import sys

def matrixRotation(matrix, rotate_cnt, m, n):

    num_rings = min(m, n) // 2

    for i in range(num_rings):

        temp_rotate_cnt = rotate_cnt % (2 * (m + n - 4 * i) - 4)

        for cnt in range(temp_rotate_cnt):

            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][j + 1]
                matrix[i][j + 1] = tmp

            for j in range(i, m - i - 1):
                tmp = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = matrix[j + 1][n - i - 1]
                matrix[j + 1][n - i - 1] = tmp

            for j in range(n - i - 1, i, -1):
                tmp = matrix[m - i - 1][j]
                matrix[m - i - 1][j] = matrix[m - i - 1][j - 1]
                matrix[m - i - 1][j - 1] = tmp

            for j in range(m - i - 1, i + 1, -1):
                tmp = matrix[j][i]
                matrix[j][i] = matrix[j - 1][i]
                matrix[j - 1][i] = tmp

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