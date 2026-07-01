# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(arr):
            i,j=0,len(arr)-1
            while i<j:
                if arr[i]!=arr[j]:
                    return False
                i+=1
                j-=1
            return True
        q=deque()
        q.append(root)
        while q:
            arr=[]
            n=len(q)
            for _ in range(n):
                node=q.popleft()
                if node is None:
                    arr.append(-101)
                else:
                    arr.append(node.val)
                    if node.left:
                        q.append(node.left)
                    else:
                        q.append(None)
                    if node.right:
                        q.append(node.right)
                    else:
                        q.append(None)
            print(arr)
            if not check(arr):
                return False
        return True
        