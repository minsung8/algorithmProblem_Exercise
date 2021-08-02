# https://programmers.co.kr/learn/courses/30/lessons/81303

def solution(n, k, cmd):

    linked_list = { i : [i - 1, i + 1] for i in range(1, n - 1)}
    linked_list[n - 1] = [n - 2, n]
    linked_list[0] = [-1, 1]
    answer = ["O" for i in range(n)]
    delete_list = []

    for i in range(len(cmd)):
        if cmd[i][0] == "D":
            for j in range(int(cmd[i][2:])):
                k = linked_list[k][1]

        elif cmd[i][0] == "U":
            for j in range(int(cmd[i][2:])):
                k = linked_list[k][0]

        elif cmd[i][0] == "C":
            up, down = linked_list[k]
            delete_list.append([up, down, k])
            answer[k] = "X"

            if down == n:
                k = up
            else:
                k = down

            if up == -1:
                linked_list[down][0] = up
            elif down == n:
                linked_list[up][1] = down
            else:
                linked_list[down][0] = up
                linked_list[up][1] = down

        elif cmd[i][0] == "Z":
            up, down, now = delete_list.pop(-1)
            answer[now] = "O"

            if up == -1:
                linked_list[down][0] = now
            elif down == n:
                linked_list[up][1] = now
            else:
                linked_list[down][0] = now
                linked_list[up][1] = now

    return "".join(answer)

print(solution(8, 0, ["C"]))

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
