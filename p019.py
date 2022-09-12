# https://www.hackerrank.com/challenges/two-pluses/problem?isFullScreen=true


def twoPluses(grid):
    
    answer = []

    idx = 1

    while True:

        answer += check(idx, grid)

        idx += 1

        if (4 * idx - 3) > len(grid) * len(grid[0]):
            break
    print(answer)
    answer = sorted(answer, reverse=True)
    return answer[0] * answer[1]

def check(idx, grid):
    answer = []
    visited = []

    for i in range(len(grid)):
        visited.append([0] * len(grid[0]))

    start_i = idx - 1 
    start_j = idx - 1

    for i in range(start_i, len(grid) - start_i):
        for j in range(start_j, len(grid[i]) - start_j):

            if grid[i][j] == 'G':
                flag = True
                for k in range(idx):
                    
                    if grid[i + k][j] != 'G' or visited[i + k][j] == 1:
                        flag = False
                        break
                    if grid[i][j + k] != 'G' or visited[i][j + k] == 1:
                        flag = False
                        break
                    if grid[i - k][j] != 'G' or visited[i - k][j] == 1:
                        flag = False
                        break
                    if grid[i][j - k] != 'G' or visited[i][j - k] == 1:
                        flag = False
                        break

                if flag:
                    visited[i + idx - 1][j] = 1
                    visited[i][j + idx - 1] = 1
                    visited[i - idx + 1][j] = 1
                    visited[i][j - idx + 1] = 1
                    answer.append(4 * idx - 3)
                    break

    return answer
    

print(twoPluses(['GGGGGG', 'GBBBGB', 'GGGGGG', 'GGBBGB', 'GGGGGG']))    # 5
print(twoPluses(['BGBBGB', 'GGGGGG', 'BGBBGB', 'GGGGGG', 'BGBBGB', 'BGBBGB']))    # 25


print(twoPluses([
'GGGGGGG',
'BGBBBBG',
'BGBBBBG',
'GGGGGGG',
'GGGGGGG',
'BGBBBBG']))   
