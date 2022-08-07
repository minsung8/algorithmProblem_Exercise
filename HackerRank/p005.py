# https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

def simpleArraySum(arr):
    # Write your code here

    positive_cnt = 0
    negative_cnt = 0
    zero_cnt = 0
    sum_cnt = 0
    for n in arr:
        if n > 0:
            positive_cnt += 1
        elif n == 0:
            negative_cnt += 1
        else:
            zero_cnt += 1
    sum_cnt = positive_cnt + negative_cnt + zero_cnt
    print(round(positive_cnt/sum_cnt, 6))
    print(round(zero_cnt/sum_cnt, 6))
    print(round(negative_cnt/sum_cnt, 6))

print(simpleArraySum([-4, 3, -9, 0, 4, 1]))
