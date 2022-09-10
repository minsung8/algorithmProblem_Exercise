# https://www.hackerrank.com/challenges/bomber-man/problem?isFullScreen=true


def bomberMan(n, grid):
    # Write your code here

    start_grid = grid.copy()
    all_bomb_grid = []

    for i in range(len(grid)):
        all_bomb_grid.append('O' * len(grid))

    n -= 3

    while True:
        all_bomb_grid = []
        for i in range(len(grid)):
            all_bomb_grid.append(list('O' * len(grid[0])))

        for i in range(len(start_grid)):
            for j in range(len(start_grid[i])):
                if start_grid[i][j] == 'O':
                    all_bomb_grid[i][j] = '.'
                    if i + 1 < len(all_bomb_grid): all_bomb_grid[i + 1][j] = '.'
                    if j + 1 < len(all_bomb_grid[0]): all_bomb_grid[i][j + 1] = '.'
                    if i > 0: all_bomb_grid[i - 1][j] = '.'
                    if j > 0: all_bomb_grid[i][j - 1] = '.'
        
        answer = []
        for g in all_bomb_grid:
            answer.append("".join(g))
        start_grid = answer

        if n <= 0:
            return start_grid
        
        if n % 2 == 1:
            for i in range(len(grid)):
                all_bomb_grid.append('O' * len(grid)) 
            return all_bomb_grid
        n -= 2

print(bomberMan(3, ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']))
# OOO.OOO
# OO...OO
# OOO...O
# ..OO.OO
# ...OOOO
# ...OOOO

print(bomberMan(5, ['.......', '...O.O.', '....O..', '..O....', 'OO...OO', 'OO.O...']))
# .......
# ...O.O.
# ...OO..
# ..OOOO.
# OOOOOOO
# OOOOOOO


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