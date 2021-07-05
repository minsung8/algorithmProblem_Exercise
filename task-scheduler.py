def solution(tasks, n):
    
    new_tasks = []

    for task in set(tasks):
        new_tasks.append([task, tasks.count(task)])
    new_tasks = sorted(new_tasks, key=lambda x: x[1], reverse=True)

    answer = []
    i = 0

    while True:
        if new_tasks[i][0] not in answer[-n:]:
            answer.append(new_tasks[i][0])
            new_tasks[i][1] -= 1
        else:
            answer.append('idle')

        if new_tasks[i][1] == 0:
            new_tasks.pop(i)
            i -= 1
        i += 1

        if not new_tasks:
            break

        if len(answer) != 0 and len(answer) % n == 0 and answer[-1] != new_tasks[0][0]:
            if new_tasks[0][0] in answer[-2:]:
                answer.append('idle')
            i = 0

        if i == len(new_tasks):
            i = 0

    return len(answer)

print(solution(["A", "A", "A", "B", "C", "D"], 2))
print(solution(["A", "A", "A", "B", "B", "B"], 2))
print(solution(["A", "A", "A"], 2))


