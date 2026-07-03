# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic={}
        self.index=0
        for i,x in enumerate(inorder):
            dic[x]=i
        n=len(inorder)
        def solve(i,j):
            if i>j :
                return None

            
            root=TreeNode(preorder[self.index])
            ind=dic[preorder[self.index]]
            self.index+=1
            root.left,root.right=solve(i,ind-1),solve(ind+1,j)
            return root
        return solve(0,n-1)
        