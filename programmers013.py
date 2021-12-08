from collections import defaultdict

def solution(a, edges):
    answer = 0

    if sum(a) != 0:
        return -1 

    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    key_list = list(graph.keys())

    while key_list:
        key = key_list.pop(0)
        if len(graph[key]) == 1:
            temp_value = graph[key].pop(0)
            answer += abs(a[key])
            a[temp_value] += a[key]
            a[key] = 0
            graph[temp_value].remove(key)
        else:
            key_list.append(key)


    return graph, a, answer, edges, graph.keys()

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
