class Solution:
    def totalMoney(self, n: int) -> int:
        total_money=0
        total_weeks=n//7 #we can get 28 dollars per week and an one dollar increament every week... 28-> 28+(1*7) -> 28+(2*7)
        pay_days=n%7
        inc=0
        total_money=0
        for week in range(total_weeks):
            total_money+=28+(inc*7)
            inc+=1
        inc+=1
        for i in range(pay_days):
            total_money+=inc
            inc+=1
        return total_money