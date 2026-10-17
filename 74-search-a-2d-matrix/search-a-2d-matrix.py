class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        low,high=0,m*n-1
        while low<=high:
            mid=low+(high-low)//2
            row,col=mid//n,mid%n
            if target==matrix[row][col]:
                return True
            elif target>matrix[row][col]:
                low=mid+1
            else:
                high=mid-1
        return False
        