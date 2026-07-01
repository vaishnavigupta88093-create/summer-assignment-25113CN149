
n1=int(input("enter size of arrays :"))
arr1 = []

for i in range(n1):
    arr1.append(int(input("Enter element: ")))

n2=int(input("enter size of arrays :"))
arr2=[]

for i in range(n2):
    arr2.append(int(input("enter your elements:")))



print("common elements in two arrays are:")
for i in arr1:
    if i in arr2:
        print(i)