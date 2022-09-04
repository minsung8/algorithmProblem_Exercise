# https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true


def gridSearch(G, P):

    start = P[0]
    idx = 1
    for i in range(len(G)):

        if start in G[i]:
            
            start_idx = G[i].index(start)
            cnt = 1
            for j in range(i + 1, len(G)):
                if P[idx] != G[j][start_idx:start_idx + len(start)]:
                    flag = False
                    break
                cnt += 1
                idx += 1

                if idx == len(P):
                    break

            if cnt == len(P):
                return "YES"
            else: idx = 1
            
    return "NO"

print(gridSearch(['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137'],
                    ['9505', '3845', "3530"]))

print(gridSearch([
"400453592126560",
"114213133098692",
"474386082879648",
"522356951180169",
"887109450487496",
"252802633388782",
"502771484966748",
"075975207693780",
"511799789562806",
"404007454272504",
"549043809916080",
"962410801534811",
"445893523733475",
"768795303214174",
"650629270887160",
],
["9", "9"]))
