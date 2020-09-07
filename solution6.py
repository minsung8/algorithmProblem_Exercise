import os
import sys

from collections import defaultdict

class Tree:
    def __init__(self):
        self.root = {}

    def create(self,  word):
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = [{}, 0]
            cur[w][1] += 1
            cur = cur[w][0]

    def search(self, query):
        cnt = 0
        cur = self.root
        for q in query:
            if q == "?":
                return cnt
            elif q in cur.keys():
                cnt = cur[q][1]
            else:
                return 0
            cur = cur[q][0]

def solution(words, queries):
    dic = defaultdict(Tree)
    re_dic = defaultdict(Tree)
    len_dict = defaultdict(int)
    answer = []

    for word in words:
        dic[len(word)].create(word)
        re_dic[len(word)].create(word[::-1])
        len_dict[len(word)] += 1

    for query in queries:
        if query[0] == "?" and query[-1] == "?":
            answer.append(len_dict[len(query)])
        elif query[0] != "?":
            answer.append(dic[len(query)].search(query))
        else:
            answer.append(re_dic[len(query)].search(query[::-1]))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?", "?????", "fro??"]))