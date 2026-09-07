class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        dic=defaultdict(int)
        s=0
        dic[s]=1
        for x in nums:
            s+=x
            if (s-k) in dic:
                res+=dic[s-k]
            dic[s]+=1
        return res
            
            
        