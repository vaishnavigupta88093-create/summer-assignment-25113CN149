n1 = int(input("Enter size of array: "))

arr1 = []

for i in range(n1):
    arr1.append(int(input("Enter element: ")))

n2=int(input("enter size of arrays :"))
arr2=[]

for i in range(n2):
    arr2.append(int(input("enter your elements:")))
arr3=arr1+arr2
print("merged arrays ",arr3)

