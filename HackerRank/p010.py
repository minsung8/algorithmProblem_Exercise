# https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true

from collections import defaultdict

def solution(n, k, r_q, c_q, obstacles):

    dic = defaultdict(boolean)

    for ob in obstacles:  
        dic[f"{ob[0]},{ob[1]}"] = 1

    answer = 0

    answer += move(1, 0, r_q, c_q, dic, n)
    answer += move(-1, 0, r_q, c_q, dic, n)
    answer += move(0, 1, r_q, c_q, dic, n)
    answer += move(0, -1, r_q, c_q, dic, n)
    answer += move(1, 1, r_q, c_q, dic, n)
    answer += move(-1, 1, r_q, c_q, dic, n)
    answer += move(1, -1, r_q, c_q, dic, n)
    answer += move(-1, -1, r_q, c_q, dic, n)

    return answer

def move(x, y, start_x, start_y, dic, n):

    answer = 0
    
    while True:

        start_x += x
        start_y += y

        if (n < start_x or n < start_y) or (start_x < 1 or start_y < 1):
            break
        
        if dic[f"{start_x},{start_y}"] == 1:
            break

        else:
            answer += 1

    return answer

# 길이, 장애물 수, 퀸의 좌표, 장애물 좌표
print(solution(4, 0, 4, 4, []))     # 9
print(solution(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))     # 10
print(solution(1, 0, 1, 1, []))     # 0

print(solution(100000, 0, 4187, 5068, []))
