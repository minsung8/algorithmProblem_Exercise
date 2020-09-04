# 프로그래머스 : https://programmers.co.kr/learn/courses/30/lessons/67259

visited = []
def solution(board):
    answer = 0
    answer_list = []
    new_board = [[1 for i in range(len(board) + 2)] for j in range(len(board) + 2)]

    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i + 1][j + 1] = board[i][j]

    start = [1, 1, -1, 0, 0]
    temp = []
    temp.append(start)
    while temp:
        temp2_list = []
        answer += 1
        for i in range(len(temp)):
            temp2_list += pos_list(temp[i], new_board, answer)
        for j in range(len(temp2_list)):
            if temp2_list[j][:2] == [len(board), len(board)]:
                answer_list.append(temp2_list[j] + [answer])
        temp = temp2_list

    result = sorted(answer_list, key=lambda x: x[3] * 5 + x[4])[0]
    return result[4] * 100 + result[3] * 500

def pos_list(temp, new_board, value):
    answer = []
    temp_list = []
    if temp[2] == -1:
        right_move = [temp[0], temp[1] + 1, 0, 0, value]
        left_move = [temp[0], temp[1] - 1, 0, 0, value]
        up_move = [temp[0] + 1, temp[1], 1, 0, value]
        down_move = [temp[0] - 1, temp[1], 1, 0, value]
    elif temp[2] == 0:
        right_move = [temp[0], temp[1] + 1, temp[2], temp[3], value]
        left_move = [temp[0], temp[1] - 1, temp[2], temp[3], value]
        up_move = [temp[0] + 1, temp[1], temp[2] + 1, temp[3] + 1, value]
        down_move = [temp[0] - 1, temp[1], temp[2] + 1, temp[3] + 1, value]
    else:
        right_move = [temp[0], temp[1] + 1, temp[2] - 1, temp[3] + 1, value]
        left_move = [temp[0], temp[1] - 1, temp[2] - 1, temp[3] + 1, value]
        up_move = [temp[0] + 1, temp[1], temp[2], temp[3], value]
        down_move = [temp[0] - 1, temp[1], temp[2], temp[3], value]
    temp_list.append(right_move), temp_list.append(left_move), temp_list.append(up_move), temp_list.append(down_move)
    for i in range(len(temp_list)):
        if new_board[temp_list[i][0]][temp_list[i][1]] == 0:
            check = False
            for j in range(len(visited)):
                if temp_list[i][:3] == visited[j][:3]:
                    check = True
                    if temp_list[i][3] * 5 + value < visited[j][3] * 5 + visited[j][4]:
                        visited[j] = temp_list[i]
                        answer.append(temp_list[i])
            if check is False:
                visited.append(temp_list[i])
                answer.append(temp_list[i])
    return answer