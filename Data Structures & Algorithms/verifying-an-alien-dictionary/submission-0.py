class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank={}
        for i,char in enumerate(order):
            rank[char]=i
        
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            length=min(len(word1),len(word2))
            for j in range(length):
                if word1[j]!=word2[j]:
                    if rank[word1[j]]>rank[word2[j]]:
                        return False
                    else:
                        break
            if len(word1)>len(word2) and word1.startswith(word2):
                return False
        return True