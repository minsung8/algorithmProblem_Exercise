# https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):
    answer = 'O' * n
    linked_list = { i : [i - 1, i + 1] for i in range(1, n - 1)}
    linked_list[n - 1] = {n - 2, None}
    linked_list[0] = {None, 1}

    for i in range(len(cmd)):

        if cmd[i][0] == "D":
            k += int(cmd[i].split(' ')[1])

        elif cmd[i][0] == "U":
            k -= int(cmd[i].split(' ')[1])

        elif cmd[i][0] == "C":
            up, down = linked_list[k]
            linked_list[up][1] = down
            linked_list[down][0] = up
            return linked_list


    return linked_list

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
#print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
