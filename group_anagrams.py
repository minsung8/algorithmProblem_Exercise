def solution(list_s):

    temp_copy_s = list_s.copy()

    for i in range(len(temp_copy_s)):
        temp_copy_s[i] = sorted(temp_copy_s[i])

    answer_list = []
    used = []

    while temp_copy_s:

        temp_flag = True

        for i in range(len(temp_copy_s)):
            if temp_copy_s[i] not in used:
                start = temp_copy_s[i]
                temp_flag = False
                break

        if (temp_flag):
            break
        
        idx_list = []

        for i in range(len(temp_copy_s)):

            if start == temp_copy_s[i]:
                idx_list.append(i)

        answer_list.append(idx_list)
        used.append(start)

    answer_list  = answer_list[::-1]
    answer = []

    for i in range(len(answer_list)):
        temp = []
        for j in range(len(answer_list[i])):
            temp.append( list_s[ answer_list[i][j] ] )
        answer.append(temp)


    return answer[::-1]

print( solution(['eat', 'tea', 'ate', 'nat', 'bat', 'tan']) )