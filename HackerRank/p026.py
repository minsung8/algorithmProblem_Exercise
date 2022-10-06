# https://www.hackerrank.com/challenges/richie-rich/problem?isFullScreen=true

def highestValuePalindrome(s, n, k):
    # Write your code here

    dif_idx_list = []

    front = list(s[:n // 2])
    back = list(s[n // 2:][::-1])

    for i in range(len(front)):
        if front[i] != back[i]:
            dif_idx_list.append(i)

    if len(dif_idx_list) > k: return '-1'
    elif len(dif_idx_list) == k:
        
        for i in range(len(dif_idx_list)):
            _max = max(int(front[dif_idx_list[i]]), int(back[dif_idx_list[i]]))

            front[dif_idx_list[i]] = str(_max)
            back[dif_idx_list[i]] = str(_max)

        return "".join(front) + "".join(back[::-1])
    else:
        
        for i in range(len(dif_idx_list)):
            _max = max(int(front[dif_idx_list[i]]), int(back[dif_idx_list[i]]))

            front[dif_idx_list[i]] = str(_max)
            back[dif_idx_list[i]] = str(_max)
        
            k -= 1

        i = 0
        while k > 0:

            front[i] = '9'
            back[i] = '9'

            k -= 1
            i += 1

    return "".join(front) + "".join(back[::-1])


print(highestValuePalindrome('3943', 4, 1))   # 3993
print(highestValuePalindrome('092282', 6, 3))   # 992299    
print(highestValuePalindrome('0011', 4, 1))   # -1
