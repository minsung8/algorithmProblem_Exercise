def solution(sticker):

    for i in range(len(sticker) - 2):
        if sticker[i] + sticker[i + 2] > sticker[i - 1] + sticker[i + 1]:
            sticker[i + 1] = 0

    return sticker


print(solution([14, 6, 5, 11, 3, 9, 2, 10]	)) # 36
# print(solution([1, 3, 2, 5, 4])) # 8
print(solution([5, 1, 16, 17, 16] ))
