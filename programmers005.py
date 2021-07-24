answer = []

def solution(arr):

    global answer

    check(arr, len(arr))
    return [answer.count(0), answer.count(1)]

def check(arr, n):

    global answer

    if n == 1:
        answer.append(arr[0][0])
        return
    
    temp1 = [[0] * n] * n
    temp2 = [[1] * n] * n    
    
    if temp1 == arr or temp2 == arr:
        answer.append(arr[0][0])
        return 

    arr1, arr2, arr3, arr4 = [], [], [], []

    for i in range(n // 2):
        arr1.append(arr[i][:n // 2])
        arr2.append(arr[i][n // 2:])
        arr3.append(arr[i + n // 2][:n // 2])
        arr4.append(arr[i + n // 2][n // 2:])
    
    check(arr1, n // 2), check(arr2, n // 2), check(arr3, n // 2), check(arr4, n // 2)  


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))