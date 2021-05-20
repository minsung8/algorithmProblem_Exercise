from collections import defaultdict

def solution(n, edges):
    
    point = []

    for i in range(n):
        point.append(i + 1)

    while True:

        dic = defaultdict(list)

        for i in range(len(edges)):
            x = edges[i][0]
            y = edges[i][1]

            dic[x].append(y)
            dic[y].append(x)

        temp = []
        
        for key in dic.keys():
            
            if len( dic[key] ) == 1:
                temp.append([key, dic[key][0]])
                point.pop( point.index(key) )

        while temp:
            start = temp.pop(0)

            if start in edges:
                edges.pop( edges.index(start) )
            else:
                start.reverse()
                edges.pop( edges.index( start ) )
        
        if len(edges) < 2:
            return point
    
    return 


        
#print(solution(4, [[1, 0], [1, 2], [1, 3]]))
#print(solution(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
print( solution(10, [[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9]]) )