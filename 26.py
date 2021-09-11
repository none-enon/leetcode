class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
        l = len(nums)
        j=0
        for i in range(1,l):
            if nums[j] == nums[j+1]:
                del(nums[j+1])
            else:
                j = j+1
        return len(nums)
            
