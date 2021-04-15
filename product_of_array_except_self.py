def solution(num):

    answer_list = [1]
    temp = 1
    for i in range(len(num)-1):
        temp *= num[i]
        answer_list.append(temp)

    num = sorted(num, reverse=True)

    answer_list2 = [1]
    temp = 1
    for i in range(len(num)-1):
        temp *= num[i]
        answer_list2.append(temp)
    
    answer = []

    for i in range(len(num)):
        temp = answer_list[i] * answer_list2[len(num) - i - 1]
        answer.append(temp)

    return answer

print( solution([1, 2, 3, 4]) )