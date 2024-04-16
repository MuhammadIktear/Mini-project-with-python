class Bank:
    def __init__(self,balance) -> None:
        self.balance=balance
        self.min_withdraw=100
        self.max_withdrow=100000

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f'Your balance after deposit {self.balance}')
        else:
            print('Invalid amount')

    def withdraw(self,amount):
        if amount<self.min_withdraw:
            print( f'fokira. You can withdraw below {self.min_withdraw}')
        elif amount>self.max_withdrow:
            print( f'bank fokir hoye jabe. You can not withdraw more than {self.max_withdrow}')
        else:
            self.balance-=amount
            print( f'Here is you money {amount}')
            print(f'Your balance after withdraw {self.balance}')
        
brac=Bank(15000)
brac.withdraw(1000)
brac.deposit(200000)
