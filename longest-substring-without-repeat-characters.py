def solution(s):
    
    dic = {}
    answer = 0

    for i in range(len(s)):

        if s[i] not in dic:
            dic[s[i]] = 1
            answer += 1

    return answer


print(solution('abcabcbb'))