class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s)==0:
            return True
        list1=[]
        for char in s:
            if char=='(':
                list1.append(char)
                continue
            if char=='*':
                list1.append('*')
                continue
            
            if char==')':
                if '(' in list1:
                    i=len(list1)-1
                    while(list1[i]!='('):
                        i=i-1
                    list1.pop(i)

                elif '*' in list1:
                    i=len(list1)-1
                    while(list1[i]!='*'):
                        i=i-1
                    list1.pop(i)
                    
                else:
                    return False
                continue
        if len(list1)==0:
            return True
        list2=[]
        for i in range(len(list1)-1,-1,-1):
            if list1[i]=='*':
                list2.append(list1[i])
            if list1[i] == '(':
                if '*' in list2:
                    list2.remove('*')
                else:
                    return False
        return True
                
        
