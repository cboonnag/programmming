# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        right_view = []
        
        if not root:
            return right_view
        else:
            right_view.append(root.val)
            
        from_right = right_view + self.rightSideView(root.right)
        from_left = right_view + self.rightSideView(root.left)
        
        len_r = len(from_right)
        len_l = len(from_left)
        
        if len_r < len_l:
            return from_right + from_left[len_r:]
        else: 
            return from_right