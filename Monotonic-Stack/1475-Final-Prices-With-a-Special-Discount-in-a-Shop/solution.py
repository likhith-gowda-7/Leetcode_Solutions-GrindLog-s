class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        stack=[]
        res=[0]*n
        for item,price in enumerate(prices):
            while stack and stack[-1][1]>=price:
                prev_item,prev_item_price=stack.pop()
                res[prev_item]=prev_item_price-price
            stack.append((item,price))
        for item,price in stack:
            res[item]=price
        return res