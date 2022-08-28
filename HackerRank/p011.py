# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=true

def organizingContainers(container):

    c_dic = {}
    len_dic = {}
    for c in container:

        for j in range(len(c)):

            if j in c_dic:
                c_dic[j] += c[j]
            else:
                c_dic[j] = c[j]
        
        if sum(c) in len_dic:
            len_dic[sum(c)] += 1
        else:
            len_dic[sum(c)] = 1

    print(c_dic, len_dic)

    for key in c_dic.keys():
        flag = False
        for l in len_dic:
            if c_dic[key] == l and len_dic[l] > 0:
                flag = True
                len_dic[l] -= 1
                break    
            
            elif c_dic[key] == len_dic[l] * l:
                flag = True
                len_dic[l] -= 1
                break
        
        if not flag:
            return "Impossible"
    
    return "Possible"



print(organizingContainers([[1, 1], [1, 1]]))
print(organizingContainers([[0, 2], [1, 1]]))

print(organizingContainers([[1, 3, 1], [2, 1, 2], [3, 3, 3]]))
print(organizingContainers([[0, 2, 1], [1, 1, 1], [2, 0, 0]]))
