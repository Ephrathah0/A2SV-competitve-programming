#Insert Operation:
#Time: O(n)
#Space: O(n)
#Search Operation:
#Time: O(n)
#Space: O(1)
#StartsWith Operation:
#Time: O(n)
#Space: O(1)
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
           
    def addWord(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isWord = True        
    
    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
        if current.isWord:
            return True
        else:
            return False
    
    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            if char in current:
                current = current.children[char]
            else:
                return False
        return True
