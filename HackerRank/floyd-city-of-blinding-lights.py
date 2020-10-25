from sys import stdin
from collections import defaultdict
import heapq

n, m = (int(x) for x in stdin.readline().split())

edges = defaultdict(dict)

for i in range(m):
    start, end, cost = (int(j) for j in stdin.readline().split())
    edges[start][end] = cost

q = int(stdin.readline().strip())
answer = {}
heap = {}

for i in range(1, n + 1):
    answer[i] = {}
    heap[i] = [[0, i]]

for i in range(q):

    start, end = (int(x) for x in stdin.readline().split())

    while end not in answer[start]:

        if not heap[start]:             # start > end 로 가는 경로가 없을 경우
            answer[start][end] = -1
            break

        temp_cost, temp_end = heapq.heappop(heap[start])

        if temp_end not in answer[start]:       # 거처간 노드가 아니라면

            answer[start][temp_end] = temp_cost

            for y, dy in edges[temp_end].items():
                heapq.heappush(heap[start], (temp_cost + dy, y))

    print(answer[start][end])