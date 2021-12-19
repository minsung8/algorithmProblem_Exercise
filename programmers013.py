from collections import defaultdict
visited = []
graph = defaultdict(list)
answer = 0
import sys
sys.setrecursionlimit(300000)

def solution(a, edges):

    if sum(a) != 0:
        return -1


    global visited, graph, answer
    visited = [0] * len(a)
    answer = 0 
    graph = defaultdict(list)

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    dfs(0, a)

    return answer

def dfs(start, a):
    global visited, graph, answer

    visited[start] = 1
    temp_answer = a[start]

    for value in graph[start]:
        if visited[value] == 0:
            temp_answer += dfs(value, a)

    answer += abs(temp_answer)

    return temp_answer


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
