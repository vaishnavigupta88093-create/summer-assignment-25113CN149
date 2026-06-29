n=int(input("enter your array elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("enter your elements:")))
key=int(input("enter your missing elements:"))    
count=0
for i in range(n):
    if i==key:
        count=1
print("frequency",count)
