# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

from itertools import combinations

def solution(k, s):

    start = len(s)
    answer = 0

    while start > 0:
        
        temp_list = combinations(s, start)
        flag = True
        
        for t in temp_list:
            temp_list2 = combinations(t, 2)
            for t2 in temp_list2:
                if sum(t2) % k == 0:
                    flag = False
                    break
            if flag:
                return start
            flag = True
        start -= 1

    return 0


print(solution(3, [1, 7, 2, 4]))    # 3
print(solution(7, [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]))
