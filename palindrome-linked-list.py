def solution1(s):

    temp_list = list(s.split('->'))

    while temp_list:

        head = temp_list.pop(0)
        tail = temp_list.pop(-1)

        if head != tail:
            return False

    return True

def solution2(s):

    temp_list = list(s.split('->'))


    return False

print(solution('1->2'))
print(solution('1->2->2->1'))