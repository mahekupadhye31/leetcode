class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=defaultdict(list)
        for st in strs:
            sorted_string= "".join(sorted(st))
            h[sorted_string].append(st)
        
        return list(h.values())