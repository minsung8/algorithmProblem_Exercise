import math
import os
import random
import re
import sys
from collections import defaultdict

def check(x, y, dic):
    answer = []

    temp = [[x, 0]]

    while temp:

        start = temp.pop(0)

        if start[0] == y:
            answer.append(start[1])
            continue

        for a in dic[start[0]]:
            if a[0] != x:
                temp.append([a[0], start[1] + a[1]])

    return answer

if __name__ == '__main__':
    road_nodes, road_edges = map(int, input().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().split())

    dic = defaultdict(list)

    for i in range(len(road_from)):
        dic[road_from[i]].append([road_to[i], road_weight[i]])
    q = int(input())
    for q_itr in range(q):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        cost_list = check(int(x), int(y), dic)

        if len(cost_list) == 0: print(-1)
        else: print(min(cost_list))