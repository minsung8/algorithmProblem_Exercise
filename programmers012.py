def solution(sticker):

    answer = 0

    if len(sticker) < 4:
        return max(sticker)
    
    for i in range(len(sticker) - 1):
        if sticker[i] == 0:
            continue

        if i == len(sticker) - 2:
            if sticker[i] < sticker[i + 1]:
                sticker[i] = 0
            else:
                sticker[i + 1] = 0
            break
        
        if i == 0 and sticker[i] < sticker[i + 1] + sticker[-1]:
            sticker[i] = 0
        else:

            if sticker[i] + sticker[i + 2] < sticker[i + 1]:
                sticker[i] = 0
                sticker[i + 2] = 0
            else:
                sticker[i + 1] = 0

    return sum(sticker)



print(solution([14, 6, 5, 11, 3, 9, 2, 10]	)) # 36
print(solution([1, 3, 2, 5, 4])) # 8
print(solution([1, 100, 1, 1, 100] ))
