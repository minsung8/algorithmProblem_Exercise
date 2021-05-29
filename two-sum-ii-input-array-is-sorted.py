def solution(nums, target):

    left, right = 0, 1
    answer = []

    while True:

        if nums[left] + nums[right] == target:
            return [left + 1, right + 1]

        right += 1

        if right == len(nums):
            left += 1
            right = left + 1

    return

print(solution([2, 7, 11,15], 9))