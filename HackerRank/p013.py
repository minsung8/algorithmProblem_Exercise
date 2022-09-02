# https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true
from collections import defaultdict

def biggerIsGreater(w):

    dic = defaultdict(list)
    flag = False
    for i in reversed(range(len(w))):
        for j in range(i):
            if w[i] > w[j]:
                dic[i].append([j, w[j]])
                flag = True
        if flag: break

    answer_idx = None
    answer = None
    temp_list2 = []
    temp3_str = ''
    for k in dic.keys():
        temp_list = sorted(dic[k], key=lambda x : x[1], reverse=False)
        print(temp_list)
        answer_idx = temp_list[0][0]
        answer = w[k]
    
        for i in range(answer_idx, len(w)):
            if k != i:
                temp_list2.append(w[i])
        temp3_str = w[:answer_idx]
    if not temp_list2: return "no answer"

    answer2 = temp3_str
    temp_list2.sort()

    while temp_list2:
        if len(answer2) == answer_idx:
            answer2 += answer
        elif temp_list2:
            answer2 += temp_list2.pop(0)

    return answer2

# 97 ~ 122

# print(biggerIsGreater("ab"))  # ba
# print(biggerIsGreater("bb"))  # no answer

print(biggerIsGreater("hefg"))  # hegf
print(biggerIsGreater("dhck"))  # dhkc

# print(biggerIsGreater("dkhc"))  # hcdk
# print(biggerIsGreater("abcd"))  # abdc
# print(biggerIsGreater("a"))

# print(biggerIsGreater('abdc'))  # acbd
