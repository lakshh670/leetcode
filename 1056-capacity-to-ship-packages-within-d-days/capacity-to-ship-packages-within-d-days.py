class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right=max(weights),sum(weights)
        def check(wt):
            num_days=0
            s=0
            for i in range(len(weights)-1):
                s+=weights[i]
                if s>wt-weights[i+1]:
                    num_days+=1
                    s=0
            num_days+=1
            return num_days<=days
        while left<right:
            mid=left+(right-left)//2
            print(left,right)
            if check(mid):
                right=mid
            else:
                left=mid+1
        return left