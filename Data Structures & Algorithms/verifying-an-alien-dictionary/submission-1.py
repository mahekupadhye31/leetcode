class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank={}
        for i,ch in enumerate(order):
            rank[ch]=i

        for i in range(len(words)-1):
            s1=words[i]
            s2=words[i+1]
            if len(s1)>len(s2) and s1.startswith(s2):
                return False
            length=min(len(s1),len(s2))
            for j in range(length):
                if s1[j]!=s2[j]:
                    if rank[s1[j]]>rank[s2[j]]:
                        return False
                    elif rank[s1[j]]<=rank[s2[j]]:
                        break
                        
        return True
