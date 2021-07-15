def solution(nums):
    answer = 0
    i = 0
    while i < len(nums):
        temp = nums[i:i+3]
        
        if len(temp) == 3:
            if temp[1] > temp[0] + temp[2]:
                answer += temp[1]
                i += 3
            else:
                answer += temp[0]
                i += 2
        else:
            answer += max(temp)
            break

    return answer



print(solution([1, 2, 3, 1, 4, 7, 2, 1]))
print(solution([2, 7, 9, 3, 1]))
print(solution([1,2,3,1]))
