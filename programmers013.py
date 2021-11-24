from collections import defaultdict

def solution(a, edges):

    if sum(a) > 0:
        return - 1

    _min = min(a)
    _max = max(a)

    if abs(_min) > abs(_max):
        index = a.index(_min)
    else:
        index = a.index(_max)

    dic = defaultdict(list)

    for edge in edges:
        dic[edge[0]].append(edge[1])
        dic[edge[1]].append(edge[0])

    return dic

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
