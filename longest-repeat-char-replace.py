def solution(s, k):

    key_list = []
    temp_list = []

    for i in s:

        if i not in key_list:
            key_list.append(i)
            temp_list.append(s.count(i))

    if len(s) <= max(temp_list) + k:
        return len(s)
    return max(temp_list) + k

print(solution("AAABBBBBBC", 2))