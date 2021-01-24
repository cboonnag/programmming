class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combine = sorted(nums1 + nums2)
        n = len(combine)
        half = int(n/2)
        
        if n%2:
            return combine[half]
        else:
            return float(combine[half-1] + combine[half]) /2