# https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true

def solution(n, k, r_q, c_q, obstacles):

    board = [ [0] * n for i in range(n)]
    answer = 0

    for x, y in obstacles:
        board[n - x][y - 1] = 1
    
    start_i, start_j = n - r_q, c_q - 1 
    board[start_i][start_j] = 1
    
    # i+
    for i in range(1, n):
        temp = start_i + i
        if (temp > n - 1) or board[temp][start_j] == 1:
            break
        else:
            answer += 1

    # j+
    for i in range(1, n):
        temp = start_j + i
        if (temp > n - 1) or board[start_i][temp] == 1:
            break
        else:
            answer += 1

    # i-
    for i in range(1, n):
        temp = start_i - i
        if (temp < 0) or board[temp][start_j] == 1:
            break
        else:
            answer += 1
    
    # j-
    for i in range(1, n):
        temp = start_j - i
        if (temp < 0) or board[start_i][temp] == 1:
            break
        else:
            answer += 1

    # i+j+
    for i in range(1, n):
        temp_i, temp_j = start_i + i, start_j + i
        if temp_i > n - 1 or temp_j > n - 1 or board[temp_i][temp_j] == 1:
            break
        else:
            answer += 1

    # i-j-
    for i in range(1, n):
        temp_i, temp_j = start_i - i, start_j - i
        if temp_i < 0 or temp_j < 0 or board[temp_i][temp_j] == 1:
            break
        else:
            answer += 1
    
    # i+j-
    for i in range(1, n):
        temp_i, temp_j = start_i + i, start_j - i
        if temp_i > n - 1 or temp_j < 0 or board[temp_i][temp_j] == 1:
            break
        else:
            answer += 1

    # i-j+
    for i in range(1, n):
        temp_i, temp_j = start_i - i, start_j + i
        if temp_i < 0 or temp_j > n - 1 or board[temp_i][temp_j] == 1:
            break
        else:
            answer += 1

    return answer

# 길이, 장애물 수, 퀸의 좌표, 장애물 좌표
print(solution(4, 0, 4, 4, []))     # 9
print(solution(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))     # 10
print(solution(1, 0, 1, 1, []))     # 0

# print(solution(100000, 0, 4187, 5068, []))
