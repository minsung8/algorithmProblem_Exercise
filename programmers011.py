def solution(s):
    answer = []
    for temp_s in s:
        temp_answer = temp_s
        i = 0
        while i < len(temp_answer):
            if temp_s[i:i+3] == '110':
                front = temp_s[:i]
                if len(front) > 2:
                    for j in range(len(front) - 2):
                        if front[j:j+3] > '110':
                            temp_answer = front[:j] + '110' + front[j:len(front)] + temp_s[i+3:]
            i += 1
        answer.append(temp_answer)
    return answer

print(solution(["1110","100111100","0111111010"]))
