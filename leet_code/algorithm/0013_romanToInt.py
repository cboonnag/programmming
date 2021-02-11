class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        dct = {"M":1000,"D":500, "C":100, "L":50, "X":10,"V":5,"I":1}
        decimal = 0
        i = 0
        remain = n
        
        while i < n-1:
            if (dct[s[i]] < dct[s[i+1]]):
                decimal -= dct[s[i]] 
                decimal += dct[s[i+1]] 
                i += 2
                remain -= 2
            else:
                decimal += dct[s[i]]
                i += 1
                remain -=1
        
        if remain == 1 : 
            decimal += dct[s[i]]
            
        return decimal