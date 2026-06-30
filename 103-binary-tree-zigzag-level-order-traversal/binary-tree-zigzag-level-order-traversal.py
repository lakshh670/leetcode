# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        sol=[]
        q=deque()
        q.append(root)
        timer=0
        while q:
            ans=[]
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                ans.append(node.val)
            if timer%2==0:
                sol.append(ans)
            else:
                sol.append(ans[::-1])
            timer+=1
        return sol
                    


        