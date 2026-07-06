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
        # My approach
        # def greatest_left_tree(temp):
        #     if temp is None:
        #         return float('-inf')
        #     while temp.right:
        #         temp=temp.right
        #     return temp.val

        # def smallest_right_tree(temp):
        #     if temp is None:
        #         return float('inf')
        #     while temp.left:
        #         temp=temp.left
        #     return temp.val

        # Most optimal
        def dfs(node,low,high):
            if node is None:
                return True
            if not low<node.val<high:
                return False
            return dfs(node.left,low,node.val) and dfs(node.right,node.val,high)


        case1=self.isValidBST(root.left) 
        case2= self.isValidBST(root.right)
        case3=dfs(root,float('-inf'),float('inf'))
        return case1 and case2 and case3
        