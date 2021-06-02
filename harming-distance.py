def solution(x, y):
    temp = bin(x ^ y)
    return temp.count("1")

print(solution(1, 4))