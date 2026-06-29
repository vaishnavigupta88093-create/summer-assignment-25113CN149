n=int(input("enter your array elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("enter your elements:")))
key=int(input("enter your missing elements:"))    
found=False

for i in range(n):
    if arr[i]==key:
        print("element found at index",i)
        found=True
        break
if not found:
    print("elements not found")
