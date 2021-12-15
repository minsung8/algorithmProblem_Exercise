from collections import defaultdict
visited = []
answer = 0
import sys
sys.setrecursionlimit(300000)

def solution(a, edges):

    global answer, visited

    visited = [0] * len(a)

    if sum(a) != 0:
        return -1

    graph = defaultdict(list)
    
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    dfs(0, graph, a)
        
    return answer

def dfs(key, graph, a):

    global answer, visited

    now = a[key]
    visited[key] = 1

    for value in graph[key]:
        if visited[value] == 0: ## 방문하지 않았으면 
            now += dfs(value, graph, a)
    
    answer += abs(now)

    return now

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
#print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
