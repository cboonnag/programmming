class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1) 
        n2 = len(word2)
        
        ls1 = list(word1)
        ls2 = list(word2)
        
        n_min = min(n1,n2)
        
        res = []
        
        for i in range(n_min):
            res.append(ls1[i])
            res.append(ls2[i])
            
        if n1 == n_min:
            for i in range(n_min,n2):
                res.append(ls2[i])
        else: 
            for i in range(n_min,n1):
                res.append(ls1[i])
                
        str1 = ""
        return str1.join(res)