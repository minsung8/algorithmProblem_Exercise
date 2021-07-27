# https://programmers.co.kr/learn/courses/30/lessons/81303
from collections import defaultdict

def solution(n, k, cmd):

    answer = list('O' * n)
    dic = {}
    delete_list = []
    dic = defaultdict(list)
    dic[0] = [None, 1]
    dic[n - 1] = [n - 2, None]
    for i in range(1, n-1):
        dic[i] = [i - 1, i + 1]
    
    return dic
    for i in range(len(cmd)):
        if cmd[i][0] == 'D':
            temp_cnt = int(cmd[i].split(' ')[1])
            k = current_list[current_list.index(k) + temp_cnt]

        elif cmd[i][0] == 'U':
            temp_cnt = int(cmd[i].split(' ')[1])
            k = current_list[current_list.index(k) - temp_cnt]

        elif cmd[i][0] == 'C':
            delete_list.append(k)

            if k == len(answer) - 1:
                temp = k
                k = current_list[current_list.index(k) - 1]
                current_list.pop(current_list.index(temp))

            else:
                temp = k
                k = current_list[current_list.index(k) + 1]
                current_list.pop(current_list.index(temp))

        elif cmd[i][0] == 'Z':
            temp_idx = delete_list.pop(-1)
            current_list.append(temp_idx)

    result = ''
    for i in range(len(answer)):
        if i in current_list:
            result += 'O'
        else:
            result += 'X'

    return result

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
