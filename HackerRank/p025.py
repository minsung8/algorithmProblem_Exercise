# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true


def isValid(s):
    # Write your code here

    dic = {}
    cnt_list = []
    for i in range(len(s)):

        if not dic.get(s[i]): dic[s[i]] = 1
        else: dic[s[i]] += 1

        cnt_list.append(s.count(s[i]))
    temp_list = []

    for i in s:
        if [i, dic[i], cnt_list.count(dic[i])] not in temp_list:
            temp_list.append([i, dic[i], cnt_list.count(dic[i])])
    _max_list = sorted(temp_list, key=lambda x: x[2], reverse=True)[0]
    flag = True

    for i in range(len(temp_list)):
        
        if temp_list[i][1] == _max_list[1]: continue
        else:
            
            if flag and abs(temp_list[i][1] - _max_list[1]) == 1:
                flag = False
                continue
            else:
                return 'NO'

    if flag and temp_list[0][1] != 1:
        return 'NO'

    return "YES"


print(isValid('aabbcd'))    # no
print(isValid('aabbccddeefghi'))    # no
print(isValid('abcdefghhgfedecba'))    # yes

print(isValid('aaaaabc'))   # no

print(isValid('aabbcc'))  # no
