class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=0
        w2=0
        word=""
        while w1<len(word1) and w2<len(word2):
            if w1<=w2:
                word+=word1[w1]
                w1+=1
            else:
                word+=word2[w2]
                w2+=1
        if w1<len(word1):
            word+=word1[w1:]
        if w2<len(word2):
            word+=word2[w2:]
        return word