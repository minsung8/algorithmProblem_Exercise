# https://school.programmers.co.kr/learn/courses/30/lessons/92335


import math

def solution(n, k):
    convert_n = convert_iter(n, k)
    temp = convert_n.split('0')
    answer = 0

    if len(temp) == 1:
        if len(temp[0]) > 0 and primenumber(int(temp[0])): return 1
        else: return 0

    for i in range(len(temp)):
        if len(temp[i]) > 0 and primenumber(int(temp[i])):
            answer += 1

    return answer

def primenumber(x):
    if x == 1 or x == 0: return False
    for i in range(2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
            return False
    return True		

def convert_iter(num, base):
    tmp = ''
    while num:
        tmp = str(num%base) + tmp
        num //= base
    return tmp

	
print(solution(437674, 3))
print(solution(110011, 10))
print(solution(304, 10))
print(solution(0, 10))