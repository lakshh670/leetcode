class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        i,j=0,0
        max_len=0
        while j<len(s):
            if s[j] in dic and dic[s[j]]>=i:
                i=dic[s[j]]+1
            dic[s[j]]=j
            max_len=max(max_len,j-i+1)
            j+=1
        return max_len
        