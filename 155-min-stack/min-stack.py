class MinStack:

    def __init__(self):
        self.st=[]
        

    def push(self, value: int) -> None:
        if not self.st:
            self.st.append((value,value))
            return
        top=self.st[-1]
        elem=(value,value) if value<top[1] else (value,top[1])
        self.st.append(elem)

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()