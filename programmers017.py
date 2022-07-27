from turtle import Turtle


def solution(a, b, g, s, w, t):

    max_t =  (2 * 10 ** 9) * 2 * (10 ** 5) + 1

    # test
    max_t = 100

    ## 이분탐색
    while True:

        temp_g = 0
        temp_s = 0
        
        for i in range(len(g)):
            temp_cnt = int((max_t + t[i]) / (2 * t[i]))
            print(temp_cnt)

        break

    return 

print(solution(10, 10, [100], [100], [7], [10]))    # 50
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))    # 50

# 2k(n - 1) +k = 50
# 2kn - 2k + k = 50
# (50 + k) = 2kn
