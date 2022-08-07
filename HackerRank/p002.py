# https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

def simpleArraySum(a, b):
    # Write your code here
    a_point = 0
    b_point = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            a_point += 1
        elif b[i] > a[i]:
            b_point += 1

    return str(a_point) + ' ' + str(b_point)


print(simpleArraySum([5, 6, 7],[3, 6, 10]))
