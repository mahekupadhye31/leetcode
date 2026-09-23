"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n=len(intervals)

        intervals.sort(key=lambda x: x.end)
        # (5,10) (15,20) (0,30)

        count=0
        end_time=0 

        for i in range(len(intervals)):
            if intervals[i].start>=end_time:
                count+=1
            end_time=intervals[i].end

        return count==n