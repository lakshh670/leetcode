class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=set()
        nums.sort()
        for i in range(n):
            tar=target-nums[i]
            j=i+1
            
            while j<n:
                k,l=j+1,n-1
                while k<l:
                    if nums[j]+nums[k]+nums[l]==tar:
                        res.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif nums[j]+nums[k]+nums[l]<tar:
                        k+=1
                    else:
                        l-=1
                j+=1
        return [list(x) for x in res]