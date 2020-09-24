# 출처 : https://programmers.co.kr/learn/courses/30/lessons/49191

from collections import defaultdict

def solution(n, results):

    answer = 0
    win_dic = defaultdict(list)
    lose_dic = defaultdict(list)

    for i in results:
        win_dic[i[0]].append(i[1])
        lose_dic[i[1]].append(i[0])

    for i in range(1, n + 1):
        visited = [1] * (n + 1)
        visited[i] = 1
        win_cnt = cnt(i, win_dic)
        lose_cnt = cnt(i, lose_dic)

        if win_cnt + lose_cnt == n - 1:
            answer += 1
    return answer

def cnt(n, temp_dic):
    visited = [0] * 101
    answer = []
    dic = temp_dic[n].copy()
    while dic:
        temp = dic.pop(0)
        answer.append(temp)
        for i in temp_dic[temp]:
            if visited[i] == 0:
                visited[i] = 1
                dic.append(i)
    return len(set(answer))