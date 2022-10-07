# https://www.hackerrank.com/challenges/richie-rich/problem?isFullScreen=true


def highestValuePalindrome(s, n, k):
    # Write your code here

    dif_idx_list = []

    if len(s) % 2 == 0:
        front = list(s[:n // 2])
        back = list(s[n // 2:][::-1])
        mid = []
    else:
        front = list(s[:n // 2])
        back = list(s[n // 2 + 1:][::-1])
        mid = [s[n // 2]]

    for i in range(len(front)):
        if front[i] != back[i]:
            dif_idx_list.append(i)

    if len(dif_idx_list) > k: return '-1'

    elif len(dif_idx_list) == k:
        for i in range(len(dif_idx_list)):
            _max = max(int(front[dif_idx_list[i]]), int(back[dif_idx_list[i]]))
            front[dif_idx_list[i]] = str(_max)
            back[dif_idx_list[i]] = str(_max)
        
        if not mid:
            return "".join(front) + "".join(back[::-1])
        else:
            return "".join(front) + mid[0] + "".join(back[::-1])

    else:

        for i in range(len(dif_idx_list)):

            if len(dif_idx_list[i:]) < k:
                if front[dif_idx_list[i]] != '9':
                    front[dif_idx_list[i]] = '9'
                    k -= 1
                if back[dif_idx_list[i]] != '9':
                    back[dif_idx_list[i]] = '9'
                    k -= 1
            else:
                _max = max(int(front[dif_idx_list[i]]), int(back[dif_idx_list[i]]))
                front[dif_idx_list[i]] = str(_max)
                back[dif_idx_list[i]] = str(_max)
                k -= 1
        
        i = 0
        while k > 1:
            if i == len(front): break

            if front[i] != '9':
                front[i] = '9'
                k -= 1
            if back[i] != '9':
                back[i] = '9'
                k -= 1

            i += 1
    if not mid:
        return "".join(front) + "".join(back[::-1])
    else:
        if k > 0:
            mid = ['9']
        return "".join(front) + mid[0] + "".join(back[::-1])

print(highestValuePalindrome('3943', 4, 1))   # 3993
print(highestValuePalindrome('092282', 6, 3))   # 992299    
print(highestValuePalindrome('0011', 4, 1))   # -1
print(highestValuePalindrome('072282', 6, 3))   # 992299    
print(highestValuePalindrome('072272', 6, 3))   # 992299    

print(highestValuePalindrome('351', 3, 1))
# 292 282
# 292 292 1
