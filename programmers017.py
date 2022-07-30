def solution(a, b, g, s, w, t):

    min_t = 0
    max_t = (10**9) * (10**5) * 4
    
    ## 이분탐색
    while True:
        temp_a = a
        temp_b = b

        temp_t = (min_t + max_t) // 2

        for i in range(len(g)):

            temp_cnt = int(((temp_t / t[i]) + 1) / 2)
            temp_w = w[i] * temp_cnt
            
            if temp_a > 0 and g[i] > 0 and temp_w > 0:
                temp = 0
                if temp_a > g[i]:
                    temp = min(g[i], temp_w)
                else:
                    temp = min(temp_a, temp_w)
                temp_w -= temp
                temp_a -= temp

            if temp_b > 0 and s[i] > 0 and temp_w > 0:
                temp = 0
                if temp_b > s[i]:
                    temp = min(s[i], temp_w)
                else:
                    temp = min(temp_b, temp_w)
                temp_w -= temp
                temp_b -= temp

        # 미션 클리어
        if temp_a <= 0 and temp_b <= 0:
            max_t = temp_t
        else:
            min_t = temp_t

        if min_t >= max_t - 1: 
            break

    return max_t

print(solution(10, 10, [100], [100], [7], [10]))    # 50
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))    # 50
