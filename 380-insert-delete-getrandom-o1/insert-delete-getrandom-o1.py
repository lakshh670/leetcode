class RandomizedSet:

    def __init__(self):
        self.lst=[]
        self.ind_map={}

    def insert(self, val: int) -> bool:
        if val in self.ind_map:
            return False
        self.lst.append(val)
        self.ind_map[val]=len(self.lst)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.ind_map:
            return False
        index=self.ind_map[val]
        self.lst[index]=self.lst[-1]
        self.ind_map[self.lst[-1]]=index
        self.lst.pop()
        del self.ind_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()