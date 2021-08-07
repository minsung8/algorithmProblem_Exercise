temp_answer = []

def solution(n, s, a, b, fares):

    global temp_answer

    answer = []

    for i in range(n):
        answer.append( [i+1, min(dfs(s, i + 1, 0, fares, []))] )
        temp_answer = []
    
    result = []

    for i in range(len(answer)):
        pass
    
    return answer

def dfs(start, end, cost, fares, visited):

    global temp_answer
    if start == end:
        return [0]

    visited += [start]

    for i in range(len(fares)):

        if (fares[i][0] == start and fares[i][1] == end) or (fares[i][1] == start and fares[i][0] == end):
            temp_answer.append(cost + fares[i][2])
        
        elif fares[i][0] == start and fares[i][1] != end and fares[i][1] not in visited:
            temp_visited = visited.copy()
            dfs(fares[i][1], end, cost + fares[i][2], fares, temp_visited)
         
        elif fares[i][1] == start and fares[i][0] != end and fares[i][0] not in visited:
            temp_visited = visited.copy()
            dfs(fares[i][0], end, cost + fares[i][2], fares, temp_visited)

    return temp_answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
#print(dfs(4, 1, 0, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]], []))
