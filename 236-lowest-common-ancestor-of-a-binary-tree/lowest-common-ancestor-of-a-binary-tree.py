# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict,deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        par1=defaultdict(int)
        q_=deque()
        q_.append((root,-1))
        while q_:
            node,par=q_.popleft()
            par1[node]=par
            if node.left:
                q_.append((node.left,node))
            if node.right:
                q_.append((node.right,node))
        ansec1,ansec2=[p],[q]
        key=p
        while par1[key]!=-1:
            ansec1.append(par1[key])
            key=par1[key]
        key=q
        while par1[key]!=-1:
            ansec2.append(par1[key])
            key=par1[key]
        for x in ansec1:
            if x in ansec2:
                return x

           
        