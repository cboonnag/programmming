class Solution:
    def reverse(self, x: int) -> int:
        
        reverse = 0
        if x < 0:
            num = -x 
        else: 
            num = x
            
        while num != 0: 
            pop = num%10
            num = num//10
            
            if ( (reverse > 2147483648/10) or ((reverse == 2147483648/10) and (pop > 7))):
                return 0
            
            reverse = reverse*10 + pop
        
        if x < 0:
            return -reverse 
        else:
            return reverse 