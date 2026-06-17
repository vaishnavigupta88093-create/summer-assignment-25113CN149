a=int(input("enter your first num:"))
b=int(input("enter your second num:"))

gcd=1

for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i

LCM = (a * b) // gcd
print(f"this is your lcm:{LCM}")