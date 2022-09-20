# https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true


from collections import defaultdict

def countSort(arr):
    # Write your code here
    dic = defaultdict(list)

    for i in range(len(arr)):
        dic[int(arr[i][0])].append(arr[i][1])

    dic2 = defaultdict(list)

    for i in range(len(arr)):
        temp = []
        for j in range(len(dic[i])):

            if j == len(dic[i]) - 1:
                temp.append(dic[i][j])
            else:
                temp.append('-')
        dic2[i].append(temp)
    print(dic2)
    answer = ''
    for i in range(len(arr)):
        answer += " ".join(dic2[i][0])
        answer += ' '
    return answer


print(countSort([['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['4', 'ij'], ['0', 'ab'], ['6', 'cd'], ['0', 'ef'], ['6', 'gh'], ['0', 'ij'], ['4', 'that'], ['3', 'be'], ['0', 'to'], ['1', 'be'], ['5', 'question'], ['1', 'or'], ['2', 'not'], ['4', 'is'], ['2', 'to'], ['4', 'the']]))
# - - - - - to be or not to be - that is the question - - - -
