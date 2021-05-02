def solution(nums, k):

    dic = {}

    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = nums.count(nums[i])

    answer = []
    keys_list = list(dic.keys())

    for i in range(len(keys_list)):

        if dic[ keys_list[i] ] >= k:
            answer.append(keys_list[i])

    return answer


print(solution([1,1,1,2,2,3], 2))