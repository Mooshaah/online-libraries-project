class credit_Card:
## CLASS CREDIT CARD THAT CONTAINS TWO INSTANCE VARS: 
# 1)" CREDIT_BALANCE " WHICH INITALIZE THE BALANCE INSIDE THE ACCOUNT = 0
# 2) " AVAILABLE_CREDIT " THAT CONTAINS A DEAFULT AMOUNT OF MONEY SET FOR ALL REGULAR USERS, WHJICH IS = 1000  

    def __init__(self):
        self.credit_balance = 0 # initialize current balance
        self.available_credit = 1000 # initialize the available credit

    def get_balance(self):
        return  self.credit_balance
    def get_available_credit(self):
        return self.available_credit