# Q6) Write a Python function to calculate the factorial of a number (a non-negative integer). The function 
#accepts the number as an argument.

num1=int(input("Enter Number : "))

def fun(num1):
    i=1
    fact=1
    while i<=num1:
        fact=fact*i
        i=i+1

    print(f"factorial of {num1} is {fact}")


fun(num1)