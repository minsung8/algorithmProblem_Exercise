def solution(s):

    answer = []

    for temp_s in s:

        i = 0
        temp_list = list(temp_s)

        while i < len(temp_list):
            if i > 1 and temp_list[i - 2:i + 1] == ['1', '1', '1']:
                temp_list2 = temp_list[i - 1:]
                if '110' not in "".join(temp_list2):
                    break
                change_idx = "".join(temp_list2).index('110') + 1 + i
                temp_list[i] = '0'
                temp_list[change_idx] = '1'
                
            i += 1

        answer.append("".join(temp_list))

    return answer

#print(solution(["1110"]))
print(solution(["1110","100111100","0111111010"]))
# ["1101","100110110","0110110111"]
