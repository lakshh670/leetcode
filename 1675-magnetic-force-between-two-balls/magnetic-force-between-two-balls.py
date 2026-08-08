class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left,right=0,position[-1]-position[0]

        def check(target):
            last_position,count=position[0],1
            for x in position[1:]:
                if x-last_position>=target:
                    count+=1
                    last_position=x
            return count>=m
        res=-1
        while left<=right:
            mid=left+(right-left)//2
            if check(mid):
                res=mid
                left=mid+1
            else:
                right=mid-1
        return res

        