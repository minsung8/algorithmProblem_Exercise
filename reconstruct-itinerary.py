def solution(tickets):

    global answer
    start = 'JFK'
    temp = [start]
    visited = [0] * len(tickets)
    answer = []

    for i in range(len(tickets)):
        
        if tickets[i][0] == start:
            temp3 = temp.copy()
            temp3.append(tickets[i][1])
            temp2 = visited.copy()
            temp2[i] = 1
            dfs(tickets[i][1], tickets, temp3, temp2, answer)
    
    return sorted(answer)[0]


def dfs(start, tickets, temp, visited, answer):
    if len(temp) == len(tickets) + 1:
        answer.append(temp)
        return
    
    for i in range(len(tickets)):

        if tickets[i][0] == start and visited[i] == 0:
            temp.append(tickets[i][1])
            visited[i] = 1
            dfs(tickets[i][1], tickets, temp, visited, answer)

    return 

print(solution([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]))
print(solution([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]))

