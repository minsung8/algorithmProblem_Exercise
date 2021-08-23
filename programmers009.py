def solution(play_time, adv_time, logs):

    if play_time == adv_time:
        return "00:00:00"

    answer_list = []

    for i in range(len(logs)):
        temp_start = logs[i].split('-')[0]
        temp_end = cal(temp_start, adv_time, '+')
        answer_list.append([temp_start, temp_end])

    for i in range(len(answer_list)):
        temp_score = 0
        for j in range(len(logs)):
            temp_score += cal2(logs[j], answer_list[i])

        answer_list[i].append(temp_score)

    answer_list = sorted(answer_list, key=lambda x: (-x[2], x[0]))

    return answer_list[0][0]

def cal(t1, t2, s, multi=None):
    if s == '+':
        h1, m1, s1 = t1.split(':')
        h2, m2, s2 = t2.split(':')
        total = ((int(h1) + int(h2)) * 3600) + ((int(m1) + int(m2)) * 60) + ((int(s1) + int(s2)))

    elif s == '-':
            h1, m1, s1 = t1.split(':')
            h2, m2, s2 = t2.split(':')
            total1 = (int(h1) * 3600) + (int(m1) * 60) + (int(s1))
            total2 = (int(h2) * 3600) + (int(m2) * 60) + (int(s2))
            total = total1 - total2
            return total

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
        answer += '0' + str(temp)
    else:
        answer += str(temp)    

    return answer 

def cal2(log, adv_time): #[]
    log_start, log_end = log.split('-')
    adv_start, adv_end = adv_time[0], adv_time[1]

    if log_end <= adv_start or log_start >= adv_end:
        return 0
    return cal(min(log_end, adv_end), max(log_start, adv_start), '-')

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
