def solution(ads):

    answer = 0
    end_time = 0
    ads = sorted(ads, key=lambda x : (x[0] * x[1], -x[1]))
    end_time += ads[0][0] + 5
    ads.pop(0)
    while ads:
        temp_ads = []
        temp_i = 0
        for i in range(len(ads)):
            if end_time >= ads[i][0]:
                temp_ads.append(ads[i]) 
                temp_i = i
        print(temp_ads)
        temp_ads = sorted(temp_ads, key=lambda x : -x[1])
        answer += (end_time - temp_ads[0][0]) * temp_ads[0][1]
        end_time += 5
        ads.pop(temp_i)

    return answer


print(solution([[1, 3], [3, 2], [5, 4]]))
print(solution([[0, 1], [0, 2], [6, 3], [8, 4]]))
print(solution([[0, 3], [5, 4]]))
print(solution([[5, 2], [2, 2], [6, 3], [9, 2]]))