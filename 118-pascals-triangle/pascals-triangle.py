class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # Iterative approach
        # res=[]
        # for i in range(numRows):
        #     row=[]
        #     for j in range(i+1):
        #         if j==0 or j==i:
        #             row.append(1)
        #         else:
        #             row.append(res[i-1][j-1]+res[i-1][j])
        #     res.append(row)
        # return res

        # Recursive approach
        if numRows==1:
            return [[1]]
        prev_rows=self.generate(numRows-1)
        row=[1]
        for i in range(1,numRows-1):
            row.append(prev_rows[-1][i-1]+prev_rows[-1][i])
        row.append(1)
        prev_rows.append(row)
        return prev_rows

        


        