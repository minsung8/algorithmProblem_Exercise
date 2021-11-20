def solution(sticker):

    if len(sticker) < 4:
        return max(sticker)

    front_zero_sticker = sticker.copy()
    front_zero_sticker[0] = 0
    for i in range(2, len(front_zero_sticker)):
        front_zero_sticker[i] = max(front_zero_sticker[i - 1], front_zero_sticker[i - 2] + front_zero_sticker[i])

    back_zero_sticker = sticker.copy()
    back_zero_sticker[1] = 0
    back_zero_sticker[-1] = 0
    for i in range(2, len(back_zero_sticker)):
        back_zero_sticker[i] = max(back_zero_sticker[i - 1], back_zero_sticker[i - 2] + back_zero_sticker[i])

    return max(front_zero_sticker[-1], back_zero_sticker[-1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]	)) # 36
print(solution([1, 3, 2, 5, 4])) # 8
print(solution([5, 1, 16, 17, 16] ))
print(solution([1, 100, 1, 1, 100]))