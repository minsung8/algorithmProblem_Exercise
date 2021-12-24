from collections import defaultdict

def solution(a, b, g, s, w, t):

    dic = defaultdict(list)

    for i in range(len(g)):
        dic[i].append(g[i])
        dic[i].append(s[i])
        dic[i].append(w[i])
        dic[i].append(t[i])

    dic = sorted(dic, key=lambda x: dic[x][2] // dic[x][3], reverse=True)
    return dic

#print(solution(10, 10, [100], [100], [7], [10]))        #10
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))        #10
