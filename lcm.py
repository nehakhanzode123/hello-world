print("enter two num")
a=int(input("enter first num"))
b=int(input("enter second num"))
for m in range(1,a*b+1):
    if m%a==0 and m%b==0:
        print("lcm is:",m)
        break