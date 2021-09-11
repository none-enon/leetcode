class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        dict2={}
        set1=[]
        for item in nums1:
            if item in dict1:
                dict1[item]+=1
            else:
                dict1[item]=1
        for item in nums2:
            if item in dict2:
                dict2[item]+=1
            else:
                dict2[item]=1
        for key in dict1.keys():
            if key in dict2.keys():
                for i in range(min(dict1[key],dict2[key])):
                    set1.append(key)
        return set1
        
