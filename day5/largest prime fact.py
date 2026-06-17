num=int(input("enter your number:"))

largest=0
for i in range(2,num+1):

    if num%i==0:

        prime=True

        for j in range(1,i):
            if i%j==0:
                prime==False
                break
        if prime:
                largest=i

print("Largest Prime Factor is:", largest)