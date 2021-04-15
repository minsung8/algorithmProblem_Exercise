def solution(num):

    answer = 0
    
    for i in range(len(num)):

        if i % 2 == 0:
            answer += num[i]

    return answer


print( solution([1, 4, 3, 2]) )