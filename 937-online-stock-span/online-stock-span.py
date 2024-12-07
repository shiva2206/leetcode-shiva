class StockSpanner:

    def __init__(self):
        self.s = []
        self.ans = 0 
    def next(self, price: int) -> int:
       
        cur_price,cur_span = price,1
        while self.s and self.s[-1][0]<=cur_price:
            prev_price,prev_span = self.s.pop()

            cur_span += prev_span
        self.s.append((cur_price,cur_span))
        return cur_span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)