def solution(times, n, k):

    global answer
    global visited
    
    answer = []
    visited = [0] * (n + 1)
    visited[0] = 1
    visited[k] = 1

    for i in range(len(times)):
        
        if times[i][0] == k:
            visited[ times[i][1] ] = 1
            dfs(times[i][1], times[i][2], times, n, k)

    return max(answer)

def dfs(start, cost, times, n, k):

    flag = False

    for i in range(len(times)):
        
        if times[i][0] == start and visited[ times[i][1] ] == 0:
            visited[ times[i][1] ] = 1
            dfs(times[i][1], cost + times[i][2], times, n, k)
            flag = True
    
    if flag is False:
        answer.append(cost)
        return

    return 



print(solution([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))