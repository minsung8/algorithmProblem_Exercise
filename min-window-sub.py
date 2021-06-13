def solution(s, t):

    answer = s
    i = 0
    j = len(s) - 1

    while i < len(s):

        if s[i] not in t:
            i += 1


        elif s[j] in t and s[j] not in s[i:j]:
            
            if len(answer) > len(s[i:j+1]):
                answer = s[i:j+1]
            i += 1
            j = len(s) - 1

            if s[i] in t and s[i] not in s[i+1:]:
                break
            
        else:
            j -= 1

        if j == i:
            i += 1
            j = len(s) - 1

    return answer
        
 
print(solution("ADOBECABCODEBANC", "ABC"))
