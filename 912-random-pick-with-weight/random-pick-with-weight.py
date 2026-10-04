import random
class Solution:

    def __init__(self, w: list[int]):
        self.w=w
        s=sum(self.w)
        self.prob=[x/s for x in self.w]
        curr_sum=0
        self.range=[]
        for i in range(len(self.prob)):
            lower_bound=curr_sum
            curr_sum+=self.prob[i]
            upper_bound=curr_sum
            self.range.append([lower_bound,upper_bound])
        

    def pickIndex(self) -> int:
        x=random.random()
        l,r=0,len(self.range)
        while l<r:
            mid=l+(r-l)//2
            if self.range[mid][0]<=x<=self.range[mid][1]:
                return mid
            elif x>self.range[mid][1]:
                l=mid+1
            else:
                r=mid


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()