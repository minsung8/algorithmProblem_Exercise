def solution1(s):

    alpha_list = []

    for i in range(len(s)):
        if s[i].isalnum():
            alpha_list.append(s[i])
    
    while True:

        if len(alpha_list) < 2:
            break

        temp = alpha_list.pop(0)

        if temp == alpha_list[-1]:
            alpha_list.pop(-1)
        
        else:
            return False
        
    return True


print(solution1('a man, a plan, a canal: panama'))
print(solution1('race a car'))