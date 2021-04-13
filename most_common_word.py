import re

def solution(paragraph, banned):
    temp_s = re.sub(r'[^\w]', ' ', paragraph)
    temp_s = temp_s.split(' ')

    answer_dic = {}

    for i in range(len(temp_s)):
        if temp_s[i] not in banned:

            if temp_s[i] not in answer_dic.keys():
                answer_dic[temp_s[i]] = 1
            else:
                answer_dic[temp_s[i]] += 1
    answer = sorted(answer_dic.items(), key=lambda x : x[1] )
    return answer[-1][0]


print( solution('bob hit a ball, the hit ball flew far after it was hit', ['hit']) )