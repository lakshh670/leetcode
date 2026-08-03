class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # count=0
        # for x in range(1,arr[-1]+k+1):
        #     if x not in arr:
        #         count+=1
        #     if count==k:
        #         return x


        # Binary Search
        left,right=0,len(arr)
        while left<right:
            mid=left+(right-left)//2
            x=arr[mid]-(mid+1)
            if x<k:
                left=mid+1
            else:
                right=mid
        return left+k
        