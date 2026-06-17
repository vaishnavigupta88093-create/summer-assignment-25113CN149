start=int(input("enter your start number:"))
end=int(input("enter your end number:"))

for num in range(start, end + 1):

    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            print(num)