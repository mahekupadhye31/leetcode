class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={}
        for i in range(numCourses):
            preMap[i]=[]
        for curr,pre in prerequisites:
            preMap[curr].append(pre)   
        visitSet=set()
        def dfs(curr):
            if preMap[curr]==[]:
                return True
            if curr in visitSet:
                return False

            visitSet.add(curr)
            for pre in preMap[curr]:
                if not dfs(pre): return False
            visitSet.remove(curr)  

            return True          

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True             

        