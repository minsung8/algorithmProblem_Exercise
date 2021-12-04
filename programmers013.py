from collections import defaultdict

def solution(a, edges):

    if sum(a) != 0:
        return -1 

    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    len_graph = {}

    for key in graph.keys():
        len_graph[key] = len(graph[key])


    return graph, len_graph



print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
#print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
