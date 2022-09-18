# https://www.hackerrank.com/challenges/larrys-array/problem?isFullScreen=true

def larrysArray(A):

    answer = sorted(A)
    pre_A = A
    start_i = 0

    while True:
        for i in range(start_i, len(A) - 2):
            if i + 1 != A[i]:
                A = A[:i] + rotate(A[i:i+3]) + A[i+3:]

        for i in range(len(A)):
            if A[i] != i + 1:
                start_i = i
                break

        if A == answer: return "YES"

        if pre_A == A: break
        pre_A = A.copy()

    return "NO"


def rotate(_list):

    _min = min(_list)

    if _list[0] == _min: return _list
    elif _list[1] == _min: return [_list[1], _list[2], _list[0]]
    else: return [_list[2], _list[0], _list[1]]


print(larrysArray([3, 1, 2]))   # yes
print(larrysArray([1, 3, 4, 2]))   # yes
print(larrysArray([1, 2, 3, 5, 4]))   # no

print(larrysArray([3, 1, 2, 4]))   # yes
print(larrysArray([1, 6, 5, 2, 3, 4]))   # no
print(larrysArray([1, 6, 5, 2, 4, 3]))   # yes


# print(larrysArray([263, 553, 326, 480, 536, 65, 796, 176, 597, 459, 71, 220, 10, 439, 756]))
# 1 2 3 5 4
# 1 2 3 5 4

# 1 2 6 5 4 3
# 1 2 4 6 5 3
# 1 2 4 3 6 5

# 1 2 3 6 4 5
# 1 2 3 4 5 6
