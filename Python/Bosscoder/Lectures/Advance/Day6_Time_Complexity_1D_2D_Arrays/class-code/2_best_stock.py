class Stock:
    def __init__(self, prices):
        self.prices = prices
    
    def solve(self):
        prices = self.prices 
        cheapPrice = prices[0]
        n = len(prices)

        ans = 0
        for i in range(1,n):
            if cheapPrice < prices[i]:
                ans = max(ans, prices[i] - cheapPrice)
            cheapPrice = min(cheapPrice, prices[i])
        
        return ans

if __name__ == "__main__":
    stock = Stock([7,1,5,3,6,4])
    print(stock.solve())