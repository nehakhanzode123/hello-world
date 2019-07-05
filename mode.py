n=int(input("how many num"))
nums=[]
for i in range(n):
    a=int(input("enter num: "))
    nums.append(a)

differentnums={}
for x in nums:
    if x not in differentnums:
        differentnums[x]=1
    else:
        differentnums[x]+1

print("num with their freq")
maxfreq=0
mode=0
for d in differentnums.keys():
    print(d, " comes ", differentnums[d], " times")
    if differentnums[d]>maxFreq:
        maxFreq=differentnums[d]
        mode=d
print("Mode is ",mode)