# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43162

visited = []

def solution(n, computers):

    global visited

    visited = [0] * n
    cnt = 0
    for i in range(len(computers)):

        if visited[i] == 0:
            visited[i] = 1
            dfs(i, computers)
            cnt += 1

    return cnt

def dfs(i, computers):

    global visited

    for j in range(len(computers[i])):

        if i != j and computers[i][j] == 1 and visited[j] == 0:
            visited[j] = 1
            dfs(j, computers)

    return