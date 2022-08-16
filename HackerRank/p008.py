# https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true

def simpleArraySum(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i

    return answer

print(simpleArraySum(25))     # 15511210043330985984000000
