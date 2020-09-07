# 출처 : https://programmers.co.kr/learn/courses/30/lessons/64063

from collections import defaultdict

def solution(k, room_number):
    pos = {}
    visit = defaultdict(int)
    answer = [0] * (len(room_number) + 1)
    for i in range(1, len(room_number) + 1):
        if answer[i] == 0 and visit[room_number[i - 1]] == 0:
            answer[i] = room_number[i - 1]
            visit[room_number[i - 1]] = 1
        else:
            temp = room_number[i - 1]
            while True:
                temp += 1
                if visit[temp] == 0:
                    answer[i] = temp
                    visit[temp] = 1
                    break
    return answer[1:]

print(solution(10, [1, 3, 4, 1, 3, 1]))