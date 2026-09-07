class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        s=0
        res=0
        for x in nums:
            s+=x
            if s%k in dic:
                res+=dic[s%k]
            dic[s%k]+=1
        return res