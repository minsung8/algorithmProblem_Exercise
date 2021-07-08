answer = []

def solution(s):
    
    if len(s) == 3:
        answer.append([cal(s)])
        return

    for i in range(len(s)):
        
        if s[i] in ['*', '-', '+']:
            temp_left = s[:i]
            temp_right = s[i + 1:]

            if len(temp_left) == 1:
                answer.append([temp_left])
            if len(temp_right) == 1:
                answer.append([temp_right])

            solution(temp_left)
            solution(temp_right)

    return answer

def cal(s):
    
    if s[1] == '+':
        return int(s[0]) + int(s[2])
    elif s[1] == '-':
        return int(s[0]) - int(s[2])
    elif s[1] == '*':
        return int(s[0]) * int(s[2])

#print(solution("2-1-1"))
print(solution("2*3-4*5"))
#print(solution("2*3-4*5+3*12"))
