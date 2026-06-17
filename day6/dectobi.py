n=int(input("enter your number:"))
binary=""
while n>0:
    rem=n%2
    binary=str(rem)+binary
    n=n//2

print(f"this your conversion from decimal to binary:{binary}")    