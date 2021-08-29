from collections import defaultdict

def solution(play_time, adv_time, logs):
    logs = sorted(logs)
    answer_dic = defaultdict(list)
    answer_dic[minute('00:00:00')] = [minute(adv_time), 0]
    answer_dic[minute(play_time) - minute(adv_time)] = [minute(play_time), len(logs) - 1]

    for i in range(len(logs)):
        temp_start, temp_end = logs[i].split('-')
        if minute(temp_start) + minute(adv_time) <= minute(play_time):
            answer_dic[minute(temp_start)] = [minute(temp_start) + minute(adv_time), i]
        if minute(temp_end) - minute(adv_time) >= 0:
            answer_dic[minute(temp_end) - minute(adv_time)] = [minute(temp_end), i]
    temp_list = sorted(list(answer_dic.keys()))
    answer_list = []
    answer = []
    answer_time = 0
    for key in temp_list:
        time = 0
        end_key = answer_dic[key][0]
        for i in range(answer_dic[key][1] - 1, len(logs)):

            temp_start, temp_end = logs[i].split('-')

            if minute(temp_start) >= end_key:
                break
            temp_time = min(end_key, minute(temp_end)) - max(key, minute(temp_start))
            if temp_time > 0:
                time += temp_time
        if not answer or answer_time < time:
            answer = [key, time]
            answer_time = time
    return sec_to_str(answer[0])
 
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
