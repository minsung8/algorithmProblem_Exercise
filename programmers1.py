## Problem : https://programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    
    answer = 2

    list_a = [0] * len(a)

    front_value = a[0]

    for i in range(1, len(a) - 1):

        if front_value > a[i]:
            list_a[i] = 1
            front_value = a[i]

    back_value = a[-1]
    
    for i in range(len(a)-1, -1, -1):

        if back_value > a[i]:
            list_a[i] = 1
            back_value = a[i]

    return list_a.count(1) + 2
    

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
print(solution([9,-1,-5]))

## 1 0 0 0 0 1 0 0 0 1
##             1 1 1 1
