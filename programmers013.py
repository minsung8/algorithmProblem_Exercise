def solution(a, edges):
    if sum(a) > 0:
        return - 1

    _min = min(a)
    _max = max(a)

    if abs(_min) > abs(_max):
        index = a.index(_min)
    else:
        index = a.index(_max)

    temp_list = [index]
    answer = 0
    score = 1

    while temp_list:
        temp = temp_list.pop(0)

        for edge in edges:
            if temp in edge:
                pass
    
    return 


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
print(solution([0, 1, 0], [[0,1],[1,2]])) # -1
