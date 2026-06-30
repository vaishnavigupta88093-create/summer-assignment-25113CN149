n = int(input("Enter size of array: "))

arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

print("Duplicate elements are:")

for i in range(n):
    for j in range(i + 1, j):
        if arr[i] == arr[j]:
         arr.remove(arr[i])
print(arr[i])
    