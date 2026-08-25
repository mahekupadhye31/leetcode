class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={}
        order=[]
        for i in range(numCourses):
            preMap[i]=[]
        for curr,pre in prerequisites:
            preMap[curr].append(pre)   
        visitSet=set()
        def dfs(curr):
            if preMap[curr]==[]:
                if curr not in order:
                    order.append(curr)
                return True
            if curr in visitSet:
                return False

            visitSet.add(curr)
            for pre in preMap[curr]:
                if not dfs(pre): return False
            visitSet.remove(curr)  

            if curr not in order:
                order.append(curr) 
            return True     

        for i in range(numCourses):
            if not dfs(i):
                return []
        return list(order )         

        