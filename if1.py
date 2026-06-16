a=int(input("enter first number:"))
b=int(input("enter second number:"))
 
c=int(input("enter third number:"))
d=int(input("enter fourth number:"))

if a >= b and a >= c and a >= d:
    print("Greatest number is:", a)
elif b >= a and b >= c and b >= d:
    print("Greatest number is:", b)
elif c >= a and c >= b and c >= d:
    print("Greatest number is:", c)
else:
    print("Greatest number is:", d)