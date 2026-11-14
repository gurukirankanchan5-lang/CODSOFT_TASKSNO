num1=int(input("Enter the number 1:  "))
num2=int(input("Enter the number 2:  "))

print("-------------")
print("1.ADD")
print("2.SUBSTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("-------------")

ch=int(input("enter your choice:  "))

if ch==1:
    print("Result is: ",num1+num2)
elif ch==2:
    print("Result is: ",num1-num2)
elif ch==3:
     print("Result is: ",num1*num2)
else:
    if num2!=0:
        print("Result is:  ",num1/num2)
    else:
        print("Cannot Divide by Zero")

