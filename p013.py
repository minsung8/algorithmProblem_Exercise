# https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true


def biggerIsGreater(w):
    if w == "".join(sorted(list(w), reverse=True)):
        return "no answer"

    reversed_w = w[::-1]

    # temp = []
    # for i in w:
    #     temp.append(ord(i))
    # print(temp)

    for i in range(len(reversed_w) - 1):
        for j in range(i + 1, len(reversed_w) - 1):
            if reversed_w[i] > reversed_w[j]:
                answer = ''
                for k in range(len(reversed_w)):
                    if i == k:
                        answer += reversed_w[j]
                    elif j == k:
                        answer += reversed_w[i]
                    else:
                        answer += reversed_w[k]
                answer = answer[::-1]
                return answer[:len(w) - j] + "".join(sorted(list(answer[len(w) - j:])))
    
    temp_list = []
    for i in range(1, len(w)):
        if w[0] < w[i]:
            temp_list.append(w[i])

    max_idx = w.index(min(temp_list))

    temp_w = sorted(list(w[:max_idx] + w[max_idx + 1:]))
    return "".join([w[max_idx]] + temp_w)

# 97 ~ 122

print(biggerIsGreater("ab"))  # ba
print(biggerIsGreater("bb"))  # no answer
print(biggerIsGreater("hefg"))  # hegf
print(biggerIsGreater("dhck"))  # dhkc
print(biggerIsGreater("dkhc"))  # hcdk
print(biggerIsGreater("abcd"))  # abdc
print(biggerIsGreater("a"))

print(biggerIsGreater('abdc'))  # acbd
