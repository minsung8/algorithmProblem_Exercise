# https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):

    answer = list('OOOOOOOO')
    delete_list = []
    for i in range(len(cmd)):
        if cmd[i][0] == 'D':
            temp_cnt = int(cmd[i].split(' ')[1])
            for j in range(k + 1, len(answer)):
                if answer[j] == 'O':
                    temp_cnt -= 1
                if temp_cnt == 0:
                    k = j
                    break

        elif cmd[i][0] == 'U':
            temp_cnt = int(cmd[i].split(' ')[1])
            for j in range(k - 1, -1, -1):
                if answer[j] == 'O':
                    temp_cnt -= 1
                if temp_cnt == 0:
                    k = j
                    break

        elif cmd[i][0] == 'C':
            answer[k] = 'X'
            delete_list.append(k)
            k += 1
            if k > len(answer) - 1 or 'O' not in answer[k:]:
                for j in range(len(answer)):
                    if answer[j] == 'O':
                        k = j

        elif cmd[i][0] == 'Z':
            temp_idx = delete_list.pop(-1)
            answer[temp_idx] = 'O'

    return "".join(answer)


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
