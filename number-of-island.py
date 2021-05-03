def solution(island):

    global visited
    answer = 0
    visited = [[0] * len(island[0]) for _ in range(len(island))]

    for i in range(len(island)):
        for j in range(len(island[i])):

            if visited[i][j] == 0 and island[i][j] == 1:
                visited[i][j] = 1
                dfs(island, i, j)
                answer += 1
    
    return answer

def dfs(island, i, j):
    global visited

    temp = [ [i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1] ]

    for i in range(len(temp)):
        x = temp[i][0]
        y = temp[i][1]

        if (0 <= x and x < len(island)) and (0 <= y and y < len(island[0])) and visited[x][y] == 0 and island[x][y] == 1 :
            visited[x][y] = 1
            dfs(island,x,y)
        
    return 

print(solution([[1,1,1,1,0], [1,1,0,1,0], [1,1,0,0,0], [0,0,0,0,0]]))
print(solution( [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,0,0], [0,0,0,1,1]]))
print(solution([[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0]]))