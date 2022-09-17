# https://www.hackerrank.com/challenges/larrys-array/problem?isFullScreen=true

def larrysArray(A):
    real_answer = sorted(A)
    # Write your code here
    for i in range(len(A)):

        if i >= len(A) - 2: break
        
        if A[i] != i + 1:
            print(i, A)
            res = rotate(A[i:i+3], i + 1)
            
            if res == -1: continue
            if i + 3 <= len(A) - 1:
                A = A[:i] + res + A[i+3:]
            else:
                A = A[:i] + res

    if real_answer == A: return 'YES'
    return 'NO'


def rotate(_list, i):

    if i not in _list:
        return -1

    answer = []
    
    for j in range(len(_list)):
        if _list[j] == i:
            
            while True:
                answer.append(_list[j])
                j += 1
                if j == i: break
                if j == len(_list): j = 0

    return answer

# print(larrysArray([3, 1, 2]))   # yes
# print(larrysArray([1, 3, 4, 2]))   # yes
# print(larrysArray([1, 2, 3, 5, 4]))   # no

# print(larrysArray([3, 1, 2, 4]))   # yes
# print(larrysArray([1, 6, 5, 2, 3, 4]))   # no
print(larrysArray([1, 6, 5, 2, 4, 3]))   # yes


# 1 2 6 5 3 4
# 1 2 5 3 6 4
# 1 2 3 6 5 4
# 1 2 3 5 4 6
# 1 2 3 4 6 5