def solution(s1, s2):

    temp1 = list(s1.split('->'))
    temp2 = list(s2.split('->'))

    answer = []

    while temp1 or temp2:

        answer.append(temp1.pop(0))
        answer.append(temp2.pop(0))

    return answer


print(solution('1->2->4', '1->3->4'))