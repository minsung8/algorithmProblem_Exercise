def solution(play_time, adv_time, logs):

    play_list = [0 for i in range(str_to_sec(play_time) + 1)]

    for log in logs:
        temp_start, temp_end = log.split('-')
        play_list[str_to_sec(temp_start)] += 1
        play_list[str_to_sec(temp_end)] -= 1

    for i in range(1, len(play_list)):
        play_list[i] += play_list[i - 1]
    for i in range(1, len(play_list)):
        play_list[i] += play_list[i - 1]
    
    answer = 0
    answer_score = play_list[str_to_sec(adv_time)] - play_list[0]
    logs = sorted(logs)

    for i in range(len(play_list)):
        
        if i + str_to_sec(adv_time) <= str_to_sec(play_time) and \
            answer_score < play_list[i + str_to_sec(adv_time)] - play_list[i]:
            answer = i + 1
            answer_score = play_list[i + str_to_sec(adv_time)] - play_list[i]
        
        if i >= str_to_sec(adv_time) and \
            answer_score < play_list[i] - play_list[i - str_to_sec(adv_time)]:
            answer = i - str_to_sec(adv_time) + 1
            answer_score = play_list[i] - play_list[i - str_to_sec(adv_time)]

    return sec_to_str(answer)

def str_to_sec(s):
    hour, minute, sec = s.split(':')
    return (int(hour) * 3600) + (int(minute) * 60) + (int(sec))

def sec_to_str(t):
    hour = str(t // 3600)
    t = t % 3600
    if len(hour) == 1:
        hour = '0' + hour
    minute = str(t // 60)
    t = t % 60
    if len(minute) == 1:
        minute = '0' + minute
    sec = str(t)
    if len(sec) == 1:
        sec = '0' + sec
    return hour + ':' + minute + ':' + sec

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
