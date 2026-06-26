n=int(input("enter your element of array :"))

arr=[]

for i in range(n):
    element = int(input("enter your elements:"))
    arr.append(element)
print(max(arr))
print(min(arr))