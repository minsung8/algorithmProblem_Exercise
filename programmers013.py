from collections import defaultdict
visited = 0
graph = defaultdict(list)
answer = 0
import sys
sys.setrecursionlimit(300000)

def solution(a, edges):
    global visited
    global graph
    global answer
    if sum(a) != 0:
        return -1

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [0] * len(a)

    dfs(0, a)

    return answer

def dfs(start, a):
    global visited
    global graph
    global answer
    key_list = graph[start]

    for v in key_list:
        if visited[v] == 0:
            dfs(v, a)
            answer += abs(a[v])

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
