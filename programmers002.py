# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []

    for number in numbers:
        temp = number
        start = number + 1

        if temp % 2 == 0:
            answer.append(temp + 1)
        
        elif '0' not in bin(temp)[2:]:
            temp2 = ['1', '0'] + list(bin(temp)[3:])
            answer.append(int('0b' + "".join(temp2), 2))
        
        else:
            while True:
                if check(temp, start).count('1') == 1 or  check(temp, start).count('1') == 2:
                    answer.append(start)
                    break
                start += 1

    return answer

def check(a, b):
    return bin(a ^ b)

print(solution([7]))
