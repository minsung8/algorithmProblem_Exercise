from collections import defaultdict

def solution(a, edges):

    if sum(a) != 0:
        return -1 

    dic = defaultdict(list)

    for x, y in edges:
        dic[x].append(y)
        dic[y].append(x)

    temp_list = sorted(list(dic.keys()), key=lambda x: len(dic[x]))
    visited = []
    answer = 0

    for temp in temp_list:
        dif = a[temp]
        for i in range(len(dic[temp])):
            if dic[temp][i] not in visited:
                a[dic[temp][i]] += dif
                a[temp] = 0
                visited.append(temp)
                answer += abs(dif)
                break
    
    for temp in a:
        if temp != 0:
            return -1
    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
