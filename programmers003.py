# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    for i in range(1, n + 1):
        answer.append([0] * i)
    x = 0
    y = -1
    start = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3  == 0:
                y += 1
                answer[y][x] = start 
                start += 1
            
            elif i % 3 == 1:
                x += 1
                answer[y][x] = start
                start += 1
            
            elif i % 3 == 2:
                x -= 1
                y -= 1
                answer[y][x] = start
                start += 1
    result = []
    for i in range(len(answer)):
        result += answer[i]
    return result

print(solution(5))
