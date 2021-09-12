class Solution:
    def reverse(self, x: int) -> int:
        max = 2**31-1
        min = -2**31       
        s = str(x)
        if s[0].isdigit():
            s=s[::-1]
        else:
            s1=s[1:]
            s1=s1[::-1]
            s = s[0]+s1
        s = int(s)
        if s>max or s< min:
            return 0
        else:
            return s
        
