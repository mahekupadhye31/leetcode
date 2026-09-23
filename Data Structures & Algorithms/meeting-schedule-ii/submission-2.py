"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times=[]
        count=0

        for i in range(len(intervals)):
            times.append([intervals[i].start,"s"])
            times.append([intervals[i].end,"e"])
        times.sort()
        maxCount=0
        for time,val in times:
            if val=="s":
                count+=1
                maxCount=max(maxCount,count)
            else:
                count-=1
            
        return maxCount