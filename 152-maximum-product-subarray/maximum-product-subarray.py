class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute Force: Try all possible subarrays
        # maxProd = nums[0]

        # # Outer loop picks the starting index
        # for i in range(len(nums)):
        #     # Initialize current product to 1
        #     prod = 1

        #     # Inner loop picks the ending index
        #     for j in range(i, len(nums)):
        #         # Multiply current number to product
        #         prod *= nums[j]

        #         # Update maximum product if needed
        #         maxProd = max(maxProd, prod)

        # # Return the result
        # return maxProd

        # Approach2: we just need to apply kadane's algo twice, one in forward direction and other in backward direction.
        # maxi1=float('-inf')
        # prod=1
        # for x in nums:
        #     prod*=x
        #     maxi1=max(prod,maxi1)
        #     if prod==0:
        #         prod=1
            
        # maxi2=float('-inf')
        # prod=1
        # for x in nums[::-1]:
            
        #     prod*=x
        #     maxi2=max(prod,maxi2)
        #     if prod==0:
        #         prod=1
            
        # return max(maxi1,maxi2)


        # Approach3:
        res,max_prod,min_prod=nums[0],nums[0],nums[0]
        for x in nums[1:]:
            if x<0:
                max_prod,min_prod=min_prod,max_prod
            max_prod=max(x,max_prod*x)
            min_prod=min(x,min_prod*x)
            res=max(res,max_prod)
        return res
            
