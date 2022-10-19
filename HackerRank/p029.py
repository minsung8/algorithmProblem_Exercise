# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3


def solution(queue1, queue2):

    _sum = (sum(queue1) + sum(queue2))

    if _sum % 2 != 0: return -1
    answer = _sum // 2

    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2 
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7

# 2 2 3 7
# 1 4 5 6

# 1 1 2 2
# 1 1 2 10

# 2

