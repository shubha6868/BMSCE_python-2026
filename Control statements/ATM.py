# ATM withdrawl with balance check
#acct balance=input eg-5000
#amt to withdrawn=input eg=500
#check can 500 be withdrawn?
#otherwise print insufficient balance or invalid amount
balance=int(input("enter your balance"))
amount=int(input(''enter amount to withdraw"))
if balance>=amount:
    if  amount>500:
        print("you can withdraw")
      else:
          print("Insufficient balance")
