import time

def solution(nums, k):
    start = time.time()

    answer = []
    i = 0

    while i + k - 1 < len(nums):
        
        answer.append(max(nums[i:i+k]))
        i += 1
    end = time.time()
    print(end - start)
    return answer


def solution2(nums, k):
    start_t = time.time()

    start = nums[:k]
    temp_max = max(start)
    answer = [temp_max]

    for i in range(k, len(nums)):

        temp = start.pop(0)

        if temp == temp_max:
            start.append(nums[i])
            temp_max = max(start)
            answer.append(temp_max)
        else:
            start.append(nums[i])
            answer.append(temp_max)
    end = time.time()
    print(end - start_t)
    return answer 

print(solution([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(solution2([1, 3, -1, -3, 5, 3, 6, 7], 3))

