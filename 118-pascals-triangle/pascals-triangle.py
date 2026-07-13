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

        res = [[1]]

        for _ in range(numRows - 1):
            dummy_row = [0] + res[-1] + [0]
            row = []

            for i in range(len(res[-1]) + 1):
                row.append(dummy_row[i] + dummy_row[i+1])
            res.append(row)
        
        return res


        