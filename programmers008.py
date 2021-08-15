from heapq import heappop, heappush

def solution(n, s, a, b, fares):

    route = {}
    for i in range(1, n + 1):
        route[i] = {}

    for i in range(len(fares)):
        route[fares[i][0]][fares[i][1]] = fares[i][2] 
        route[fares[i][1]][fares[i][0]] = fares[i][2]

    answer = float('inf')

    for i in range(1, n + 1):
        answer = min(answer, find(s, i, route) + find(i, a, route) + find(i, b, route))
    return answer

def find(start, end, route):

    answer_list = [float('inf') for i in range(len(route.keys()) + 1)]
    answer_list[start] = 0

    temp_list = [[0, start]]

    while temp_list:
        temp_cost, temp_start = heappop(temp_list)

        if temp_cost > answer_list[temp_start]:
            continue

        for key in route[temp_start].keys():
            
            if answer_list[key] > route[temp_start][key] + temp_cost:
                answer_list[key] = route[temp_start][key] + temp_cost
                heappush(temp_list, [route[temp_start][key] + temp_cost, key])
    
    return answer_list[end]

    


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
#print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
#print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))