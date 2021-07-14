
def solution(s):

    answer = dfs(s)

    for i in range(len(answer)):
        answer[i] = int(answer[i])
    return answer

def dfs(s):

    if s.isnumeric():
        return [s]
    answer = []

    for i in range(len(s)):
        left_list = []
        right_list = []
        if s[i] in '*-+':
            left_list = dfs(s[:i])
            right_list = dfs(s[i+1:])
            for x in range(len(left_list)):
                for y in range(len(right_list)):
                    answer.append( str(eval(left_list[x] + s[i] + right_list[y])))

    return answer


print(solution('3-4'))
print(solution("2-1-1"))
print(solution("2*3-4*5"))
print(solution("2*3-4*5+3*12"))
