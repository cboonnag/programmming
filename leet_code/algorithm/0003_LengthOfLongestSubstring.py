class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = len(set(s))
        n = len(s)
        output = 0
        dct = {}
        i = 0
        
        for j in range(n):
            if s[j] in dct:
                i = max(dct[s[j]], i)
            
            output = max(output, j-i+1)
            dct[s[j]] = j+1
            
            if output == maxlen:
                return output 
        
        return output