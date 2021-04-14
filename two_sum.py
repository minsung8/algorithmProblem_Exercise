def solution(nums, target):

    sort_nums = sorted(nums)

    answer = []

    x1 = 0
    x2 = 1

    while x1 < len(nums) and x2 < len(nums):
        print(x1, x2)

        if nums[x1] + nums[x2] == target:
            answer.append(x1)
            answer.append(x2)
        elif  nums[x1] + nums[x2] > target:
            x1 += 1
            x2 = x1
        
        x2 += 1

        if x2 == len(nums):
            x1 += 1
            x2 = x1 + 1
        
    return answer


print( solution([2, 7, 11, 15], 26) )
