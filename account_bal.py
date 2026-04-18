a=float(input("Ener initial balance:"))
print("1.Deposit\n2.Withdrawal\n")
b=int(input("Enter choice:"))
c=int(input("Enter transaction amount:"))
if b==1:
   if c>500:
      d=a+c
      print("Amount deposited")
      print("Updated Balance:",d)
   else:
      print("Minimum 500 rupees should be deposited")
elif b==2:
   d=a-c
   if a<c:
      print("Your balance is less than the withdrawal amount")
   elif d>1000 and d>0:
      print("Withdrawal is done")
      print("Updated balance:",d)
   else:
      print("Account balance should be minimum 1000")
