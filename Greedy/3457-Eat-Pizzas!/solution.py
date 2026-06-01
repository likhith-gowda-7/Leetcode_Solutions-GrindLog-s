class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n=len(pizzas)
        z=n-1
        odd_takes=math.ceil((n/4)/2)
        even_takes=(n//4)//2
        total=0
        idx=n-1
        for odd_days in range(odd_takes):
            total+=pizzas[idx]
            idx-=1
        idx-=1
        for even_days in range(even_takes):
            total+=pizzas[idx]
            idx-=2
        return total