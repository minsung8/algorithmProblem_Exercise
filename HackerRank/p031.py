# https://school.programmers.co.kr/learn/courses/30/lessons/92342


def solution(n, info):
    answer = []

    score_list = []
    j = 0
    for i in range(10, -1, -1):
        if info[j] != 0:
            score_list.append([i / info[j], info[j] + 1, j])
        else:
            score_list.append([0, info[j] + 1, j])
        j += 1
    
    score_list = sorted(score_list, key=lambda x : (x[0], -x[1]), reverse=True)

    return score_list



print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) # 	[0,2,2,0,1,0,0,0,0,0,0]


# 