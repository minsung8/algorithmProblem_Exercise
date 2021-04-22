def solution(s):
    set_s = sorted(list(set(s)))

    answer = ''
    for i in range(len(set_s)):
        answer += set_s[i]
    return answer

print(solution('bcabc'))
print(solution('cbacdcbc'))