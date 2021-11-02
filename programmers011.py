def solution(s):

    answer_list = []

    for temp_s in s:        #1110
        temp_list = list(temp_s)
        for i in range(len(temp_list)):
            flag = False

            if "".join(temp_list[i:i+3]) == '110':
                front = temp_list[:i]
                back = temp_list[i+3:]
                if len(front) < 3:
                    if "".join(front) < '110':
                        temp_list = ['1', '1', '0'] + front + back
                        continue
                else:
                    for j in range(len(front) - 2):
                        if "".join(front[j:j+3]) > '110':
                            temp_list = front[:j] + ['1','1','0'] + front[j+3:] + front[j:j+3] + back
                            flag = True
                            break
                if flag:
                    continue
                
                if len(back) < 3:
                    if "".join(back) < '110':
                        temp_list = front + back + ['1', '1', '0']
                        continue
                else:
                    for j in range(len(back) - 2):
                        if "".join(back[j:j+3]) < '110':
                            temp_list = front + back[j:j+3] + back[:j] + ['1','1','0'] + back[j+3:]
                            break
                
        answer_list.append("".join(temp_list))
    return answer_list
    
print(solution(["1110","100111100","0111111010"]		))
# ["1101","100110110","0110110111"]
