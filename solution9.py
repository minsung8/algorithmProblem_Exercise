# 출처 : https://programmers.co.kr/learn/courses/30/lessons/43162

visited = []
def solution(n, computers):

    global visited
    visited = [0] * n

    cnt = 0
    for i in range(len(computers)):
        if visited[i] == 0:
            dfs(computers[i], i, computers)
            cnt += 1

    return cnt

def dfs(temp_list, k, computers):

    for i in range(len(temp_list)):

        if k != i and temp_list[i] == 1 and visited[i] == 0:
            visited[i] = 1
            dfs(computers[i], i, computers)

    return