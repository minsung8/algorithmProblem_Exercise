def solution(candidates, target):
    
    global answer

    answer = []

    for i in range(len(candidates)):
        temp = [candidates[i]]
        dfs(temp, candidates, target, answer, i)

    return answer


def dfs(temp, candidates, target, answer, k):

    if sum(temp) == target and sorted(temp) not in answer:
        answer.append(sorted(temp))
        return 
    elif sum(temp) > target:
        return

    for i in range(len(candidates)):
        temp2 = temp.copy() + [candidates[i]]
        dfs(temp2, candidates, target, answer, i)
    return 

print(solution([2,3,6,7], 7))