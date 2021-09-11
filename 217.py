class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        for i in range(1,len(nums)):
            key = nums[i]
            j=i-1
            while j>=0:
                if key==nums[j]:
                    return True
                if key > nums[j]:
                    break
                nums[j+1]=nums[j]
                j=j-1
        return False


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        for i in range(1,len(nums)):
            key = nums[i]
            j=i-1
            while j>=0:
                if key==nums[j]:
                    return True
                if key > nums[j]:
                    break
                nums[j+1]=nums[j]
                j=j-1
        return False
