from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(0,len(nums)):
            remain = target - nums[i]
            new_nums = nums[i+1:]
            
            if remain in new_nums:
                j = i+1 + new_nums.index(remain)
                output = [i,j]
                return output

if __name__ == "__main__":
    x = Solution
    print(x.twoSum(x,[2,7,11,15],9))