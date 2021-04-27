def solution(j, s):
    dic = {}

    for i in range(len(s)):

        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1

    answer = 0

    for i in range(len(j)):
        answer += dic[ j[i] ]
    return answer 


print(solution('ab', 'abbcccc'))