"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        filled = set()
        for inter in intervals:
            for i in range(inter.start, inter.end):
                if i in filled: return False
                filled.add(i)
        return True