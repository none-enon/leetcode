class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxi=0

        for i in range(len(prices)-1):
            interest = prices[i+1]-prices[i]
            if interest>0:
                maxi+=interest
