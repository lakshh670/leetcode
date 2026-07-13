class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # cnt,elem=0,None
        # res=[]
        # n=len(nums)
        # for x in nums:
        #     if elem is None or elem==x:
        #         cnt+=1                
        #     else:        
        #         cnt=1
        #     if cnt>n//3:
        #             res.append(x)
           
        #     elem=x
            
        # return list(set(res))

        # Boyer Moore majority voting algorithm: O(1) space
        res=[]
        n=len(nums)
        majority1,majority2,cnt1,cnt2=None,None,0,0
        for x in nums:
            if x==majority1:
                cnt1+=1
            elif x==majority2:
                cnt2+=1
            elif cnt1==0:
                majority1=x
                cnt1=1
            elif cnt2==0:
                majority2=x
                cnt2=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1,cnt2=0,0
        for x in nums:
            if x==majority1 :
                cnt1+=1
            if x==majority2 :
                cnt2+=1
        if cnt1>n//3:
            res.append(majority1)
        if cnt2>n//3:
            res.append(majority2)
        return res
            
        