class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        resArr = []
        i = 0
        intervals.sort()
        while i <len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                temp = intervals[i+1][1]
                intervals.insert(i, [ intervals[i][0], max(intervals[i+1][1], intervals[i][1] ) ] )
                intervals.remove(intervals[i+1])
                intervals.remove(intervals[i+1])
            else:
                i+=1
        return intervals

        
