class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        indeg=[0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            indeg[u]+=1
        q=deque()
        for x in range(numCourses):
            if indeg[x]==0:
                q.append(x)
        count=0
        while q:
            node=q.popleft()
            count+=1
            for neigh in adj[node]:
                indeg[neigh]-=1
                if not indeg[neigh]:
                    q.append(neigh)
        return count==numCourses
        