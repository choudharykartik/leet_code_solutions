class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # with two pointer approach
        l,r,maxprof=0,1,0
        while r<len(prices):
            if prices[l] < prices[r]:
                prof = prices[r]-prices[l]
                maxprof = max(maxprof,prof)
            else:
                l=r
            r+=1
        return maxprof
