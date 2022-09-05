# https://www.hackerrank.com/challenges/the-grid-search/problem?isFullScreen=true


def gridSearch(G, P):

    start = P[0]
    _len = len(start)

    for i in range(len(G)):

        for j in range(len(G[i]) - _len + 1):
            if G[i][j:j + _len] == start:
                idx = 1

                for k in range(1, len(P)):
                    if i + idx == len(G): break

                    if P[k] != G[i + idx][j:j + _len]:
                        break
                    idx += 1
                
                if idx == len(P): return "YES"
            
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
"96241080534811",
"445893523733475",
"768700303214199",
"650629270887191",
],
["99", "99"]))
