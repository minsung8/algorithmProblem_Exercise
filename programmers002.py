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
            reverse_temp2 = list(reversed(bin(temp)[2:]))
            zero_idx = reverse_temp2.index('0') + 1
            temp2 = list(bin(temp)[2:])
            temp2[-zero_idx] = '1'
            temp2[-zero_idx + 1] = '0'
            answer.append(int('0b' + ''.join(temp2), 2))
    return answer


print(solution([11]))
