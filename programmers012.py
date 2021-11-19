def solution(sticker):

    temp_list = sticker.copy()

    for i in range(len(sticker) - 1):
        
        if sticker[i] < sticker[i - 1] + sticker[i + 1]:
            temp_list[i] = 0
        else:
            temp_list[i - 1] = 0
            temp_list[i + 1] = 0

    return temp_list


print(solution([14, 6, 5, 11, 3, 9, 2, 10]	)) # 36
# print(solution([1, 3, 2, 5, 4])) # 8
print(solution([5, 1, 16, 17, 16] ))
