# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []

    for number in numbers:
        temp = list(binToString(number))[::-1]

        if '0' in temp:
            temp_idx = temp.index('0')
            temp[temp_idx] = '1'
            temp2 = "0b"+ "".join(temp)
            answer.append(int(temp2,  2))
        else:
            temp3 = ['1', '0'] + temp[1:]
            temp4 = "0b"+ "".join(temp3)
            answer.append(int(temp4,  2))

    return answer

def binToString(i):
    print(bin(i))
    return bin(i)[2:]

print(solution([3]))

