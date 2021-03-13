# https://programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):

    if len(sticker) < 4:
        return max(sticker)

    answer_list = []

    # 첫번째 시작
    first_sticker = sticker[:-1]
    idx = 0
    temp_answer = 0
    while idx < len(first_sticker):
        temp_answer += first_sticker[idx]
        if idx + 3 < len(first_sticker) and first_sticker[idx + 3] > first_sticker[idx + 2]:
            idx += 3
        else:
            idx += 2
    answer_list.append(temp_answer)

    # 두번째 시작
    sec_sticker = sticker[1:]
    idx = 0
    temp_answer = 0
    while idx < len(sec_sticker):
        temp_answer += sec_sticker[idx]

        if idx + 3 < len(sec_sticker) and sec_sticker[idx + 3] > sec_sticker[idx + 2]:
            idx += 3
        else:
            idx += 2
    answer_list.append(temp_answer)

    # 세번째 시작
    third_sticker = sticker[2:]
    idx = 0
    temp_answer = 0
    while idx < len(third_sticker):
        temp_answer += third_sticker[idx]

        if idx + 3 < len(third_sticker) and third_sticker[idx + 3] > third_sticker[idx + 2]:
            idx += 3
        else:
            idx += 2
    answer_list.append(temp_answer)

    # 그 중 가장 큰 값
    return max(answer_list)

print(solution([14, 6, 5, 7, 3, 9, 2, 10, 8, 4, 22, 4, 4, 8, 100, 1]))
#print(solution([1, 3, 2, 5, 4]))
#print(solution([1, 1, 1, 1, 1]))

