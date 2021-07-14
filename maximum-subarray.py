def solution(nums):

    for i in range(1, len(nums)):
        nums[i] = max(nums[i - 1] + nums[i], 0)

    return nums

print(solution([-2,1,-3,4,-1,2,1,-5,4,3]))