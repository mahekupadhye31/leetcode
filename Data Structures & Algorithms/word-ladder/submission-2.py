class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if beginWord==endWord:
            return 0
    
        wordSet=set(wordList)

        q=deque([(beginWord,1)])

        while q:
            word,length=q.popleft()
            if word==endWord:
                return length
            for i in range(len(word)):
                for alpha in range(26):
                    newword=word[:i]+ chr(alpha+ord('a')) + word[i+1:]
                    if newword in wordSet:
                        wordSet.remove(newword)
                        q.append((newword,length+1))
        return 0