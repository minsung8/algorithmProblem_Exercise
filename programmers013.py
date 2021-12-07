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
    
    while end_node_list:
        temp_key = end_node_list.pop(0)
        if graph[temp_key]:
            temp_value = graph[temp_key].pop(0)

            a[temp_value] += a[temp_key]
            answer += abs(a[temp_key])
            a[temp_key] = 0

            for i in range(len(graph[temp_value])):
                if graph[temp_value][i] == temp_key:
                    graph[temp_value].pop(i)
                    break
            
            if len(graph[temp_value]) == 1:
                end_node_list.append(temp_value)

        else:
            continue

    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
#print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
