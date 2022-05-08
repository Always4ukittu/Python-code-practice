# Finding HCF or GCD of number

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if(a>b):
    num = b
else:
    num = a
# finding highest common factor which divide both the number
for i in range(1, num+1):
    if(a%i==0 and b%i==0):
        hcf = i

print(f"HCF of {a} and {b} is {hcf}")