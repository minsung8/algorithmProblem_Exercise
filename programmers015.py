#   imos 알고리즘 사용

def solution(board, skill):
    answer = 0
    temp_board =[[0 for j in range(len(board[0])+1)] for i in range(len(board) + 1)]

    for s in skill:

        if s[0] == 1:   # 파괴
            temp_score = -s[5]
        else:   # 회복
            temp_score = s[5]

        for i in range(s[1], s[3] + 1):
            temp_board[i][s[2]] += temp_score
            temp_board[i][s[4] + 1] += (temp_score * -1)
    
    for i in range(len(temp_board)):
        for j in range(1, len(temp_board[i]) - 1):
            temp_board[i][j] += temp_board[i][j - 1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += temp_board[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


print(solution(
    [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
    [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
))  # res = 10

print(solution(
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
))  # res = 6
