def solution(s):
    answer = []

    zero_cnt = 0
    change_cnt = 0

    while '1' != s:
        print(s)
        temp = s.count('1') * '1'
        change_cnt += 1
        zero_cnt += s.count('0')
        s = bin(len(temp))[2:]
        print(s)
    return [change_cnt, zero_cnt]

print(solution("01110"))