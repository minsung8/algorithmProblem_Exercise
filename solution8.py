# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq

def solution(food_times, k):

    if sum(food_times) <= k: return -1

    if k < len(food_times):
        return k + 1

    food_times = [(food, idx) for idx, food in enumerate(food_times, 1)]
    heapq.heapify(food_times)

    small_food = food_times[0][0]
    prev = 0
    while k - ((small_food - prev) * len(food_times)) >= 0:
        k -= (small_food - prev) * len(food_times)
        prev, index = heapq.heappop(food_times)
        small_food = food_times[0][0]

    food_times = sorted(food_times, key=lambda x: x[1])

    return food_times[k % len(food_times)][1]