def solution(a, b, g, s, w, t):

    min_t = 0
    max_t = (10**9) * (10**5) * 4

    ## 이분탐색
    while True:
        gold = 0
        silver = 0
        total = 0
        temp_t = (min_t + max_t) // 2

        for i in range(len(g)):

            move_cnt = int(((temp_t / t[i]) + 1) / 2)

            gold += g[i] if (g[i] < move_cnt * w[i]) else move_cnt * w[i] 
            silver += s[i] if (s[i] < move_cnt * w[i]) else move_cnt * w[i]
            total += g[i] + s[i] if (g[i] + s[i] < move_cnt * w[i]) else move_cnt * w[i] 

        # 미션 클리어
        if gold >= a and silver >= b and total >= a + b:
            max_t = temp_t
        else:
            min_t = temp_t

        if min_t >= max_t - 1: 
            break

    return max_t

print(solution(10, 10, [100], [100], [7], [10]))    # 50
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))    # 50
