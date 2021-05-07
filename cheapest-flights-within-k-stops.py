def solution(n, edges, start, end, k):

    global answer

    answer = []

    for i in range(len(edges)):

        if edges[i][0] == start:
            temp_cost = edges[i][2]
            temp_cnt = 0
            dfs(edges, edges[i][1], end, temp_cost, temp_cnt, k, answer)

    return min(answer)

def dfs(edges, start, end, temp_cost, temp_cnt, k, answer):
    
    if temp_cnt > k:
        return

    if start == end:
        answer.append(temp_cost)

    for i in range(len(edges)):

        if edges[i][0] == start:
            temp_cost2 = temp_cost + edges[i][2]
            temp_cnt2 = temp_cnt + 1
            dfs(edges, edges[i][1], end, temp_cost2, temp_cnt2, k, answer)
    
    return 

print(solution( 3, [[0,1,100], [1,2,100], [0,2,500]], 0, 2, 0 ))