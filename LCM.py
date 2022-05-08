# Method 1 to find LCM
a = int(input("Eneter the first number:"))
b = int(input("Eneter the second number:"))


maxnum = max(a, b)

while(True):
    if(maxnum%a==0 and maxnum%b==0):
        break
    maxnum = maxnum+1
print(f"The LCM of {a} and {b} is : {maxnum}")