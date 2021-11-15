def solution(sticker):

    answer = 0

    if len(sticker) < 4:
        return max(sticker)

    if sticker[0] < sticker[1] + sticker[-1]:
        sticker[0] = 0
        i = 1
    else:
        sticker[1] = 0
        sticker[-1] = 0
        i = 2
    
    while i < len(sticker):
        pass
    print(sticker)



print(solution([14, 6, 5, 11, 3, 9, 2, 10]	)) # 36
#print(solution([1, 3, 2, 5, 4])) # 8
print(solution([5, 1, 16, 17, 16] ))