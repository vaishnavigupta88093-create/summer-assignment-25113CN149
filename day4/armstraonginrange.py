start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):

    total = 0

    for digit in str(num):
        total = total + int(digit) ** 3

    if total == num:
        print(num)
 