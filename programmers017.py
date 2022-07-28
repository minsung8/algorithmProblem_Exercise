def solution(a, b, g, s, w, t):

    max_t =  (2 * 10 ** 9) * 2 * (10 ** 5) + 1

    ## 이분탐색
    while True:
        temp_a = a
        temp_b = b

        for i in range(len(g)):

            temp_cnt = int(((max_t / t[i]) + 1) / 2)
            temp_w = w[i] * temp_cnt

            if g[i] > 0 and temp_a > 0 and temp_a > g[i]:
                if temp_w < g[i]:
                    temp_a -= temp_w
                    temp_w = 0
                else:
                    temp_a -= g[i]
                    temp_w -= g[i]
            elif g[i] > 0 and temp_a > 0 and temp_a <= g[i]:
                if temp_w < temp_a:
                    temp_a -= temp_w
                    temp_w = 0
                else:
                    temp_w -= temp_a
                    temp_a = 0

            if s[i] > 0 and temp_b > 0 and temp_w > 0 and temp_b > s[i]:
                if temp_w < s[i]:
                    temp_b -= temp_w
                else:
                    temp_b -= s[i]
            elif s[i] > 0 and temp_b > 0 and  temp_w > 0 and temp_b <= s[i]:
                if temp_w < temp_b:
                    temp_b -= temp_w
                else:
                    temp_b = 0

        if temp_a > 0 or temp_b > 0:
            break

        max_t = int(max_t / 2)

    # 실패한 가장 큰 시간 : max_t
    

    return max_t

print(solution(10, 10, [100], [100], [7], [10]))    # 50
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))    # 50

# 50 100
# 1000 => 50 / 100
# int(((max_t / 10) + 1) / 2)
# 

# 2  = 1
# 6  = 2
# 10 = 3
# cnt = max_T