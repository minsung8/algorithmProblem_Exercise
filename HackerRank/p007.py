# https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true

def simpleArraySum(arr):
    # Write your code here
    answer = []
    poss = []

    for i in range(1, 10):
        for j in range(1, 10):
            if i != j and set([i, 15 - (i + j), j, 5 + j - i, 5, 5 - j + i, 10 - j, i + j - 5, 10 - i]) == set(range(1,10)):
                poss.append([i, 15 - (i + j), j, 5 + j - i, 5, 5 - j + i, 10 - j, i + j - 5, 10 - i])
    
    temp_list = arr[0] + arr[1] + arr[2]
    for temp in poss:
        temp_answer = 0
        for i in range(len(temp_list)):
            temp_answer += abs(temp_list[i] - temp[i])
        answer.append(temp_answer)

    
    return answer
    

print(simpleArraySum([[4, 9, 2], [3, 5, 7], [8, 1, 5]]))
