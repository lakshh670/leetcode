class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q=deque()
        visit=set()
        wordList=set(wordList) # That's the most important step, we are converting this to a set because searching in set takes constant time
        q.append((beginWord,1))
        visit.add(beginWord)
        while q:
            word,steps=q.popleft()
            
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                for i in range(len(word)):
                    new_word=word[:i]+ch+word[i+1:]
                    if new_word not in visit and new_word in wordList  :
                        if new_word==endWord:
                            return steps+1
                        q.append((new_word,steps+1))
                        visit.add(new_word)
        return 0

        