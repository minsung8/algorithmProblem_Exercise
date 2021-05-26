def solution(n_list):
    
    x = 0
    y = 1

    while True:
        if int(str(n_list[x]) + str(n_list[y])) < int(str(n_list[y]) + str(n_list[x])):
            temp = n_list[y]
            n_list[y] = n_list[x]
            n_list[x] = temp
        
        y += 1

        if y == len(n_list):
            x += 1
            y = x + 1
        
        if x == len(n_list) - 1:
            break

    answer = ''
    for i in n_list:
        answer += str(i)
    return answer

print(solution([3, 30, 34, 5, 9]))
print(solution([10, 2]))