# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

from itertools import combinations
from collections import defaultdict
def solution(k, s):

    dic = defaultdict(list)
    answer = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if (s[i] + s[j]) % k != 0:
                dic[s[i]].append(s[j])
                dic[s[j]].append(s[i])
    
    for a in dic.keys():
        answer.append(check(dic[a], k))
        
    return answer


def check(s, k):

    dic = defaultdict(list)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if (s[i] + s[j]) % k != 0:
                dic[s[i]].append(s[j])
                dic[s[j]].append(s[i])
    
    print(len(dic.keys()))

    return 


print(solution(3, [1, 7, 2, 4]))    # 3
print(solution(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]))

