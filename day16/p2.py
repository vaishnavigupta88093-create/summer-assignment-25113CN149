n=int(input("enter your array elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("enter your elements:")))

max_count=0
max_element=arr[0]

for i in range(n):
    count=0

    for j in range(n):
        if arr[i]==arr[j]:
            count+=1

    if count>max_count:
             max_count=count
             max_element=arr[i]
    
print("elements with max frequency",max_element)   
print("count",max_count)             
