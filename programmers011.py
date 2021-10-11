from collections import defaultdict

def solution(s):

    dic = defaultdict(list)

    for x in s:
        start = x
        i = 0
        while True:
            if i == len(start) - 2:
                break

            if start[i:i+3] == '110':
                temp_str = start[:i] + start[i+3:]

                dic[start].append(start)
                for j in range(len(temp_str)):
                    temp_str2 = temp_str[:j] + '110' + temp_str[j:]
                    dic[start].append(temp_str2)
                dic[start].append(temp_str + '110')

            i += 1
    answer = []
    for key in dic.keys():
        temp_list = dic[key]
        answer.append(sorted(temp_list)[0])

    return answer

print(solution(["1110","100111100","0111111010"]))
