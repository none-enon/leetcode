class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        reverse=[]
        step = k%len(nums)
        for i in range(step):
            reverse.append(nums[-step+i])
            #return reverse
        for j in range(len(nums)-step):
            reverse.append(nums[j])
        for i in range(len(nums)):
            nums[i]=reverse[i]
        
