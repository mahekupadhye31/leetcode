class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet=set(wordList)

        if beginWord in wordSet:
            wordSet.remove(beginWord)
        
        q=deque([(beginWord,1)])

        while q:
            word,seq=q.popleft()
            if word==endWord:
                return seq
            length=len(word)
            for i in range(length):
                for alpha in range(26):
                    newword=word[0:i]+chr(alpha+ord('a'))+word[i+1:]
                    if newword in wordSet:
                        q.append((newword,seq+1))
                        wordSet.remove(newword)
        return 0           