def solution(a, b, g, s, w, t):

    start = 0
    end = (10**9) * (10**5) * 4

    while True:

        mid = int((start + end) / 2)
        gold = 0    # 캘 수 있는 금
        silver = 0  # 캘 수 있는 은
        total = 0   # 캘 수  있는 금  + 은

        for i in range(len(g)):
            
            move_cnt = int((mid / t[i] + 1)/ 2)
            
            gold += g[i] if g[i] < move_cnt * w[i] else move_cnt * w[i]
            silver += s[i] if s[i] < move_cnt * w[i] else move_cnt * w[i]
            total += g[i] + s[i] if (g[i] + s[i] < move_cnt * w[i]) else move_cnt * w[i] 
        
        if gold >= a and silver >= b and total >= a + b:
            end = mid
        else:
            start = mid
        
        if start >= end - 1: 
            break

    return end

print(solution(10, 10, [100], [100], [7], [10]))    # 50
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))    # 50

# 50 = (2n - 1) * t 
# (50 / t + 1)/ 2 = 2n