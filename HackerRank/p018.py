# https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true


def bomberMan(n, grid):
    # Write your code here
    if n == 1: 
        return grid

    real_bomb_grid = []
    for i in range(len(grid)):
        real_bomb_grid.append('O' * len(grid[0]))

    if n % 2 == 0: return real_bomb_grid

    cnt = (n - 1) // 2

    bomb_grid = real_bomb_grid.copy()
    answer = []
    for c in range(4):
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == 'O':
                    bomb_grid[i] = bomb_grid[i][:j] + '.' + bomb_grid[i][j + 1:]

                    if i + 1 < len(grid): bomb_grid[i + 1] = bomb_grid[i + 1][:j] + '.' + bomb_grid[i + 1][j + 1:]
                    if j + 1 < len(grid[0]): bomb_grid[i] = bomb_grid[i][:j + 1] + '.' + bomb_grid[i][j + 2:]
                    if i > 0: bomb_grid[i - 1] = bomb_grid[i - 1][:j] + '.' + bomb_grid[i - 1][j + 1:]
                    if j > 0: bomb_grid[i] = bomb_grid[i][:j - 1] + '.' + bomb_grid[i][j:]
        answer.append(bomb_grid)
        grid = bomb_grid
        bomb_grid = real_bomb_grid.copy()
    
    if cnt % 2 == 0: return answer[1]
    return answer[0]

print(bomberMan(3, ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']))
# print(bomberMan(7, ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']))
# print(bomberMan(9, ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']))
# print(bomberMan(11, ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']))

# OOO.OOO
# OO...OO
# OOO...O
# ..OO.OO
# ...OOOO
# ...OOOO
print(bomberMan(5, ['.......', '...O.O.', '....O..', '..O....', 'OO...OO', 'OO.O...']))

# # .......
# # ...O.O.
# # ...OO..
# # ..OOOO.
# # OOOOOOO
# # OOOOOOO


# 1 -> 그대로
# 2 -> 올
# 3 -> 터짐
# 4 -> 그대로 

# '.......' 
# '...O.O.' 
# '....O..' 
# '..O....'
# 'OO...OO'
# 'OO.O...'

# 3초 후 
# OOOO.OO
# OO.....
# OO....O
# .......
# .......
# .......

# .......
# ...O.O.
# ...OO..
# ..OOOO.
# OOOOOOO
# OOOOOOO