class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        result=[intervals[0]]

        for start,end in intervals:
            latest_merge=result[-1]
            if start<=latest_merge[1]:
                latest_merge[1]=max(latest_merge[1],end)
                latest_merge[0]=min(latest_merge[0],start)
            
            else:
                result.append([start,end])
        return result