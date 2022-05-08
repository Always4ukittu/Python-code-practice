# 1. Find the factorial of number
# 2. Find the trailing zeros


def factorial(num):
    if num == 0 or num ==1:
        return 1
    else:
        return num * factorial(num - 1)

def factorialTrailingZeros(num):
    pass

if __name__ == '__main__':
    num = int(input("Enter the number: "))
    fac = factorial(num)
    print(f"The Factorial is {fac}")
