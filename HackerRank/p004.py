# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

def simpleArraySum(arr):
    # Write your code here
    a, b = 0, 0
    for i in range(len(arr)):
        a += arr[i][i]
        b += arr[i][len(arr) - i - 1]

    return abs(a - b)

print(simpleArraySum([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
