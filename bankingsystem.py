class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        self. __balance += amount
        print("Deposit Succesful.New balance: ",self.__balance)    
    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient Balance.") 
        else:
            self.__balance -=amount
            print("Withdrawal Successful.Now balance :",self.__balance)
    def __show_balance(self):
        print("Current Balance is : ",self.__balance)               