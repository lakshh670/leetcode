import heapq
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n=len(nums)
        q=[]
        for i in range(k):
            heapq.heappush(q,(-nums[i],i))
        l,r=0,k-1
        res=[]
        while r<n:
            while q[0][1]<l:
                heapq.heappop(q)
            
            res.append(-q[0][0])
            l+=1
            r+=1
            if r<n:
                heapq.heappush(q,(-nums[r],r))
        return res
            

        