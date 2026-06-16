a=int(input("enter your maths marks:"))
b=int(input("enter your english marks:  "))
c=int(input("enter your physics marks:"))
total=a+b+c
percentage=(total/300)*100
print("percentage is ",percentage)
if percentage >= 40 and a >= 33 and b >= 33 and c >= 33:
    print("Pass")
else:
    print("Fail")
