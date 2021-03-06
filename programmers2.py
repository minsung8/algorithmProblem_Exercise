## https://programmers.co.kr/learn/courses/30/lessons/70130

def solution(a):

    freq = {}

    for i in a:
        
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    
    most_freq1 = sorted(freq.items(), key=lambda x: -x[1])[0][0]
    second_freq = sorted(freq.items(), key=lambda x: -x[1])[1][0]     
    answer_list = []

    freq_list = [most_freq1, second_freq]

    while freq_list:

        most_freq = freq_list.pop()

        temp_list = []
        temp = []

        for i in range(len(a)):
            
            temp.append(a[i])

            if len(temp) == 2:

                if most_freq in temp:

                    if temp[0] != temp[1]:
                        temp_list.append(temp)
                        temp = []
                    else:
                        temp.pop()
                
                else:
                    temp.pop()
        if len(temp_list) < 2:
            answer_list.append(0)
            continue

        answer_list.append(len(temp_list) * 2)

    return max(answer_list)

print(solution([1, 2, 3, 2]))

    


    



