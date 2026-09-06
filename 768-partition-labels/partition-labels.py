class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index={}
        for i,c in enumerate(s):
            last_index[c]=i
        end,pat_len=0,0
        res=[]
        for i,c in enumerate(s):
            pat_len+=1
            end=max(end,last_index[c])
            if i==end:
                res.append(pat_len)
                pat_len=0
        return res