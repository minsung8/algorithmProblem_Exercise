def solution():

    dic = {}
    dic[2] = "abc"
    dic[3] = "def"

    answer = []

    for x in dic[2]:
        for y in dic[3]:
            answer.append(x + y)
    return answer


print(solution())