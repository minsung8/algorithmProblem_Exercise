
def solution(n, info):

    temp = [0] * len(info)

    dfs(0, info, temp, n)

    return

def dfs(i, info, temp, n):

    # 승리
    temp_score = info[i] + 1
    temp_v = temp.copy()[i] = temp_score
    n_v = n - temp_score
    if n_v > 0:
        dfs(i + 1, info, temp_v, n_v)

    # 패배
    dfs(i + 1, info, temp, n)
    return

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))     # res = [0,2,2,0,1,0,0,0,0,0,0]
