import heapq

def solution(people):

    temp_list = sorted(people, key=lambda x: (x[0], -x[1]), reverse=True)
    answer = []
    print(temp_list)
    for p in temp_list:
        print(answer)
        if p[1] >= len(answer):
            answer.append(p)
        else:
            answer = answer[:p[1]] + [p] + answer[p[1]:]
    
    return answer

print(solution([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
