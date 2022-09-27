# https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true

from tempfile import tempdir
from tkinter import W


def lilysHomework(arr):
    # Write your code here

    # front 
    f_arr = arr.copy()
    front_cnt = 0
    front_answer = sorted(arr)
    f_idx = 0

    while True:

        for i in range(len(f_arr)):

            if f_arr[i] == front_answer[f_idx]:

                if i == f_idx: break
                else:
                    temp = f_arr[f_idx]
                    f_arr[f_idx] = f_arr[i]
                    f_arr[i] = temp
                    front_cnt += 1
                    break
        f_idx += 1
                    
        if f_idx == len(f_arr): break

    # back
    b_arr = arr.copy()
    back_cnt = 0
    back_answer = sorted(arr, reverse=True)
    b_idx = 0

    while True:

        for i in range(len(b_arr)):

            if b_arr[i] == back_answer[b_idx]:

                if i == b_idx: break
                else:
                    temp = b_arr[b_idx]
                    b_arr[b_idx] = b_arr[i]
                    b_arr[i] = temp
                    back_cnt += 1
                    break
        b_idx += 1
                    
        if b_idx == len(b_arr): break

    return min(back_cnt, front_cnt)


print(lilysHomework([2, 5, 3, 1]))  # 2
print(lilysHomework([3, 4, 2, 5, 1]))    # 2

