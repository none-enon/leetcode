class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash =[]
        for item in nums:
            
            if item in hash:
                hash.remove(item)
            else:
                hash.append(item)
        return hash[0]
