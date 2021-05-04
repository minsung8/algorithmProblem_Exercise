def solution(nums):

    global answer

    answer = []

    for i in range(len(nums)):

        dfs(nums, [nums[i]], answer)

    return answer

def dfs(nums, temp, answer):

    if len(temp) == 3:
        answer.append(temp)
        return 

    for i in range(len(nums)):
        temp2 = temp.copy()
        if nums[i] not in temp:
            temp2.append(nums[i])
            dfs(nums, temp2, answer)

    return 
 
print(solution([1, 2, 3]))

