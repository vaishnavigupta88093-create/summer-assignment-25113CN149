n=int(input("enter your element of array :"))

arr=[]

for i in range(n):
    element = int(input("enter your elements:"))
    arr.append(element)
even=0
odd=0
for i in arr:
    if i%2==0:
        even+=1
        print("even")
    else:
        print("odd")
        odd+=1
print("even",even)
print("odd",odd)
    