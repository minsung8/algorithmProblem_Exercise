# https://school.programmers.co.kr/learn/courses/30/lessons/92335


def solution(n, k):
    convert_n = convert_iter(n, k)

    return convert_n.split('0')


def primenumber(x):
    for i in range(2, x):	
        if x % i == 0:		
            return False
    return True

def convert_iter(num, base):
    power = 0
    tmp = ''
    while num:
        tmp = str(num%base) + tmp
        num //= base
    return tmp

	
print(solution(437674, 3))
print(solution(110011, 10))