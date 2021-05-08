def solution(places):

    answer =[]

    for i in range(len(places)):

        answer.append(check(places[i]))
    
    return answer

def check(temp):

    for i in range(len(temp)):

        for j in range(len(temp[i])):   ## POOOP

            if temp[i][j] == 'P':

                if i + 1 < len(temp) and temp[i + 1][j] == 'P':
                    return 0
                
                if j + 1 < len(temp[i]) and temp[i][j + 1] == 'P':
                    return 0
                
                if (i + 1 < len(temp) and j + 1 < len(temp[i]))  and temp[i + 1][j + 1] == 'P' and ( temp[i + 1][j] == 'O' or temp[i][j + 1] == 'O'):
                    return 0

                if (j - 1 >= 0 and i + 1 < len(temp)) and (temp[i + 1][j - 1] == 'P') and ( temp[i][j-1] == 'O' or temp[i-1][j] == 'O'):
                    return 0
                
                if j + 2 < len(temp[i]) and temp[i][j + 1] == 'O' and temp[i][j + 2] == 'P':
                    return 0

                if i + 2 < len(temp) and temp[i + 1][j] == 'O' and temp[i + 2][j] == 'P':
                    return 0

    return 1

