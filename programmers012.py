def solution(sticker):

    answer = 0

    if len(sticker) < 4:
        return max(sticker)
    
    for i in range(1, len(sticker)):
        if i == 1:
            if sticker[i] + sticker[-1] < sticker[i - 1]:
                sticker[i] = sticker[i - 1]
            else:
                sticker[i - 1] = 0
            
        else:
            if sticker[i] + sticker[i - 2] < sticker[i - 1]:
                sticker[i] = sticker[i - 1]
            else:
                sticker[i] += sticker[i - 2]
    return sticker[-1]


print(solution([14, 6, 5, 11, 3, 9, 2, 10]	)) # 36
print(solution([1, 3, 2, 5, 4])) # 8
print(solution([1, 16, 1, 17, 16] ))
