def solution(nums):

    global answer

    answer = []

    for i in range(len(nums)):
        temp = [nums[i]]
        dfs(temp, i, nums, answer)
    answer.append([])
    return answer


def dfs(temp, i, nums, answer):

    answer.append(temp)

    for j in range(i + 1, len(nums)):
        temp2 = temp.copy()
        temp2.append(nums[j])
        dfs(temp2, j, nums, answer)
    
    return


print(solution([1,2,3]))