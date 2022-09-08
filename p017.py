# https://www.hackerrank.com/challenges/absolute-permutation/problem?isFullScreen=true


def absolutePermutation(n, k):
    # Write your code here

    _list = []
    for i in range(1, n + 1):
        _list.append(i)

    _answer = []

    for i in range(len(_list)):
        if _list[i] - k > 0:
            _answer.append(_list[i] - k)
        else:
            if _list[i] + k > n:
                return [-1]
            _answer.append(_list[i] + k) 

    return _answer

print(absolutePermutation(4, 2))    # 2 1

print(absolutePermutation(2, 1))    # 2 1
print(absolutePermutation(3, 0))    # 1 2 3
print(absolutePermutation(3, 2))    # -1
