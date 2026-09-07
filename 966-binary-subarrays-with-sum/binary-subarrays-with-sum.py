class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        k=goal
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
        