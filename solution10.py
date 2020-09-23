# 출처 : https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import defaultdict

def solution(n, edge):

    dic = defaultdict(list)
    visited = [1, 1] + [0] * (n - 1)
    answer = [[1]]
    for i in edge:
        dic[i[0]].append(i[1])
        dic[i[1]].append(i[0])

    temp = dic[1]
    for i in temp:
        visited[i] = 1

    while temp:
        answer.append(temp)
        temp3 = []
        for i in temp:
            for j in dic[i]:
                if visited[j] == 0 and j not in temp and j not in temp3:
                    visited[j] = 1
                    temp3.append(j)
        temp = temp3
    return len(answer[-1])
