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
    while True:


        if complete_list[-1] != new_tasks[i][0] and complete_list[-2] != new_tasks[i][0]:
            complete_list.append(new_tasks[i][0])
            new_tasks[i][1] -= 1
            i += 1

        if i == len(new_tasks) - 1:
            i = 0
        
        return 


    return new_tasks

print(solution(["A", "A", "A", "B", "B", "B"], 2))
