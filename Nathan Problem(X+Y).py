# Twenty random cards are placed in a row all face down. A turn consists of taking two adjacent cards where the left one is face up and the right one can be face up or face down and flipping then both. Show that this process must terminate. (With all the cards facing up).

# let  face up --> 0
# let face down --> 1

def transform(b):
    for i in range(len(b)-1):
        if b[i] == '1':
            b[i] = '0'
            if b[i+1] == '0':
                b[i+1] = '1'
            else:
                b[i+1] = '0'
    return b
            
if __name__ == '__main__':
    a = list('1110101001111100101010')
    print(a)
    # sending copy of 'a' so that value of 'a' will not change
    while a != transform(a.copy()):
        a = transform(a.copy())
    print(a)