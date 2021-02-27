## https://programmers.co.kr/learn/courses/30/lessons/70130

def solution(a):

    if len(a) < 2:
        return 0

    freq_dic = {}

    for i in a:
        if i not in freq_dic:
            freq_dic[i] = 1
        else:
            freq_dic[i] += 1
    
    most_freq_val = 0
    freq = 0

    for i in a:
        if freq < freq_dic[i]:
            most_freq_val = i
            freq = freq_dic[i]
    
    cnt = 0
    i = 0
    print('most_freq_val = ' + str(most_freq_val))
    while i + 1 < len(a) - 1:

        if a[i] != most_freq_val and a[i + 1] != most_freq_val:
            cnt += 1
        elif a[i] == a[i + 1]:
            cnt += 1
        
        i += 2
    
    return cnt

print(solution([0,3,3,0,7,0,2,0]))
print(solution([5,2,3,3,5,3]))
print(solution([0]))

print(solution([5,2,3,3,5,3,7]))

    


    



