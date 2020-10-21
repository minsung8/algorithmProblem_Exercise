from math import inf
import os
import random
import re
import sys
from collections import defaultdict

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().split())

    q = int(input())
    dp = [[inf for i in range(road_edges)] for j in range(road_edges)]

    for i in range(len(road_from)):
        dp[road_from[i] - 1][road_to[i] - 1] = road_weight[i]

    for k in range(road_edges):
        for i in range(road_edges):
            for j in range(road_edges):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                if i == j: dp[i][j] = 0

    for q_itr in range(q):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        answer = dp[x - 1][y - 1]
        if answer == inf: print(-1)
        else: print(answer)