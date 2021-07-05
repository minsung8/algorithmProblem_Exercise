def solution(gas, cost):

    if sum(gas) < sum(cost):
        return -1

    answer = 0
    temp = 0

    for i in range(len(gas)):
        
        if gas[i] + temp < cost[i]:
            answer = i + 1
            temp = 0
        else:
            temp += gas[i]
            temp -= cost[i]


    return answer
print(solution([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
