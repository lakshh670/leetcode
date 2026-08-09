class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m,n=len(mat),len(mat[0])
       
            
            
        left,right=0,n-1
        while left<right:
            mid=left+(right-left)//2
            curr_row,max_elm=0,mat[0][mid]
            for i in range(m):
                if mat[i][mid]>max_elm:
                    max_elm=mat[i][mid]
                    curr_row=i
            l=mat[curr_row][mid-1] if mid>0 else -1
            r=mat[curr_row][mid+1] if mid<n-1 else -1
            if mat[curr_row][mid]>l and mat[curr_row][mid]>r:
                return [curr_row,mid]
            if mat[curr_row][mid]>r:
                right=mid
            else:
                left=mid+1
        # left == right, so find max element in final column
        curr_row = 0

        for i in range(1, m):
            if mat[i][left] > mat[curr_row][left]:
                curr_row = i

        return [curr_row, left]
        