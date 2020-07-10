def solution(lines):
    cnt = []
    answer_list = []
    for i in lines:
        temp = i.split(" ")
        temp2 = temp[1].split(':')
        end_time = (3600 * float(temp2[0])) + (60 * float(temp2[1])) + float(temp2[2])
        start_time = round((end_time - float(temp[2][:-1]) + 0.001), 3)
        answer_list.append([start_time, end_time])
    for i in answer_list:
        temp_start = i[1]
        temp_end = round((i[1] + 0.999), 3)
        temp_cnt = 0
        for j in answer_list:
            if not (temp_end < j[0] or temp_start > j[1]):
                temp_cnt += 1
        cnt.append(temp_cnt)
    return max(cnt)
