a=float(input("Enter monthly salary of an emoployee:"))
b=int(input("Enter number of days the employee was absent"))
if b>2:
   c=a-((b-2)*500)
else:
   c=a
print("Final salary:",c)
