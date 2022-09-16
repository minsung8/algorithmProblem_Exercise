# https://www.hackerrank.com/challenges/larrys-array/problem?isFullScreen=true

def larrysArray(A):
    # Write your code here
    
    return rotate(A)


def rotate(_list):
    return _list[1:] + [_list[0]]

print(larrysArray([3, 1, 2]))
# YES
# YES
# NO

