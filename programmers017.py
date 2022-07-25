
from re import A


def solution(a, b, g, s, w, t):

    # gold, silver, weight, time, current_time
    temp_list = []
    temp_time = 0

    for i in range(len(t)):
        temp_list.append([g[i], s[i], w[i], t[i], t[i]])

    while True:
        temp_list.sort(key=lambda x : x[-1])
        bucket = []
        temp_g, temp_s, temp_weight, temp_t, temp_current_time = temp_list.pop()
        idx_weight = temp_weight

        # gold를 캐야할 경우
        if a > 0 and temp_g > 0:
            
            # 무게가 필요한 금보다 많을 경우
            if a < temp_weight:
                bucket.append(a)
                temp_g -= a
                temp_weight -= a

            else:
                bucket.append(temp_weight)
                temp_g -= temp_weight
                temp_weight = 0
        else:
            bucket.append(0)
                
        # 금을 캐고 무게가 남았을경우
        if temp_weight != 0:
            bucket.append(temp_weight)
            temp_s -= temp_weight
            temp_weight = 0
        else:
            bucket.append(0)

        a -= bucket[0]
        b -= bucket[1]
        temp_time = temp_current_time
        temp_current_time += temp_t * 2

        temp_list.append([temp_g, temp_s, idx_weight, temp_t, temp_current_time])

        if a <= 0 and b <= 0:
            break

    return temp_time


print(solution(10, 10, [100], [100], [7], [10]))    # 50
# print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))    # 50

# 
