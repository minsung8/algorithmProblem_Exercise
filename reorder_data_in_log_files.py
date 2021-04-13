def solution(logs):

    temp1_list = []
    answer_list = []

    for i in range(len(logs)):

        temp1_list.append( logs[i].split(' ') )

    ## 정렬
    temp2_list = sorted(temp1_list, key=lambda x: (x[1:], x[0]))

    ## 문자
    for i in range(len(temp2_list)):

        flag = True

        for j in range(1, len(temp2_list[i])):

            if temp2_list[i][j].isdigit():

                flag = False
        
        if flag:

            answer_list.append( temp2_list[i] )

    temp2_list = sorted(temp1_list, key=lambda x: x[0])

    ## 숫자
    for i in range(len(temp2_list)):

        flag = True

        for j in range(1, len(temp2_list[i])):

            if temp2_list[i][j].isdigit() == False:

                flag = False
        
        if flag:

            answer_list.append( temp2_list[i] )
    

    answer = []
    # answer
    for i in range(len(answer_list)):
        temp_s = ''
        for j in range(len(answer_list[i])):
            temp_s += answer_list[i][j]
            if j != len(answer_list[i]) - 1:
                temp_s += ' '
        answer.append(temp_s)
        
    return answer


print(solution(['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dog', 'let3 art zero']))