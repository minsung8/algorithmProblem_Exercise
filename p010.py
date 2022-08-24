# https://www.hackerrank.com/challenges/queens-attack-2/problem?isFullScreen=true

def solution(n, k, r_q, c_q, obstacles):

    board = [ [0] * n for i in range(n)]

    # 장애물 설정
    for x, y in obstacles:
        board[n - x][y - 1] = 1
    
    start = n - r_q, c_q - 1 
    return board, start

# 길이, 장애물 수, 퀸의 좌표, 장애물 좌표
#print(solution(4, 0, 4, 4, []))     # 9
print(solution(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]))     # 10
#print(solution(1, 0, 1, 1, []))     # 0

