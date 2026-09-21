
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic=defaultdict(list)
        for s in strs:
            dic[''.join(sorted(list(s)))].append(s)
        return [val for val in dic.values()]

        


        