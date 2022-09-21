# https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true


from collections import defaultdict

def countSort(arr):

    # Write your code here
    mid = int(len(arr) / 2)
    for temp in arr[:mid]:
        temp[1] = '-'

    arr = sorted(arr, key=lambda e: int(e[0]))

    answer = ''
    for temp in arr:
        answer += temp[1] + ' '
        
    return answer


print(countSort([['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'], ['1', 'be'], ['5', 'question'], ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']]))
# - - - - - to be or not to be - that is the question - - - -
