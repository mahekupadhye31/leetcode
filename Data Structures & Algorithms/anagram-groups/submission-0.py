class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=defaultdict(list)
        result=[]

        for st in strs:
            sort="".join(sorted(st))
            #sorted() returns a list ["a","e","t"]
            h[sort].append(st)

        for val in h.values():
            result.append(val)
        return result