# https://www.hackerrank.com/challenges/common-child/problem?isFullScreen=true


from re import I


def commonChild(s1, s2):
    # Write your code here

    start_list = []
    for i in range(len(s1)):
        if s1[i] in s2:
            start_list.append(i)

    answer_list = []
    for i in start_list:    
        temp_answer = ''
        visited = [0] * len(s2)

        for j in range(i, len(s1)):
            
            for k in range(len(s2)):

                if s1[j] == s2[k] and visited[k] == 0:
                    temp_answer += s1[j]
                    visited[k] = 1
                    break

        answer_list.append(temp_answer)
    
    return answer_list





print(commonChild('SHINCHAN', 'NOHARAAA'))    # 3   NHA


print(commonChild('HARRY', 'SALLY'))    # 2

print(commonChild('AA', 'BB'))    # 0
print(commonChild('OUDFRMYMAW', 'AWHYFCCMQX'))    # 2
