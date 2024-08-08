class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if len(stones)==1:
            return stones[0]
        #sorting the list every time
        while len(stones)>1:
            stones.sort()
            bigger = stones[(len(stones)-1)]
            small = stones[(len(stones)-2)]
            if bigger == small:
                stones.remove(bigger)
                stones.remove(small)
            else:
                stones[(len(stones)-1)] = bigger-small
                stones.remove(small)
        if len(stones)==0:
            return 0
        else:
            return stones[0]
