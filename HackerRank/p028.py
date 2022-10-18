# https://www.hackerrank.com/challenges/common-child/problem?isFullScreen=true

def commonChild(s1, s2):
    L = [0] * len(s2)
    for c in s1:
        p = 0
        L = [
            p := (q+1 if c==d else r if p < r else p)
            for d, q, r in zip(s2, [0]+L, L)
        ]
    return L[-1]


print(commonChild('SHINCHAN', 'NOHARAAA'))    # 3   NHA

# print(commonChild('HARRY', 'SALLYA'))    # 2

# print(commonChild('AA', 'BB'))    # 0

# print(commonChild('OUDFRMYMAW', 'AWHYFCCMQX'))    # 2

# print(commonChild('ABCDEF', 'FBDAMN'))

# print(commonChild('WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS', 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'))

# # SHINCHAN
# NOHARAAA

# S 0000 0000
# N 0011 1111
#  
#  NNNNNNNN
# 
