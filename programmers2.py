## https://programmers.co.kr/learn/courses/30/lessons/70130

def solution(a):

    freq = {}

    for i in a:
        
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    answer_list = []
    temp = []
    
    most_freq = sorted(freq.items(), key=lambda x: -x[1])[0][0]

    for i in range(len(a)):
        
        temp.append(a[i])

        if len(temp) == 2:

            if most_freq in temp:

                if temp[0] != temp[1]:
                    answer_list.append(temp)
                    temp = []
                else:
                    temp.pop()
            
            else:
                temp.pop()
    
    if len(answer_list) < 2:
        return 0

    return len(answer_list) * 2

print(solution([0,3,3,0,7,0,2,0]))
print(solution([5,2,3,3,5,3]))
print(solution([0, 1, 2, 1]))

print(solution([5,2,3,3,5,3,7]))

    


    



