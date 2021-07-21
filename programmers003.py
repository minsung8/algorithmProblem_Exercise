# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = [[] for i in range(n)]


    start = 1
    i = 0
    j = 0
    
    right = False
    bot = False
    left = True
    start_idx = 0
    end_idx = n

    while start_idx <= end_idx:

        if left:
            for x in range(start_idx, end_idx):
                if len(answer[x]) == 0:
                    answer[x] = [start] + answer[x]
                else:
                    answer[x] = answer[x][:-1] + [start] + [answer[x][-1]]
                start += 1
            left = False
            bot = True
            start_idx += 1
        if bot:
            for x in range(start_idx, end_idx):
                if end_idx == n:
                    answer[end_idx - 1].append(start)
                else:
                    answer[end_idx - 1] = answer[end_idx - 1][:-1] + [start] + [answer[end_idx - 1][-1]]
                start += 1
            bot = False
            right = True
            end_idx -= 1

        if right:
            for x in range(end_idx - 1, start_idx - 1, -1):
                if end_idx == n - 1:
                    answer[x] = answer[x] + [start]
                else:
                    answer[x] = answer[x][:-1] + [start] + [answer[x][-1]]
                start += 1
            right = False
            left = True
            start_idx += 1
    print(answer)
    result = []
    for i in range(len(answer)):
        result += answer[i]
    return result

print(solution(8))
