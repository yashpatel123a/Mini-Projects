class Account:
    def __init__(self,account_number,opening_deposit):
        self.account_number = account_number
        self.balance = opening_deposit

    def __str__(self):
        return f'Rs. = {self.balance:.2f}'

    def deposit(self,deposit_amount):
        self.balance += deposit_amount

    def withdraw(self,withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            return 0
        else:
            print('Funds Unavailable')
            return 1

class Checking(Account):
    def __init__(self,account_number,opening_deposit):
        super().__init__(account_number,opening_deposit)

    def __str__(self):
        return f'Checking Account #{self.account_number}\nBalance: {Account.__str__(self)}'

class Savings(Account):
    def __init__(self,account_number,opening_deposit):
        super().__init__(account_number,opening_deposit)

    def __str__(self):
        return f'Savings Account #{self.account_number}\nBalance: {Account.__str__(self)}'

class Business(Account):
    def __init__(self,account_number,opening_deposit):
        super().__init__(account_number,opening_deposit)

    def __str__(self):
        return f'Business Account #{self.account_number}\nBalance: {Account.__str__(self)}'
                
class Customer:
    def __init__(self,name,PIN):
        self.name = name
        self.PIN = PIN
        self.accounts = {'C':[],'S':[],'B':[]}

    def __str__(self):
        return self.name

    def open_checking(self,account_number,opening_deposit):
        self.accounts['C'].append(Checking(account_number,opening_deposit))
    
    def open_savings(self,account_number,opening_deposit):
        self.accounts['S'].append(Savings(account_number,opening_deposit))
    
    def open_business(self,account_number,opening_deposit):
        self.accounts['B'].append(Business(account_number,opening_deposit))

    def get_total_deposits(self):
        total = 0
        print('***')
        for ac in self.accounts['C']:
            print(ac)
            total += ac.balance
        for ac in self.accounts['S']:
            print(ac)
            total += ac.balance
        for ac in self.accounts['B']:
            print(ac)
            total += ac.balance
        print(f'Combined Deposits: Rs. = {total:.2f}')

    def total_account(self):
        return len(self.accounts['C']) + len(self.accounts['S']) + len(self.accounts['B'])

        
def make_dep(cust,ac_type,ac_number,deposit_amount):
    flag = 1
    for ac in cust.accounts[ac_type]:
        if ac.account_number == ac_number:
            ac.deposit(deposit_amount)
            flag = 0
    return flag
 
def make_wd(cust,ac_type,ac_number,withdraw_amount):
    flag = 1
    for ac in cust.accounts[ac_type]:
        if ac.account_number == ac_number:
            flag = ac.withdraw(withdraw_amount)
    return flag
    
