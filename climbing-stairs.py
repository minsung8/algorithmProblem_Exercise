def solution(stairs):
    answer = 0
    a = 1
    b = 2
    for i in range(stairs-2):
        answer = a + b

        temp = b
        b = answer
        a = temp

    return answer

print(solution(5))