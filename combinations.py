def solution(n, k):

    global answer
    answer = []

    for i in range(1, n + 1):
        temp = [i]
        dfs(temp, i, n, k, answer)
    return answer

def dfs(temp, i, n, k, answer):

    if len(temp) == k:
        answer.append(temp)
        return

    for i in range(i + 1, n + 1):
        temp2 = temp.copy() + [i]
        dfs(temp2, i, n, k, answer)
    return

print(solution(4, 2))