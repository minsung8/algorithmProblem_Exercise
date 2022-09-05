# https://www.hackerrank.com/challenges/3d-surface-area/problem?isFullScreen=true

def surfaceArea(A):
    # Write your code here
    answer = 0
    for a in A:
        # 첫번째
        answer += sum(a) + (len(a) * 2) + (max(a) * 2)

        # 중간

        # 마지막

    return answer

print(surfaceArea([[1, 3, 4], [2, 2, 3], [1, 2, 4]]))   # 60

#\