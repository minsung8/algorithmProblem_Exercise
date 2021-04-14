def solutuon(s):
    answer = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            temp = s[i:j]

            if check(temp):

                if len(answer) < len(temp):
                    answer = temp
            
    return answer


def check(s):
    if s == s[::-1]:
        return True
    else:
        return False 

print( solutuon("abcdcba") )
print( solutuon("abacde") )
