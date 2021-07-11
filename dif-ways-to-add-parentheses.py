answer = []

def solution(s):
    print(s)
        
    if cnt(s) == 1:
        return cal(s)

    if s.isnumeric():
        return s

    for i in range(1, len(s)):
        if s[i] in ['*', '-', '+']:
            temp_left = s[:i]
            temp_right = s[i + 1:]

            answer.append(int( solution( solution(temp_left) + s[i] + solution(temp_right) ) ))

    return answer

def cal(s):
    
    if s[1] == '+':
        return str( int(s[0]) + int(s[2]) )
    elif s[1] == '-':
        return str( int(s[0]) - int(s[2]) )
    elif s[1] == '*':
        return str( int(s[0]) * int(s[2]) )

def cnt(s):
    cnt = 0
    for i in range(1, len(s)):
        if s[i] in ['*', '-', '+']:
            cnt += 1
    return cnt

#print(solution("2-1-1"))
print(solution("2*3-4*5"))
#print(solution("2*3-4*5+3*12"))
