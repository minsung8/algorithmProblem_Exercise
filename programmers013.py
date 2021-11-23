def solution(a, edges):

    if sum(a) > 0:
        return - 1

    _min = min(a)
    _max = max(a)

    if abs(_min) > abs(_max):
        index = a.index(_min)
    else:
        index = a.index(_max)

    temp_list = [[index, 1]]
    answer = 0
    visited = [0] * len(edges)
 
    while temp_list:
        temp, temp_score = temp_list.pop(0)
        next_score = temp_score + 1

        i = 0
        while i < len(edges):
            
            if edges[i][0] == temp:
                answer += temp_score * a[edges[i][1]]
                temp_list.append([edges[i][1], next_score])
                edges.pop(i)
                
            elif edges[i][1] == temp:
                answer += temp_score * a[edges[i][0]]
                temp_list.append([edges[i][0], next_score])
                edges.pop(i)    
            i += 1
            print(edges)

        print(temp_list, answer)
        
    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
