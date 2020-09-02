visited = [[[1, 1], [1, 2]]]
def solution(board):

    answer = 0

    new_board = [[1 for i in range(len(board) + 2)] for j in range(len(board) + 2)]

    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i + 1][j + 1] = board[i][j]

    start = [[1, 1], [1, 2]]
    temp_list = []
    temp_list.append(start)
    while temp_list:

        answer += 1
        temp2_list = []
        for i in range(len(temp_list)):

            temp3_list = pos_list(temp_list[i], new_board)

            if [[len(board) - 1, len(board)], [len(board), len(board)]] in temp3_list or [[len(board), len(board) - 1], [len(board), len(board)]] in temp3_list:

                return answer

            temp2_list += temp3_list

        temp_list = temp2_list
        print(temp_list, answer)


def pos_list(temp_list, board):

    global visited

    y1, x1 = temp_list[0][0], temp_list[0][1]
    y2, x2 = temp_list[1][0], temp_list[1][1]

    answer_list = []
    temp2_list = []

    right_move = [[y1, x1 + 1], [y2, x2 + 1]]
    left_move = [[y1, x1 - 1], [y2, x2 - 1]]
    down_move = [[y1 + 1, x1], [y2 + 1, x2]]
    up_move = [[y1 - 1, x1], [y2 - 1, x2]]

    temp2_list.append(right_move),  temp2_list.append(left_move),  temp2_list.append(down_move),  temp2_list.append(up_move)

    if y1 == y2:          # 가로모양
        if board[y1 - 1][x1] == 0 and board[y2 - 1][x2] == 0:
            temp2_list.append([[y1 - 1, x1], [y1, x1]])
            temp2_list.append([[y2 - 1, x2], [y2, x2]])
        if board[y1 + 1][x1] == 0 and board[y2 + 1][x2] == 0:
            temp2_list.append([[y1, x1], [y1 + 1, x1]])
            temp2_list.append([[y2, x2], [y2 + 1, x2]])

    else:          # 세로모양
        if board[y1][x1 - 1] == 0 and board[y2][x2 - 1] == 0:
            temp2_list.append([[y1, x1 - 1], [y1, x1]])
            temp2_list.append([[y2, x2 - 1], [y2, x2]])
        if board[y1][x1 + 1] == 0 and board[y2][x2 + 1] == 0:
            temp2_list.append([[y1, x1], [y1, x1 + 1]])
            temp2_list.append([[y2, x2], [y2, x2 + 1]])

    for i in range(len(temp2_list)):

        temp_y1, temp_x1 = temp2_list[i][0][0], temp2_list[i][0][1]
        temp_y2, temp_x2 = temp2_list[i][1][0], temp2_list[i][1][1]

        if board[temp_y1][temp_x1] == 0 and board[temp_y2][temp_x2] == 0 and temp2_list[i] not in visited:
            visited.append(temp2_list[i])
            answer_list.append(temp2_list[i])

    return answer_list