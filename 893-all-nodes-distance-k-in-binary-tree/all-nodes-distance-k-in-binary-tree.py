# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict,deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj=defaultdict(list)
        def preorder(node,par):
            if node is None:
                return
            nonlocal adj
            if par!=None:
                adj[par.val].append(node.val)
                adj[node.val].append(par.val)
            preorder(node.left,node)
            preorder(node.right,node)
        preorder(root,None)
        if k>=len(adj):
            return []
        
        
        q,visit=deque(),set()
        q.append((target.val,0))
        visit.add(target.val)
       
        ans=[]
        while q:
            node,steps=q.popleft()
            if steps==k:
                ans.append(node)
            else:
                for neigh in adj[node]:
                    if neigh not in visit:
                        q.append((neigh,steps+1))
                        visit.add(neigh)
        return ans

        
        


        