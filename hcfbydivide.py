print("Enter two number")
a=int(input("enter first num: "))
b=int(input("enter second num: "))
while a%b!=0:
    rem=a%b
    a=b
    b=rem
print("HCF is: ",b)