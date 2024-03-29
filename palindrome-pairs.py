import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    @staticmethod
    def is_palidrome(word : str) -> bool:
        return word[::] == word[::-1]

    #단어 삽입
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palidrome(word[:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index

    def search(self, index, word) -> List[List[int]]:
        result = []
        node = self.root

        while word:
            # 판별 1
            if node.word_id >= 0:
                if self.is_palidrome(word):
                    result.append([index, node,word_id])
            if not word[0] in node.children:
                return result
            
            node = node.children[word[0]]
            word = word[1:]

            # 판별 2
            if node.word_id >= 0 and node.word_id != index:
                result.append([index, node.word_id])
            
            # 판별 3
            for palindrome_word_id in node.palindrome_word_ids:
                result.append([index, palindrome_word_id])
        
        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        answer = []
        for i, word in enumerate(words):
            answer.extend(trie.search(i, word))
        
        return answer


a = Solution().palindromePairs(['abcd', 'dcba', 'lls', 's', 'sssll'])
print(a)

## [abcd, 0] <-> ['dcba', 1]
