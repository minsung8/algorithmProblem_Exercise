
from django.dispatch import receiver


def solution(n, info):
    score_list = []

    for i in range(len(info)):
        score_list.append([ i, ( 2 * (10 - i) / (info[i] + 1) ) + (10 - i)])
    

    return sorted(score_list, key=lambda x : (x[1], -x[0]), reverse=True)


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))     # res = [0,2,2,0,1,0,0,0,0,0,0]

# 3 - > 10 = 3.3
# 2 -> 9 = 4.5
# 2 -> 8 = 4
# 1 -> 7 = 7  
# 2 -> 6 = 3
# [3.3333333333333335, 4.5, 4.0, 3.5, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0, 0.0]


# [0 -10], [3, 10] => 3,10 = 13.3
# [0 -9], [2, 9] => 2,18 = 18
# [0 -8], [2, 8] => 2,16 = 16
# [0, -7], [2, 7] => 2,7 = 14
# [0, -6], [1, 6] => 1, 6 = 12
# [0, -5], [1, 5] => 1, 5 = 15
