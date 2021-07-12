answer = []

def solution(s):
    
    for i in range(len(s)):
        
        if s[i] in ['*', '-', '+']:
            left = s[:i]
            right = s[i + 1:]
        
            left_list = dfs(left)
            right_list = dfs(right)
            print(left_list, right_list)

    return answer


def dfs(s):

    answer = []

    if s.isnumeric():
        return [s]

    for i in range(len(s)):
        if s[i] in '*-+':
            answer.append(eval( str(eval(s[i:])) + s[i] + str(eval(s[i+1:])) ))

    return answer


print(solution('3-4'))
print(solution("2-1-1"))
#print(solution("2*3-4*5"))
#print(solution("2*3-4*5+3*12"))
