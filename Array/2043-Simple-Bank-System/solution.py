class Bank:

    def __init__(self, balance: List[int]):
        self.n=len(balance)
        self.bank=balance
    def transfer(self, acc1: int, acc2: int, money: int) -> bool:
        acc1-=1
        acc2-=1
        #Check if account number is valid or not
        if(acc1>=self.n or acc2>=self.n):
            return False
        #check if account one has enough balance to transfer, if not then false
        if(money>self.bank[acc1]):
            return False
        #Transfer the money
        self.bank[acc1]-=money
        self.bank[acc2]+=money
        return True
    def deposit(self, account: int, money: int) -> bool:
        account-=1
        #Check if account number is valid or not
        if(account>=self.n):
            return False
        self.bank[account]+=money
        return True
    def withdraw(self, account: int, money: int) -> bool:
        account-=1
        #Check if account number is valid or not
        if(account>=self.n):
            return False
        #check if account one has enough balance to withdraw, if not then false
        if(money>self.bank[account]):
            return False
        self.bank[account]-=money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)