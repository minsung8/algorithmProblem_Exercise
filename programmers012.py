answer_list = []

def solution(sticker):

    global answer_list
    
    first_list = sticker[2:-1]
    second_list = sticker[3:]
    dfs(sticker[0], first_list)
    dfs(sticker[1], second_list)

    return answer_list

def dfs(sum, temp_list):


    if len(temp_list) == 2:
        answer_list.append(sum + max(temp_list))
    elif len(temp_list) == 3:
        answer_list.append(sum + max(temp_list[1], temp_list[0] + temp_list[2]))
    else:
        first_list = temp_list[2:]
        second_list = temp_list[3:]
        dfs(temp_list[0] + sum, first_list)
        dfs(temp_list[1] + sum, second_list)
    return



print(solution([14, 6, 5, 11, 3, 9, 2, 10]	)) # 36
print(solution([1, 3, 2, 5, 4])) # 8