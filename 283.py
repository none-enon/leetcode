class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index=0
        count=0
        for i in range(len(nums)):
            if(nums[i]==0):
                count+=1
            else:
                nums[index]=nums[i]
                index+=1
        for j in range(count):
            nums[-count+j]=0
