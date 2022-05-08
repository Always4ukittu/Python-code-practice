# reading the text file
with open('currencyData.txt') as f:
    lines = f.readlines()  # read all the lines of the files and store in the list 

# Storing the currncy name and values
currencyDisc = {}
for line in lines:
    parsed = line.split('\t')
    currencyDisc[parsed[0]] = float(parsed[1])
print(currencyDisc)

# user Input
userInp = int(input("Enter the Amount: "))
# Asking for currency to conver
for cur in currencyDisc.keys():
    print(cur)
currency = input('Enter the currency, in which you want to convert from the option given above..\n')

# Changing the currency
if currency in currencyDisc.keys():
    print(f"INR {userInp} in equal to {userInp*currencyDisc[currency]} in {currency}")
else:
    print('Invalid Choice')