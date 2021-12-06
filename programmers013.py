from collections import defaultdict

def solution(a, edges):
    answer = 0

    if sum(a) != 0:
        return -1 

    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    end_node_list = []

    for key in graph.keys():
        if len(graph[key]) == 1:
            end_node_list.append(key)
    print(end_node_list)
    while end_node_list:
        temp = end_node_list.pop(0)
        if not graph[temp]:
            continue
        next_node = graph[temp][0]
        a[next_node] += a[temp]
        answer += abs(a[temp])

        graph[next_node].remove(temp)

        if len(graph[next_node]) == 1:
            end_node_list.append(next_node)

    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
#print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
