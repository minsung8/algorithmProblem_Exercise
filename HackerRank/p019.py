# https://www.hackerrank.com/challenges/two-pluses/problem?isFullScreen=true


from re import L


visited = []

def twoPluses(grid):

    global visited

    for i in range(len(grid)):
        visited.append([0] * len(grid[0]))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            
            if grid[i][j] == 'G':
                check(i, j, grid)
    return 

def check(i, j, grid):
    pass

print(twoPluses(['GGGGGG', 'GBBBGB', 'GGGGGG', 'GGBBGB', 'GGGGGG']))    # 5
print(twoPluses(['BGBBGB', 'GGGGGG', 'BGBBGB', 'GGGGGG', 'BGBBGB', 'BGBBGB']))    # 25
