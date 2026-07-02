# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def find_left_height(node):
            if node is None:
                return 0
            return 1+find_left_height(node.left)
        
        def find_right_height(node):
            if node is None:
                return 0
            return 1+find_right_height(node.right)

        lh=find_left_height(root)
        rh=find_right_height(root)
        if lh==rh: 
            return 2**lh-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

        