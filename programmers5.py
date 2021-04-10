def solution(tickets):
    
    answer_list = []
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            visited = [0] * len(tickets)
            visited[i] = 1
            temp = ["ICN", tickets[i][1]]
            result = bfs(tickets, visited, tickets[i][1], temp)

            if len(result) == len(tickets) + 1:

                answer_list.append(result)
    return answer_list

def bfs(tickets, visited, start, temp):
    print(visited)
    for i in range(len(tickets)):

        if visited[i] == 0 and tickets[i][0] == start:
            go = []
            for j in range(len(visited)):
                go.append(visited[j])
            go[i] = 1
            temp.append(tickets[i][1])
            bfs(tickets, go, tickets[i][1], temp)

    return temp


#print( solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) )
print( solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) )
#print( solution([['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'], ['BOO', 'DOO'], ['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO']]) )


#[ ['COO', 'DOO'], ['DOO', 'COO'], ['COO', 'BOO']]