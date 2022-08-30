# https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true

def encryption(s):
    temp_list = []
    l = len(s)
    x = int(l ** (1/2))
    y = x + 1

    if l ** (1/2) == x:
        y -= 1
    idx = 0

    while idx < l:
        temp = s[idx:idx + y]
        temp_list.append(temp)
        idx += y

    answer = []
    for i in range(x + 2):
        temp_answer = ''
        for t in temp_list:
            if i < len(t):
                temp_answer += t[i]
        answer.append(temp_answer)
            
    return " ".join(answer)
print(encryption("haveaniceday"))    # hae and via ecy
print(encryption("feedthedog"))    # fto ehg ee dd
print(encryption("chillout"))    # clu hlt io


print(encryption('abcd'))