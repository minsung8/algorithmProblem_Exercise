def solution(s):

    answer = []

    for temp_s in s: 
        temp_list = []
        temp_cnt = 0
        
        for s in temp_s:
            if s == '0':
                if temp_list[-2:] == ['1', '1']:
                    temp_list.pop(-1)
                    temp_list.pop(-1)
                    temp_cnt += 1
                else:
                    temp_list.append(s)
            else:
                temp_list.append(s)
        if '0' not in temp_list:
            temp_answer = ('110' * temp_cnt) + "".join(temp_list)
        else:
            j = len(temp_list) - 1
            while j > -1:
                if temp_list[j] == '0':
                    temp_answer = "".join(temp_list[:j + 1]) + ('110' * temp_cnt) + "".join(temp_list[j+1:])
                    break
                j -= 1
        
        answer.append(temp_answer)
    return answer

#print(solution(["1110"]))
print(solution(["1110","100111100","0111111010"]))
# ["1101","100110110","0110110111"]
