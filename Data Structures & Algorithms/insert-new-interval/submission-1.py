class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        n=len(intervals)
        i=0
        #left portion
        for s,e in intervals:
            if e<newInterval[0]:
                result.append([s,e])
                i+=1
            else:
                break

        #middle portion that we need to merge
        while i<n and newInterval[1]>=intervals[i][0]:
            newInterval[0]=min(newInterval[0],intervals[i][0])
            newInterval[1]=max(newInterval[1],intervals[i][1])
            i+=1
        result.append(newInterval)
        #right portion
        while i<n:
            result.append(intervals[i])
            i+=1
        return result

            