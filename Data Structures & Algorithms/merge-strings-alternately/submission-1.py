class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=0
        w2=0
        result=[]
        while w1<len(word1) and w2<len(word2):
            if w1<=w2:
                result.append(word1[w1])
                w1+=1
            else:
                result.append(word2[w2])
                w2+=1
        while w1<len(word1):
            result.append(word1[w1])
            w1+=1
        while w2<len(word2):
            result.append(word2[w2])
            w2+=1
        return "".join(result)