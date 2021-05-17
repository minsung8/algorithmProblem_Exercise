import collections

def solution(n, edges):

    dic = collections.defaultdict(list)

    for i in range(len(edges)):

        x = edges[i][0]
        y = edges[i][1]
        dic[x].append(y)
        dic[y].append(x)

    while dic:
        answer = set()
        temp = dic.keys()
        print(temp)
        for key in temp:

            if len(dic[key]) == 1:
                temp_value = dic[key].pop()
                answer.add(temp_value)
                dic[temp_value].pop( dic[temp_value].index(key) )
        print(answer)
        flag = True
        answer = list(answer)
        for i in range(len(answer)):
            
            if len(dic[ answer[i] ]) == 0:
                flag = False
        
        if flag is False:
            return answer

        
#print(solution(4, [[1, 0], [1, 2], [1, 3]]))
print(solution(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))