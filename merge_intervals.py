def solution(p_list):

    p_list.sort()
    temp_i = 0

    while temp_i < len(p_list) - 1:

        if p_list[temp_i][1] >= p_list[temp_i + 1][0]:
            p_list[temp_i] = [p_list[temp_i][0], p_list[temp_i + 1][1]]
            p_list.pop(temp_i + 1)
        
        temp_i += 1
    
    return p_list

print(solution([[2, 6], [1, 3], [8, 10], [15, 18]]))
