def solution(n, s, a, b, fares):

    cost_dic = {}
    answer = []

    for i in range(len(fares)):
        if fares[i][0] not in cost_dic:
            cost_dic[fares[i][0]] = {fares[i][1]: fares[i][2]}
        else:
            cost_dic[fares[i][0]][fares[i][1]] = fares[i][2]

        if fares[i][1] not in cost_dic:
            cost_dic[fares[i][1]] = {fares[i][0]: fares[i][2]}
        else:
            cost_dic[fares[i][1]][fares[i][0]] = fares[i][2]

    # for i in range(1, n + 1):

    #     temp = dfs(s, i, cost_dic)

    #     if len(temp) > 0:
    #         start_cost = min(temp)
    #         answer.append( start_cost + min(dfs(i, a, cost_dic)) + min(dfs(i, b, cost_dic)))
    return answer


def dfs(start, end, cost_dic):

    if start == end:
        return [0]

    answer = []
    temp_list = [[start, 0]]
    visited = []
    while temp_list:
        # 4
        temp_start, temp_cost = temp_list.pop(0)
        visited.append(temp_start)
        #[1, 6, 2]
        for i in range(len(cost_dic[temp_start].keys())):

            if cost_dic[temp_start][i]:
                answer.append(temp_cost + cost_dic[temp_start][1][i])
            else:
                if cost_dic[temp_start][0][i] not in visited:
                    temp_list.append([cost_dic[temp_start][0][i], temp_cost + cost_dic[temp_start][1][i]])

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
#print(dfs(4, 1, 0, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]], []))
#print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
