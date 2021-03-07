# https://programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):

    answer_list = []

    idx = 0

    temp = 0

    last_value = sticker.pop(-1)

    while idx < len(sticker):

        temp += sticker[idx]

        if idx + 4 < len(sticker) and (sticker[idx + 3] > sticker[idx + 2] + sticker[idx + 4]):
            idx += 3
        
        elif idx + 3 < len(sticker) and sticker[idx + 3] > sticker[idx + 2]:
            idx += 3
        
        else:
            idx += 2
    
    answer_list.append(temp)
    sticker += [last_value]

    idx = 1

    temp = 0

    while idx < len(sticker):

        temp += sticker[idx]

        if idx + 4 < len(sticker) and (sticker[idx + 3] > sticker[idx + 2] + sticker[idx + 4]):
            idx += 3
        
        elif idx + 3 < len(sticker) and sticker[idx + 3] > sticker[idx + 2]:
            idx += 3
        
        else:
            idx += 2
    
    answer_list.append(temp)
        
    return max(answer_list)

## temp = 25 idx = 3 / temp = 34 idx = 5

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
