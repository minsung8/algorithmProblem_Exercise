# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true

from itertools import combinations
        
        
def sherlockAndAnagrams(s):
    # Write your code here
    cnt = 0
    s = list(s)

    for i in range(len(s) - 1):
        for j in range(len(s) - i):
            temp = s[j:j + i + 1]

            for k in range(j + 1, len(s)):
                if sorted(temp) == sorted(s[k:k + i + 1]):
                    cnt += 1
    return cnt

print(sherlockAndAnagrams('abba'))  # 4
print(sherlockAndAnagrams('abcd'))  # 0


# a b b a
# ab ab aa bb ba ba
