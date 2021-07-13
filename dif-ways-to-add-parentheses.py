result = []

def solution(s):

    dfs(s)

    return result

def dfs(s):
    if s.isnumeric():
        return s

    global result

    for i in range(len(s)):
        if s[i] in '*-+':
            print(s[:i], s[i], s[i+1:], result)
            print(eval(dfs(s[:i]) + s[i] + dfs(s[i+1:])) )
            result.append( eval(dfs(s[:i]) + s[i] + dfs(s[i+1:])) )
            print(result)

    return




#print(solution('3-4'))
#print(solution("2-1-1"))
print(solution("2*3-4*5"))
#print(solution("2*3-4*5+3*12"))
