# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k=k
        self.ans=None
        def find(root):
            if self.ans is not None:
                return
            if root.left:
                find(root.left)
            if self.k==1:
                self.ans=root.val
                self.k-=1
                return
            self.k-=1
            if root.right:
                find(root.right)
        find(root)
        return self.ans

        