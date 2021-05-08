def solution(s):
    
    con = {}
    con['zero'] = 0
    con['one'] = 1
    con['two'] = 2
    con['three'] = 3
    con['four'] = 4
    con['five'] = 5
    con['six'] = 6
    con['seven'] = 7
    con['eight'] = 8
    con['nine'] = 9

    answer = ''
    temp = ''
    for i in range(len(s)):

        if s[i].isdigit():
            answer += str(s[i])
        else:
            temp += s[i]

        if temp in con:
            answer += str(con[ temp ])
            temp = ''
    
    return int(answer)


print(solution('one4seveneight'))