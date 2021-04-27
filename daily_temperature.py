def solution(temperature):

    answer = [0] * len(temperature)

    for i in range(len(temperature)):
        temp = temperature[i]
        cnt = 1
        for j in range(i+1, len(temperature)):
            if temp < temperature[j]:
                answer[i] += cnt
                break

            else:
                cnt += 1

    return answer



def solution2(temperature):

    answer = [0] * len(temperature)
    stack = []

    for i in range(len(temperature)):

        while stack and stack[-1][1] < temperature[i]:
            temp = stack.pop(0)
            print(temp, i)
            answer[temp[0]] = i - temp[0]

        stack.append([i,temperature[i]])
    
    return answer 


print(solution2([73, 74, 75, 71, 69, 72, 76, 73]))
