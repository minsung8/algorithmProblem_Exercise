# https://www.hackerrank.com/challenges/almost-sorted/problem?isFullScreen=true

from turtle import st


def almostSorted(arr):
    # Write your code here
    answer = sorted(arr)
    cnt_list = []

    for i in range(len(arr)):
        if answer[i] != arr[i]:
            cnt_list.append(i)
    
    if len(cnt_list) == 2:
        print('yes')
        return 'swap ' + str(cnt_list[0] + 1) + ' ' + str(cnt_list[1] + 1)
    
    start_i = cnt_list[0]
    end_i = cnt_list[-1]

    temp = []
    for i in range(start_i, end_i + 1):
        temp.append(arr[i])

    temp_answer = arr[:start_i] + list(reversed(temp)) + arr[end_i + 1:]

    if temp_answer == answer:
        print('yes')
        return f'reverse {start_i + 1} {end_i + 1}'
    return 'no'


print(almostSorted([4, 2]))
# yes
# swap 1 2

print(almostSorted([3, 1, 2])) # no

print(almostSorted([1, 5, 4, 3, 2, 6]))
# yes
# reverse 2 5
