class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ls = list(s)
        n = len(s)
        
        c_index = []
        res = []
        
        for i in range(n):
            if ls[i] == c:
                c_index.append(i)
                
        for i in range(n):
            tmp = [abs(i-x) for x in c_index]
            distance = min(tmp) 
            res.append(distance)
            
        return res