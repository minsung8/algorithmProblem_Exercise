# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3


def solution(queue1, queue2):
    _sum = (sum(queue1) + sum(queue2))
    if _sum % 2 != 0: return -1
    answer = _sum // 2

    i, j = 0, 0
    a, b = 0, 0
    res = 0


    while i < len(queue1) or j < len(queue2):

        if i < len(queue1) and a + queue1[i] < answer:
            a += queue1[i]
            i += 1

        elif j < len(queue2) and a + queue2[j] < answer:
            a += queue2[j]
            j += 1
            res += 1
        else:
            if i < len(queue1):
                b += queue1[i]
                i += 1
            elif j < len(queue2):
                b += queue2[j]
                j += 1

            return a, b, i ,j, res

    return a, b, i, j, res


# print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2 
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7


# 1 2 1 2 1 10 / 2
# 1 2 , 1 2 1 2 2 / 5 