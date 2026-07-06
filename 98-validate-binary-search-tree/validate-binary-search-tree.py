# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def greatest_left_tree(temp):
            if temp is None:
                return float('-inf')
            while temp.right:
                temp=temp.right
            return temp.val

        def smallest_right_tree(temp):
            if temp is None:
                return float('inf')
            while temp.left:
                temp=temp.left
            return temp.val

        case1=self.isValidBST(root.left) 
        case2= self.isValidBST(root.right)
        case3=greatest_left_tree(root.left)<root.val and smallest_right_tree(root.right)>root.val
        return case1 and case2 and case3
        