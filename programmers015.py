global_board = []

def solution(board, skill):

    global global_board
    global_board = board

    for s in skill:
        # type = s[0]
        # start_i, start_j = s[1], s[2]
        # end_i, end_j = s[3], s[4]
        # degree = s[5]

        if s[0] == 1:   # attack
            cal(s[1], s[2], s[3], s[4], (s[5] * -1))
        else:   # recovery
            cal(s[1], s[2], s[3], s[4], s[5])

    return count(global_board)

def count(board):
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                cnt += 1
    return cnt

def cal(start_i, start_j, end_i, end_j, deg):
    global global_board

    for i in range(start_i, end_i + 1):
        for j in range(start_j, end_j + 1):
            global_board[i][j] += deg

    return

print(solution(
    [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
    [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
))  # res = 10

print(solution(
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
))  # res = 6
