# https://www.hackerrank.com/challenges/common-child/problem?isFullScreen=true

def commonChild(s1, s2):
    # Write your code here

    s1_len = len(s1)
    s2_len = len(s2)
    m = [[0 for _ in range(s2_len + 1)] for _ in range(s1_len + 1)]


    for i in range(1, s1_len+1):
        for j in range(1, s2_len+1):
            
            if s1[i-1] == s2[j-1]:
                m[i][j] =  m[i-1][j-1] + 1
            else:
                m[i][j] = max(m[i-1][j], m[i][j-1])


    return m[-1][-1]



print(commonChild('SHINCHAN', 'NOHARAAA'))    # 3   NHA


print(commonChild('HARRY', 'SALLY'))    # 2

print(commonChild('AA', 'BB'))    # 0
print(commonChild('OUDFRMYMAW', 'AWHYFCCMQX'))    # 2

print(commonChild('ABCDEF', 'FBDAMN'))

print(commonChild('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS', 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'))
