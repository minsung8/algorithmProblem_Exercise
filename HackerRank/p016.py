# https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true

def surfaceArea(A):

    answer = 0
    for i in range(len(A)):
        if i == 0:
            answer += sum(A[i]) + (len(A[i]) * 2) + (max(A[i]) * 2)
            if len(A) == 1: answer += sum(A[0])

        elif i == len(A) - 1:
            answer += (len(A[i]) * 2) + (max(A[i]) * 2)
            for j in range(len(A[i])):
                answer += abs(A[i][j] - A[i - 1][j])
            answer += sum(A[i])

        else:
            answer += (len(A[i]) * 2) + (max(A[i]) * 2)
            for j in range(len(A[i])):
                answer += abs(A[i][j] - A[i - 1][j])

    return answer

print(surfaceArea([[1]]))   # 6
print(surfaceArea([[1, 3, 4], [2, 2, 3], [1, 2, 4]]))   # 60

# 2 3   