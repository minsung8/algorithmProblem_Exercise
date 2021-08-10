cost_dic = {}
answer_dic = {}

def solution(n, s, a, b, fares):

    global cost_dic, answer_dic

    answer = float('inf')
    
    for i in range(len(fares)):
        if fares[i][0] not in cost_dic.keys():
            cost_dic[fares[i][0]] = {fares[i][1]: fares[i][2]}
        else:
            cost_dic[fares[i][0]][fares[i][1]] = fares[i][2]

        if fares[i][1] not in cost_dic.keys():
            cost_dic[fares[i][1]] = {fares[i][0]: fares[i][2]}
        else:
            cost_dic[fares[i][1]][fares[i][0]] = fares[i][2]

    for i in range(1, n+1):

        temp_start_cost = find(s, i, fares)
        if temp_start_cost != float('inf'):
            result = temp_start_cost + find(i, a, fares) + find(i, b, fares)
            print(result)
            if result < answer:
                answer = result

    return answer

def find(start, end, fares):

    global cost_dic, answer_dic

    if start in answer_dic.keys() and end in answer_dic[start].keys():
        return answer_dic[start][end]

    if start == end:
        return 0

    answer = float('inf')
    temp_list = [[start, 0]]
    visited = []
    while temp_list:
        temp_start, temp_cost = temp_list.pop(0)
        visited.append(temp_start)

        if temp_cost < answer:
            for key in cost_dic[temp_start]:
                if key in visited:
                    continue
                
                if key == end and temp_cost + cost_dic[temp_start][key] < answer:
                    answer = temp_cost + cost_dic[temp_start][key]
                    
                elif temp_cost + cost_dic[temp_start][key] < answer:
                    temp_list.append([key, temp_cost + cost_dic[temp_start][key]])

    if start in answer_dic.keys():
        answer_dic[start][end] = answer
    else:
        answer_dic[start] = {end:answer}

    return answer
                
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))