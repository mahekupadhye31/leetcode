class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        n=len(intervals)

        intervals.sort(key=lambda x: x[1])
        # (5,10) (15,20) (0,30)

        count=0
        end_time=float("-inf")

        for i in range(len(intervals)):
            if intervals[i][0]>=end_time:
                count+=1
                end_time=intervals[i][1]
        return n-count