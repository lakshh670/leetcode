import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        for x in nums:
            dic[x]+=1
        freq=[]
        for elm,cnt in dic.items():
            heapq.heappush(freq,(-cnt,elm))
        res=[]
        for _ in range(k):
            cnt,elm=heapq.heappop(freq)
            res.append(elm)
        return res
        