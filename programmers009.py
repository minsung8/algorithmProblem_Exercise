def solution(play_time, adv_time, logs):

    answer_list = []

    for i in range(len(logs)):
        temp_start = logs[i].split('-')[0]
        temp_end = cal(temp_start, adv_time, '+')
        temp_answer = ''
        for j in range(len(logs)):
            temp_start2 = logs[j].split('-')[0]
            temp_end2 = logs[j].split('-')[1]

    answer = ''

    return 


def cal(t1, t2, s, multi=None):
    if s == '+':
        h1, m1, s1 = t1.split(':')
        h2, m2, s2 = t2.split(':')
        total = ((int(h1) + int(h2)) * 3600) + ((int(m1) + int(m2)) * 60) + ((int(s1) + int(s2)))

    elif s == '+':
            h1, m1, s1 = t1.split(':')
            h2, m2, s2 = t2.split(':')
            total1 = (int(h1) * 3600) + (int(m1) * 60) + (int(s1))
            total2 = (int(h2) * 3600) + (int(m2) * 60) + (int(s2))
            total = total1 - total2

    elif s == '*':
        h2, m2, s2 = t2.split(':')
        total = ((int(h2) * 3600) + (int(m2) * 60) + (int(s2))) * multi
  
    answer = ''
    if len(str(total // 3600)) == 1:
        answer += '0' + str(total // 3600) + ':'
    else:
        answer += str(total // 3600) + ':'
    temp = total % 3600
    if len(str(temp // 60)) == 1:
        answer += '0' + str(temp // 60) + ':'
    else:
        answer += str(temp // 60) + ':'
    temp = temp % 60
    if len(str(temp)) == 1:
        answer += '0' + str(temp) + ':'
    else:
        answer += str(temp)    

    return answer 



print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))