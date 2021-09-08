def solution(play_time, adv_time, logs):
    play_list = [0] * (minute(play_time) + 1)

    for log in logs:
        temp_start, temp_end = log.split('-')
        play_list[minute(temp_start)] += 1
        play_list[minute(temp_end)] -= 1
    
    for i in range(1, len(play_list)):
        play_list[i] += play_list[i - 1]
    
    for i in range(1, len(play_list)):
        play_list[i] += play_list[i - 1]

    logs = sorted(logs)

    answer = 0
    answer_score = play_list[minute(adv_time)] - play_list[0]

    for i in range(1, len(play_list)):
        if i + minute(adv_time) <= minute(play_time) and \
            answer_score < play_list[i + minute(adv_time)] - play_list[i]:
            answer = i + 1
            answer_score = play_list[i + minute(adv_time)] - play_list[i]

    return sec_to_str(answer)


def minute(t):
    h1, m1, s1 = t.split(':')
    return int(h1) * 3600 + int(m1) * 60 + int(s1)


def sec_to_str(s):
    answer = ''
    temp = str(int(s) // 3600)
    if len(str(temp)) == 1:
        temp = '0' + str(temp)
    answer += str(temp) + ':'
    s = int(s) % 3600

    temp = str(int(s) // 60)
    if len(str(temp)) == 1:
        temp = '0' + str(temp)
    answer += str(temp) + ':'
    s = int(s) % 60

    temp = int(s)
    if len(str(temp)) == 1:
        temp = '0' + str(temp)
    answer += str(temp)
    return answer

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
