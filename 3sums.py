def solution(nums):     ## 합 = 0

    sort_nums = sorted(nums)
    answer = []

    x = 0
    y = 1
    z = 2

    while x < len(nums) - 2:

        z += 1

        if z == len(nums):
            x += 1
            y = x + 1
            z = y + 1
        
        if z >= len(nums):
            break

        if sort_nums[x] + sort_nums[y] + sort_nums[z] == 0:
            answer.append([sort_nums[x], sort_nums[y], sort_nums[z]])
        
        if sort_nums[x] + sort_nums[y] + sort_nums[z] > 0:
            x += 1
            y = x + 1
            z = y + 1
        
    return answer

print( solution([-1, 0, 1, 2, -1, -4]) )