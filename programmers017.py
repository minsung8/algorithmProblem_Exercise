def solution(a, b, g, s, w, t):

    start = 0
    end = (10**9) * (10**5) * 4

    while True:
        mid = int((start + end) / 2)

        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):

            move_cnt = int((mid / t[i] + 1)/ 2)
            gold += min(move_cnt * w[i], g[i])
            silver += min(move_cnt * w[i], s[i])
            total += min(g[i] + s[i], move_cnt * w[i])

        if gold >= a and silver >= b and total >= a + b:
            end = mid
        else:
            start = mid
        
        if start >= end - 1: 
            break

    return end

print(solution(10, 10, [100], [100], [7], [10]))    # 50
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))    # 50
