visited = []

def solution(game_board, table):

    global visited
    # 1. 개수가 맞아야 함
    # 2. 회전만으로 모양 일치 

    answer = 0

    visited = [[0] * len(game_board[0]) for j in range(len(game_board))]
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            
            if game_board[i][j] == 0:
                temp = bfs(i, j, game_board)
                print(temp)
                if checked_table(temp):
                    answer += len(temp)

    return answer

def checked_table(temp):
    return True

def bfs(start_i, start_j, game_board):
    global visited
    answer = [[start_i, start_j]]
    temp = [[start_i, start_j]]

    visited[start_i][start_j] = 1

    while temp:

        temp_i, temp_j = temp.pop()

        if temp_i - 1 >= 0 and game_board[temp_i - 1][temp_j] == 0 and visited[temp_i - 1][temp_j] == 0:
            temp.append([temp_i - 1, temp_j])
            answer.append([temp_i - 1, temp_j])
            visited[temp_i - 1][temp_j] = 1

        if temp_i + 1 < len(game_board) and game_board[temp_i + 1][temp_j] == 0 and visited[temp_i + 1][temp_j] == 0:
            temp.append([temp_i + 1, temp_j])
            answer.append([temp_i + 1, temp_j])
            visited[temp_i + 1][temp_j] = 1

        if temp_j - 1 >= 0 and game_board[temp_i][temp_j - 1] == 0 and visited[temp_i][temp_j - 1] == 0:
            temp.append([temp_i, temp_j - 1])
            answer.append([temp_i, temp_j - 1])
            visited[temp_i][temp_j - 1] = 1

        if temp_j + 1 < len(game_board[0]) and game_board[temp_i][temp_j + 1] == 0 and visited[temp_i][temp_j + 1] == 0:
            temp.append([temp_i, temp_j + 1])
            answer.append([temp_i, temp_j + 1])
            visited[temp_i][temp_j + 1] = 1

    return answer

print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
    [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
#print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))
