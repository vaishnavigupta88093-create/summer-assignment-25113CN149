num=int(input("enter your num:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if num==sum:
        print("perfect number")
else:
        print("not a perfect number")


