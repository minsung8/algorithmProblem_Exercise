answer = []

def solution(arr):

    idx = len(arr)
    answer = []
    check(arr, idx)
    return idx

def check(arr, n):

    if n == 1:
        answer.append(arr[0][0])
    return 

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))