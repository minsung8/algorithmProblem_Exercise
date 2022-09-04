# https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true

def biggerIsGreater(w):

    reversed_w = list(w[::-1])

    for i in range(1, len(reversed_w)):
        if reversed_w[i - 1] > reversed_w[i]:
            for j in range(i):
                if reversed_w[j] > reversed_w[i]:
                    reversed_w[i], reversed_w[j] = reversed_w[j], reversed_w[i]
                    answer = reversed_w[::-1]
                    return "".join(answer[:len(w) - i] + sorted(answer[len(w) - i:]))

    return

# print(biggerIsGreater("ab"))  # ba
# print(biggerIsGreater("bb"))  # no answer

print(biggerIsGreater("hefg"))  # hegf
print(biggerIsGreater("dhck"))  # dhkc

print(biggerIsGreater("dkhc"))  # hcdk
print(biggerIsGreater("abcd"))  # abdc
# print(biggerIsGreater("a"))

print(biggerIsGreater('abdc'))  # acbd

# chkd -> cdkh