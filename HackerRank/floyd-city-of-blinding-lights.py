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

    edge = defaultdict(list)

    for i in range(len(road_from)):
        edge[road_from[i]].append([road_to[i], road_weight[i]])

    questions = [
        tuple(int(x) for x in input().strip().split())
        for _ in range(int(input()))
    ]

    questions_dict = dict()
    for fr, to in questions:
        if fr not in questions_dict:
            questions_dict[fr] = {to}
        else:
            questions_dict[fr].add(to)
    answer_dic = dict()
    for i in questions_dict.keys():
        dists = [inf] * (road_nodes + 1)
        dists[i] = 0
        visited = [i]
        while visited:
            next_visited = set()

            for node in visited:
                temp_cost = dists[node]
                for node_cost in edge[node]:
                    temp_cost2 = node_cost[1] + temp_cost

                    if dists[node_cost[0]] == inf or dists[node_cost[0]] > temp_cost2:
                        dists[node_cost[0]] = temp_cost2
                        next_visited.add(node_cost[0])
            visited = next_visited

        answer_dic[i] = dists

    for start, end in questions:
        answer = answer_dic[start][end]
        if answer == inf: print(-1)
        else: print(answer)













