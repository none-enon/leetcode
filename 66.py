class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l=len(digits)
        flag=0
        results=[]
        if digits[-1]==9:
            digits[-1]=0
            flag=1
        else:
            digits[-1]+=1
        for i in range(l-2,-1,-1):
            digits[i] = digits[i]+flag
            if(digits[i]>=10):
                digits[i]-=10
                flag=1
            else:
                flag=0
        
        if flag==1:
            results.append(1)
        results = results+ digits
        return results
