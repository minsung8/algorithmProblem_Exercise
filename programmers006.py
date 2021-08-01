# https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):

    answer = ['O'] * n
    linked_list = { i : [i - 1, i + 1] for i in range(1, n + 1)}
    linked_list[0] = [0, 1]
    delete_list = []

    for i in range(len(cmd)):
        if cmd[i][0] == "D":
            for j in range(int(cmd[i][2:])):
                k = linked_list[k][1]

        elif cmd[i][0] == "U":
            for j in range(int(cmd[i][2:])):
                k = linked_list[k][0]

        elif cmd[i][0] == "C":
            print (linked_list, k)
            up, down = linked_list[k]
            delete_list.append(k)

            if down == n + 1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if up == 0:
                linked_list[down][0] = up
            elif down == n + 1:
                linked_list[up][1] = down
            else:
                linked_list[down][0] = up
                linked_list[up][1] = down


        elif cmd[i][0] == "Z":
            temp = delete_list.pop(-1)
            up, down = linked_list[temp]
            if up == 0:
                linked_list[down][0] = temp
            elif down == n + 1:
                linked_list[up][1] = temp
            else:
                linked_list[down][0] = temp
                linked_list[up][1] = temp
            
    for i in range(len(delete_list)):
        answer[delete_list[i]] = 'X'

    return "".join(answer)

print(solution(8, 0, ["C"]))
#print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
