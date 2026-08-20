class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe={}
        ans=[]
        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i]=False
            for neigh in graph[i]:
                if not dfs(neigh):
                    return False
            safe[i]=True
            return safe[i]
        for x in range(len(graph)):
            if dfs(x):
                ans.append(x)
        return ans

        
        