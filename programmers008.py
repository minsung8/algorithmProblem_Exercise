from heapq import heappop, heappush

def solution(n, s, a, b, fares):

    cost = {}

    for i in range(1, n + 1):
        cost[i] = {}

    for i in range(len(fares)):

        cost[fares[i][0]][fares[i][1]] = fares[i][2]
        cost[fares[i][1]][fares[i][0]] = fares[i][2]

    answer = float('inf')

    for i in range(1, n + 1):
        

        answer = min(answer, find(i, s, cost) + find(i, a, cost) + find(i, b, cost))
            
    return answer


def find(start, end, cost):
    
    if start == end:
        return 0
    
    answer = float('inf')
    temp = [[0, start]]
    visited = []

    while temp:
        temp_cost, temp_start = heappop(temp)
        visited.append(temp_start)
        if temp_cost > answer:
            continue

        for key in cost[temp_start].keys():
            if key == end and answer > temp_cost + cost[temp_start][key] and key not in visited:
                answer = temp_cost + cost[temp_start][key]
            elif key != end and answer > temp_cost + cost[temp_start][key] and key not in visited:
                heappush(temp, [temp_cost + temp_cost + cost[temp_start][key], key])

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))