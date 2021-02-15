class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        n = len(s)
        i = 0 
        
        num_r = 0
        num_l = 0
        
        while (i < n):
            if s[i] == 'R':
                num_r +=1
            else:
                num_l += 1
            if (num_r == num_l) and (num_r >0 ) and (num_l > 0) :
                res += 1
            i+=1
            
        return res