class Node:
    def __init__(self):
        self.child=[None]*26
        self.is_leaf=False
class Trie:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.child[index] is  None:
                curr.child[index]=Node()
            curr=curr.child[index]
        curr.is_leaf=True

    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            index=ord(c)-ord('a')
            if curr.child[index] is None:
                return False
            curr=curr.child[index]
        return curr.is_leaf

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            index=ord(c)-ord('a')
            if curr.child[index] is None:
                return False
            curr=curr.child[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)