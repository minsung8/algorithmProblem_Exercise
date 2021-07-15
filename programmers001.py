#https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer  = 0
    #answer = rotate(s, 2)
    for i in range(1, len(s) + 1):
        print(i)
        temp = rotate(s, i)
        if check(temp):
            answer += 1
    return answer

def rotate(s, cnt):
    front = s[:-cnt]
    back = s[-cnt:]
    return back + front

def check(s):
    
    dic = {}
    for i in range(len(s)):
        if s[i] in '[({':
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        else:
            if s[i] == '}': temp = '{'
            elif s[i] == ']': temp = '['
            elif s[i] == ')': temp = '('

            if temp not in dic:
                return False
            else:
                dic[temp] -= 1
                if dic[temp] < 0:
                    return False
    
    for x in dic.values():
        if x != 0:
            return False

    return True

print(solution("{(})"))
#print(solution("}]()[{"))
