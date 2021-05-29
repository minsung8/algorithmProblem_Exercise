def solution(matrix, target):

    x = len(matrix[0]) - 1
    y = 0

    while (x >= 0) and (y <= len(matrix) - 1):

        if matrix[y][x] == target:
            return True

        if matrix[y][x] > target:
            x -= 1
        
        elif matrix[y][x] < target:
            y += 1

    return False

print(solution([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30] 
], 35))
