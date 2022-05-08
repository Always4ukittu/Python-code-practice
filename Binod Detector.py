import os

# Detext binod in files and folders
def findbinod(filename):
    with open(filename,'r') as f:
        line = f.read()
    if 'binod' in line.lower():
        return True
    else:
        return False     


if __name__ == '__main__':
    dir = os.listdir()
    times = 0
    for list in dir:
        if(list.endswith('txt')):
            result = findbinod(list)
            if(result):
                times += 1
                print(f"Binod found in '{list}'..........................")
            else:
                print(f"Binod not found in '{list}'")

print("############################################")
print(f"Binod found in {times} files")