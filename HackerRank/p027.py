# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true
        
        
def sherlockAndAnagrams(s):
    # Write your code here
    cnt = 0
    s = list(s)

    dic = {}

    for i in range(len(s) - 1):
        for j in range(len(s) - i):
            temp = s[j:j + i + 1]
            temp_key = "".join(temp)
            if not dic.get(temp_key):
                dic[temp_key] = "".join(sorted(temp))
    
    for i in range(len(s) - 1):
        for j in range(len(s) - i):
            temp_key = "".join(s[j:j + i + 1])

            for k in range(j + 1, len(s)):
                if dic[temp_key] == dic["".join(s[k:k + i + 1])]:
                    cnt += 1
    return cnt

print(sherlockAndAnagrams('abba'))  # 4
print(sherlockAndAnagrams('abcd'))  # 0


