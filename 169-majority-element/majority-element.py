class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # O(NlogN) complexity
        # n=len(nums)
        # mid=n//2
        # nums.sort()
        # return nums[mid]

        # Boyer Moore's majority voting algorithm
        cnt,elem=0,None
        for x in nums:
            if elem==x:
                cnt+=1
            else:
                if not cnt:
                    elem=x
                else:
                    cnt-=1

        return elem
            

        