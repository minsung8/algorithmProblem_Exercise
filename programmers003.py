# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    for i in range(1, n + 1):
        temp = [0] * i
        answer.append(temp)

    return answer




print(solution(4))