def solution(points, k):

    sorted_points = sorted(points, key=lambda x: abs(x[0]*x[1]), reverse=True)

    answer = []
    for i in range(k):
        answer.append(sorted_points.pop(0))
    return answer

print(solution([[1,3], [-2, 2]], 1))
print(solution([[3,3], [5, -1], [-2, 4]], 2))