class Account:
     def __init__(self,ano,cname,abal):
          self.account_no=ano
          self.customer_name=cname
          self.account_balance=abal
     def deposit(self,amount):
          self.account_balance+=amount
     def withdraw(self,amount):
           if self.account_balance>amount:
                self.account_balance-=amount
           else:
                 return "Insufficent account balance"
     def dispaly(self,accounts):
          for cus in accounts:
                print(cus.customer_name,cus.account_no,cus.account_balance)
     @classmethod
     def search_cus_by_account_number(cls,accounts):
           acc=int(input("Enter the customer account number ..."))
           for cus in accounts:
                if acc ==  cus.account_no: 
                       print(cus.customer_name,cus.account_no,cus.account_balance)
                       break
           else:
                 print("Customer not found with this accout  number ...")    
     @classmethod
     def deposit_amount_customer_account(cls,accounts):
           acc=int(input("Enter the customer account number ..."))
           amount= int(input("Enter the amount in account ..."))
           for cus in accounts:
                if acc ==  cus.account_no: 
                       cus.account_balance+=amount
                       return "Amount deposit successfully"
           else:
                 print("Customer not found with this accout  number ...") 
                 return "Amount not deposit "   
     @classmethod
     def account_have_amount_gretter_50000(cls,accounts):
           for cus in accounts:
                if cus.account_balance>50000: 
                             print(cus.customer_name,cus.account_no,cus.account_balance)
     @classmethod
     def account_highest_bal(cls,accounts):
           higest= accounts[0].account_balance
           for cus in accounts:
                          if cus.account_balance>higest: 
                                      higest=cus.account_balance
           return higest