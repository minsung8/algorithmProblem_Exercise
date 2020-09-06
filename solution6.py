# 프로그래머스 : https://programmers.co.kr/learn/courses/30/lessons/60060

import os
import sys

from collections import defaultdict

class Trie:

    def __init__(self):
        self.root = {} # chr|visited

    def insert(self, s):
        cur = self.root
        while s:
            if s[0] not in cur: cur[s[0]] = [ {} , 0 ]
            cur[s[0]][1] += 1
            cur = cur[s[0]][0]
            s = s[1:]


    def find(self, s)->int:
        cur = self.root; pre_v = 0
        while s:
            if s[0] == '?': return pre_v
            else:
                if s[0] not in cur: return 0
                pre_v = cur[s[0]][1]; cur = cur[s[0]][0]
            s = s[1:]

        return pre_v

def solution(words, queries):
    prefix_dict = defaultdict(Trie)
    result = []

    for word in words:
        prefix_dict[len(word)].insert(word)

    for q in queries:
        result.append(prefix_dict[len(q)].find(q))

    return result

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))