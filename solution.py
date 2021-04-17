def solution(rows, columns, queries):
    
    table = []
    idx = 1
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(idx)
            idx += 1
        table.append(temp)
    
    answer = []

    for i in range(len(queries)):

        temp = []

        start_y = queries[i][0]
        start_x = queries[i][1]    
        end_y = queries[i][2]
        end_x = queries[i][3]

        temp_len_x = end_x - start_x
        temp_len_y = end_y - start_y

        temp_x = end_x - 1
        temp_s1 = table[start_y-1][end_x-1]
        temp.append(temp_s1)
        for a in range(temp_len_x):
            table[start_y-1][temp_x] = table[start_y-1][temp_x-1]
            temp.append(table[start_y-1][temp_x])
            temp_x -= 1

        ## temp_s1 = 10
        temp_y = end_y
        temp_s2 = 0
        temp_s2 = table[temp_y-1][end_x-1]
        temp.append(temp_s2)
        for b in range(temp_len_y):
            table[temp_y-1][end_x-1] = table[temp_y-2][end_x-1]
            temp.append(table[temp_y-1][end_x-1])
            temp_y -= 1
        table[start_y][end_x-1] = temp_s1

        ## temp_s2 = 28
        temp_x = start_x - 1
        temp_s3 = table[end_y-1][start_x-1]
        temp.append(temp_s3)
        for a in range(temp_len_x-1):
            table[end_y-1][temp_x] = table[end_y-1][temp_x+1]
            temp.append(table[end_y-1][temp_x])
            temp_x += 1
        table[end_y-1][end_x-2] = temp_s2

        ## temp_s3 = 26
        temp_y = start_y
        for b in range(temp_len_y):
            table[temp_y-1][start_x-1] = table[temp_y][start_x-1]
            temp.append(table[temp_y-1][start_x-1])
            temp_y += 1
        table[end_y-2][start_x-1] = temp_s3

        answer.append(min(temp))
        

    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
