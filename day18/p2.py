n = int(input("Enter array size: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter element: ")))

arr.sort(reverse=True)      # Binary search requires a sorted array
print("Sorted array:", arr)