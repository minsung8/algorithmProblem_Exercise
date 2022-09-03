# https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true

def biggerIsGreater(w):

    s = list(w[::-1])

    for i in range(1, len(s)):
        if s[i - 1] > s[i]:
            for j in range(i):
                if s[j] > s[i]:
                    print(j)
                    s[j],s[i] = s[i],s[j]
                    s = sorted(s[:i])[::-1] + s[i:]
                    return "".join(s[::-1])
    
    return "no answer"


# 97 ~ 122

# print(biggerIsGreater("ab"))  # ba
# print(biggerIsGreater("bb"))  # no answer

# print(biggerIsGreater("hefg"))  # hegf
# print(biggerIsGreater("dhck"))  # dhkc

print(biggerIsGreater("dkhc"))  # hcdk
# print(biggerIsGreater("abcd"))  # abdc
# print(biggerIsGreater("a"))

# print(biggerIsGreater('abdc'))  # acbd
