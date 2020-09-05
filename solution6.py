# 프로그래머스 : https://programmers.co.kr/learn/courses/30/lessons/60060

class Node:
    def __init__(self, w = ""):
        self.word = w
        self.cList = {}         ## 자식노드 저장
        self.length = len(w)        ## 마지막 노드에 그 단어 길이 저장

class Tree:
    def __init__(self):
        self.root = Node("")
        self.keyList = {}           ## 각 단어와 길이 dictionary로 저장

    def create(self,  words, reverse=False):
        for word in words:
            if word not in self.keyList:
                self.keyList[word] = len(word)
                cur_node = self.root
                for w in word:
                    if w not in cur_node.cList:
                        cur_node.cList[w] = Node(w)
                    cur_node = cur_node.cList[w]
                cur_node.length = len(word)

    def search(self, word):
        num = 0
        cur_node = self.root
        temp = []
        for w in word:
            if w == "?":
                for node in cur_node.cList.values():
                    temp.append(node)
                while temp:
                    temp_node = temp.pop()
                    if temp_node.length == len(word):
                        num += 1
                    else:
                        for node in temp_node.cList.values():
                            temp.append(node)
                return num
            elif w in cur_node.cList:
                cur_node = cur_node.cList[w]
            else:
                return num

def solution(words, queries):
    dic = {}
    answer = []
    tree = Tree()
    tree.create(words, False)

    for q in queries:
        if q not in dic:
            answer.append(tree.search(q))
        else:
            answer.append(dic[q])
    return answer