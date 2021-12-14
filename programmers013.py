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

    for key in graph.keys():
        if len(graph[key]) == 1 and visited[key] == 0:
            dfs(key, graph, a, 0)
        
    return answer

def dfs(key, graph, a, temp_answer):
    global answer, visited

    
    
    
    answer += abs(temp_answer)
    return

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
#print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
