
def armstrong(num):
   

    num=int(input("enter your number:"))

    sum=0

    for digit in str(num):
         sum=sum+int(digit)**3
    if sum==num:
        print("armstrong number")
    else:
        print("not armstrong number")    
print(125)
 