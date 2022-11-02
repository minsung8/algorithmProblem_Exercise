# https://school.programmers.co.kr/learn/courses/30/lessons/92342


def solution(n, info):

    score_list = []
    j = 0
    for i in range(10, -1, -1):
        if info[j] != 0:
            score_list.append([i / info[j], info[j] + 1, j])
        else:
            score_list.append([0, info[j] + 1, j])
        j += 1
    
    # 우선순위, 횟수, 인덱스 
    score_list = sorted(score_list, key=lambda x : (x[0], -x[1]), reverse=True)
    answer = [0] * len(info)

    for i in range(len(score_list)):

        if score_list[i][1] <= n:
            n -= score_list[i][1]
            answer[score_list[i][2]] = score_list[i][1]

        if n <= 0: break
    
    a, b = 0, 0

    for i in range(len(info)):
        if info[i] != 0 or answer[i] != 0:
            if info[i] >= answer[i]:
                a += 10 - i
            else:
                b += 10 - i
        print(a, b)

    if a >= b: return [-1]

    return answer



print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) # 	[0,2,2,0,1,0,0,0,0,0,0]
print(solution(	1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
