class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        cnt,elem=0,None
        res=[]
        n=len(nums)
        for x in nums:
            if elem is None or elem==x:
                cnt+=1                
            else:        
                cnt=1
            if cnt>n//3:
                    res.append(x)
           
            elem=x
            
        return list(set(res))
        