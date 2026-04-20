print("Enter 5 subject marks:")
i=0
tot=0
while i<5:
    a=int(input())
    if a>100:
        print(a,"is invalid:")
        break
    tot=tot+a
    i=i+1
per=tot/5
print("Aggregate:",tot)
print("Percentage:",per)
print("Grade is:",end=" ")
if per<=100 and per>=90:
    print("O")
elif per<90 and per>=80:
    print("A+")
elif per<80 and per>=70:
    print("A")
elif per<70 and per>=60:
    print("B+")
elif per<60 and per>=55:
    print("B")
elif per<55 and per>=50:
    print("C")
elif per<50 and per>=0:
    print("F")
else:
    print("Mark is invalid")
