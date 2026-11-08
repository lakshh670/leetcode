class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        q=[]
        n=len(matrix)
        for i in range(n):
            for j in range(n):
                heapq.heappush(q,-matrix[i][j])
                if len(q)>k:
                    heapq.heappop(q)
        return -q[0]
        