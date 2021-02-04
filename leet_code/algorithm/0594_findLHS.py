class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        set_nums = sorted( list( set(nums) ) )
        m = len(set_nums)
        
        keep = {}
        for i in set_nums:
            keep[i] = 0

        for i in range(0,n):
            keep[ nums[i] ] += 1 

        c = [0 for i in range(m)]
        for i in range(0,m-1):
            if( abs(set_nums[i] - set_nums[i+1]) == 1 ):
                c[i] = keep[set_nums[i] ]+keep[ set_nums[i+1] ]

        return max(c)