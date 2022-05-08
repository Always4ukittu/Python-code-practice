# Write a python program which will keep adding a stream of numbers inputted bu the uiser. The adding stops as soon as user presses q key on the keyboard.

total = 0
itemDisc ={}
while(True):
    itemName = input("Enter the items Name or q to quit: ")
    if(itemName != 'q'):
        itemPrice = int(input("Price: "))
        itemDisc[itemName] = itemPrice
        total += itemPrice
        print(f"Order total so far: {total} ")
    else:
        for key in itemDisc:
            print(key, ':' , itemDisc[key])
        print(f"Total amount to be paid to the seller is INR {float(total)} Thanks for shopping with us.")
        break
