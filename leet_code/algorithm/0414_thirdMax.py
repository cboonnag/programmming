class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(list(set(nums)), reverse = True)
        
        if len(sorted_nums) < 3:
            return max(sorted_nums)
        else:
            return sorted_nums[2]