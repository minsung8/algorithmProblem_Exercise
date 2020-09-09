# 출처 : https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):

    if sum(food_times) <= k: return -1
    temp_list = []
    for i in range(len(food_times)):
        temp_list.append([i, food_times[i]])
    temp_list = sorted(temp_list, key=lambda x: x[1])

    idx = 0
    total = 0
    temp = []
    if k > len(temp_list):
        while k > len(temp_list):
            temp = temp_list.pop(0)
            idx = temp[0]
            total = temp[1] - total

            if k - (total * (len(temp_list) + 1)) > 0:
                k -= total * (len(temp_list) + 1)
            else:
                if k > len(temp_list) + 1:
                    k -= (k // (len(temp_list) + 1)) * (len(temp_list) + 1)
                    return k + 1
                break

        temp_list = [temp] + temp_list
    return temp_list[k - 1][0] + 1




