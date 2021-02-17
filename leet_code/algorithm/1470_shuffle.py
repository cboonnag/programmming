class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        m = int(n/2) 
        
        res = []
        for i in range(m):
            res.append(nums[i])
            res.append(nums[i+m])
        
        return res