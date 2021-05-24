def solution(n_list):

    temp_list = sorted(n_list, key=lambda x:  int(str(x)[0]), reverse=True)

    temp_idx = 0
    while temp_idx < len(temp_list) - 1:
        
        if str(temp_list[temp_idx])[0] == str(temp_list[temp_idx + 1])[0]:

            if len(str(temp_list[temp_idx])) == len(str(temp_list[temp_idx + 1])) and temp_list[temp_idx] < temp_list[temp_idx + 1]:
                temp = temp_list[temp_idx]
                temp_list[temp_idx] = temp_list[temp_idx + 1]
                temp_list[temp_idx + 1] = temp
                temp_idx += 1
            else:
                temp2 = str(temp_list[temp_idx])[0] * len(str(temp_list[temp_idx + 1])[0])

                if int(temp2) < temp_list[temp_idx + 1]:
                    temp = temp_list[temp_idx]
                    temp_list[temp_idx] = temp_list[temp_idx + 1]
                    temp_list[temp_idx + 1] = temp
                    temp_idx += 1

        else:
            temp_idx += 1
                

    return temp_list

print(solution([3, 30, 34, 5, 9]))