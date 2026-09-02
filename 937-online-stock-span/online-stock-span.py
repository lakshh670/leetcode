class StockSpanner:
    # Brute Force
    # def __init__(self):
    #     self.stocks=[]
    
    
        
        

    # def next(self, price: int) -> int:
    #     cnt=1
    #     st=self.stocks[:]
    #     while st and st[-1]<=price:
    #         st.pop()
    #         cnt+=1
    #     self.stocks.append(price)
    #     return cnt

    # Most Optimal
    def __init__(self):
        self.stack = []  # Each element: [price, span]

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append([price, span])
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)