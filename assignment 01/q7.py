# Q7Using for loop, write and run a Python program to find factorial from 0 to 10.


def fun(num1):
    fact = 1; 
    count = 1;
    while (count < num1):
        fact = fact * count;
        count = count + 1
    print(f"The factorail of : {fact}")

num1=0
for count in range(10):
    num1 = num1 + 1
    fun(num1)
    
