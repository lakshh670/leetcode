# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # We know that inorder of bst is sorted, so we can just sort preorder to form the inorder
        inorder=sorted(preorder)
        dic={}
        for i,x in enumerate(inorder):
            dic[x]=i
        self.index=0
        def form_tree(l,r):
            if l>r:
                return None
            root=TreeNode(preorder[self.index])
            ind=dic[preorder[self.index]]
            self.index+=1
            root.left,root.right=form_tree(l,ind-1),form_tree(ind+1,r)
            return root
        return form_tree(0,len(preorder)-1)

        