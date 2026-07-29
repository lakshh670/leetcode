class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        def find_first():
            left,right,ans=0,n-1,-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]==target:
                    ans=mid
                    right=mid-1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return ans
        def find_last():
            left,right,ans=0,n-1,-1
            while left<=right:
                mid=left+(right-left)//2
                if nums[mid]==target:
                    ans=mid
                    left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return ans

        return [find_first(),find_last()]

        
        
        