class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<m*k:
            return -1
        left,right=1,max(bloomDay)
        def check(num):
            bouq,flow=0,0
            for x in bloomDay:
                
                if num>=x:
                    flow+=1
                    if flow==k:
                        bouq+=1
                        flow=0
                else:
                    flow=0
            
            return bouq>=m

            

        while left<right:
            mid=left+(right-left)//2
            
            if check(mid):
                right=mid
                
            else:
                left=mid+1
        return left
        
        