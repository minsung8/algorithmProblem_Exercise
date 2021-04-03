def solution(tickets):

    answer_list = []

    for i in range(len(tickets)):

        if tickets[i][0] == "ICN":

            temp_list = ["ICN"]
            temp_visited = [0] * len(tickets)
            temp_visited[i] = 1

            temp_answer = dfs(tickets[i][1], tickets, temp_list, temp_visited):

            if len(temp_answer) == len(tickets) + 1:
                answer_list.append(temp_answer)
            
    return answer_list


def dfs(start, tickets, temp_list, temp_visited):
    temp_list.append(start)

    for i in range(len(tickets)):
        
        if start == tickets[i][0] and temp_visited[i] == 0:
            temp_list.append(tickets[i][1])
            temp_visited[i] = 1
            dfs(tickets[i][1], tickets, temp_list, temp_visited)

    return

print( solution( [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]] ))
print( solution( [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]] ))