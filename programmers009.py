def solution(play_time, adv_time, logs):
    
    answer_list = []

    for i in range(len(logs)):
        temp_start = logs[i].split('-')[0]
        temp_end = plus(temp_start, adv_time)
        if temp_end <= play_time and len(temp_end) == 8:
            answer_list.append([temp_start, temp_end])
    
    if not answer_list:
        return "00:00:00"
    return answer_list


def plus(t1, t2):
    h1, m1, s1 = t1.split(':')
    h2, m2, s2 = t2.split(':')
    temp_answer = int(h1) * 3600 + int(m1) * 60 + int(s1) + int(h2) * 3600 + int(m2) * 60 + int(s2)
    answer = ""
    temp_h = str(temp_answer // 3600)
    if len(temp_h) == 1:
        temp_h = '0' + temp_h
    temp_answer = temp_answer % 3600
    temp_m = str(temp_answer // 60)
    if len(temp_m) == 1:
        temp_m= '0' + temp_m
    temp_answer = temp_answer % 60
    temp_s = str(temp_answer)
    if len(temp_s) == 1:
        temp_s= '0' + temp_s

    return temp_h + ":" + temp_m + ":" + temp_s



print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
