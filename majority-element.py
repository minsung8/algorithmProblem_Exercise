def solution(nums):

    memo = {}

    for i in nums:
        if i not in memo:
            memo[i] = nums.count(i)
        
        if memo[i] > len(nums) / 2:
            return i

    return memo

print(solution([3,2,3]))
print(solution([2,2,1,1,1,2,2]))