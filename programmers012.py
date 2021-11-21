def solution(sticker):

    if len(sticker) < 4:
        return max(sticker)

    # 첫번째를 뜯을 경우
    first_case = sticker.copy()
    first_case[-1] = 0
    first_case[1] = sticker[0]
    for i in range(2, len(first_case)):
        first_case[i] = max(first_case[i - 1], first_case[i] + first_case[i - 2])
    
    # 그 외
    second_case = sticker.copy()
    second_case[0] = 0
    for i in range(2, len(second_case)):
        second_case[i] = max(second_case[i - 1], second_case[i] + second_case[i - 2])

    return max(first_case[-1], second_case[-1])

print(solution([14, 6, 5, 11, 3, 9, 2, 10]	)) # 36
print(solution([1, 3, 2, 5, 4])) # 8
print(solution([5, 1, 16, 17, 16] ))
print(solution([1, 100, 1, 1, 100]))