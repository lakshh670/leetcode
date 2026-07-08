from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic=defaultdict(int)
        for i,x in enumerate(nums):
            if target-x in dic:
                return [i,dic[target-x]]
            dic[x]=i


        