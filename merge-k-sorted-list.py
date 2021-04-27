def solution(t):

    answer = []

    for i in range(len(t)):

        answer += t[i]

    return sorted(answer)
print(solution([[1, 4, 5], [1, 3, 4], [2, 6]]))