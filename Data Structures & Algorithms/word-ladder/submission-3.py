class Solution:
    def ladderLength(self, beginword: str, endword: str, wordlist: List[str]) -> int:
        wordset=set(wordlist)
        if beginword==endword:
            return 1
        
        q=deque([(beginword,1)])
        while q:
            word,steps=q.popleft()
            if word==endword:
                return steps
            for i in range(len(word)):
                for alpha in range(26):
                    newword=word[:i]+chr(alpha+97)+word[i+1:]
                    if newword in wordset:
                        q.append((newword,steps+1))
                        wordset.remove(newword)
        return 0


        
