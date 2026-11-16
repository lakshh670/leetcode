# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        q=deque()
        res=[]
        arr=[]
        q.append(root)
        q.append(None)
        while q:
            node=q.popleft()
            if node:
                arr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                res.append(arr)
                arr=[]
                if q:
                    q.append(None)
        return res
        