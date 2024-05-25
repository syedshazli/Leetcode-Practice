#Notes
# intervals is an array of arrays, representing the intervals in ascending order
# obv we want to insert newInterval into these existing intervals, while maintining sorted ascending order
# If newInterval ends before current interval starts, we can add newInterval to result
# If newInterval starts before current interval ends, we can add current interval to new result array
# else, we can merge overlaps by taking the minimum of 2 intervals and maximum of the overlapping intervals and make it the new interval
# appending newInterval outside the loop is crucial

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        # Intervals is an array of arrays
        # new Interval is just the interval given
        result = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval) 
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                # minimum of left values and max of right values for new interval, our "merging method"
                newInterval = min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])

        result.append(newInterval) #handle edge cases like empty array, accounts for where newInterval is past the intervals or doesn't overlap!
        return result
        
