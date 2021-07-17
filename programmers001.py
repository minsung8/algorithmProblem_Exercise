#https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer  = 0
    #answer = rotate(s, 2)
    for i in range(1, len(s) + 1):
        temp = rotate(s, i)
        if check(temp):
            answer += 1
    return answer

def rotate(s, cnt):
    front = s[:-cnt]
    back = s[-cnt:]
    return back + front

def check(s):

    temp = ''

    for i in range(len(s)):
        if s[i] in '{[(':
            temp += s[i]
        elif temp != '':
            if s[i] == '}':
                if temp[-1] == '{':
                    temp = temp[:-1]
                else:
                    return False
            elif s[i] == ']':
                if temp[-1] == '[':
                    temp = temp[:-1]
                else:
                    return False
            elif s[i] == ')':
                if temp[-1] == '(':
                    temp = temp[:-1]
                else:
                    return False
        else:
            return False
    return True
    

#print(solution("{(})"))
#print(solution("}]()[{"))
#print(solution("}]()[{"))
print(check('[{}]()'))