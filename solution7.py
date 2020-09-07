# 출처 : https://programmers.co.kr/learn/courses/30/lessons/64063

import sys
sys.setrecursionlimit(10000)

def find(n, dic):
    if n not in dic:
        dic[n] = n + 1
        return n

    answer = find(dic[n], dic)
    dic[n] = answer + 1
    return answer

def solution(k, room_number):
    answer = []
    dic = dict()
    for n in room_number:
        temp = find(n, dic)
        answer.append(temp)
    return answer