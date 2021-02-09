# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.collect_sum = 0
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.convertBST(root.right)
        self.collect_sum += root.val
        root.val = self.collect_sum
        self.convertBST(root.left)
        
        return root