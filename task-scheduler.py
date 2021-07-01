def solution(tasks, n):
    new_tasks = []
    tasks.sort()

    for task in tasks:

        if len(new_tasks) == 0:
            new_tasks.append([task, 1])
        
        elif new_tasks[-1][0] == task:
            new_tasks[-1][1] += 1
        
        elif new_tasks[-1][0] != task:
            new_tasks.append([task, 1])

    complete_list = []
    i = 0
    while new_tasks:
        print(complete_list, new_tasks)
        print(complete_list[-n:], new_tasks[i][0])
        if len(complete_list) < n:
            complete_list.append(new_tasks[i][0])
            new_tasks[i][1] -= 1
        elif new_tasks[i][0] not in complete_list[-n:]:
            complete_list.append(new_tasks[i][0])
            new_tasks[i][1] -= 1
        else:
            complete_list.append('idle')
            i -= 1

        if new_tasks[i][1] == 0:
            new_tasks.pop(i)
        else:
            i += 1

        if i == len(new_tasks):
            i = 0
        
        if len(complete_list) != 0 and (len(complete_list) + 1)% n == 0 and i != 0:
            i = 0

    return complete_list

print(solution(["A", "A", "A", "B", "C", "D"], 2))
