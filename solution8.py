# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42891

import sys
sys.setrecursionlimit(5000)
def solution(food_times, k):
    idx = 0
    cnt = 0
    dic = {}
    while cnt < k:
        if food_times[idx] != 0:
            food_times[idx] -= 1
            cnt += 1

        idx = next_idx(idx, food_times, dic)

        if idx == -1: return -1
    if food_times[idx] != 0: return idx + 1

    return next_idx(idx, food_times, dic)

def next_idx(idx, food_times, dic):
    if len(dic) == len(food_times): return -1
    answer = idx + 1
    if answer == len(food_times): answer = 0

    if food_times[answer] != 0: return answer
    else:
        dic[answer] = answer + 1
        dic[answer] = next_idx(answer, food_times, dic)
        return dic[answer]

print(solution([3, 1, 2], 6))




