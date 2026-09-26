"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count=0 
        maxcount=float("-inf")

        timings=[]
        for i in range(len(intervals)):
            timings.append([intervals[i].start,"start"])
            timings.append([intervals[i].end,"end"])

        timings.sort()

        for time,action in timings:
            if action=="start":
                count+=1
                maxcount=max(maxcount,count)
            else:
                count-=1
        return maxcount if maxcount!=float("-inf") else 0
            