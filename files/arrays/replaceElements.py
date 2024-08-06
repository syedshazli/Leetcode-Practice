class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maximum = 0

        #for i in range(len(nums)) (Or maybe go reversed!)
        for i in range(len(arr)-1, -1, -1):
            
            if arr[i]<maximum:
                arr[i] = maximum
            prevmax = maximum
      
            maximum = max(maximum, arr[i])
            if arr[i]>prevmax and prevmax != 0:
                arr[i] = prevmax
            if i == len(arr)-2:
                arr[i] = arr[i+1]
        arr[len(arr)-1] = -1
        return arr
