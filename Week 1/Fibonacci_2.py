
# Author : Jeff Odhiambo
# Date written : Feb, 09 2020
# About : This is an implementation of a code that request for a number and check wether its fibonacci or not
# Approach 2: Request for a number and store in a variale the use the principle below to check if the number is a fibonacci or not using factions
#            "A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square"
import math

def perfectsq(num):
    num_sqrt = int(math.sqrt(num))
    #Checking if number is a perfect square
    if num_sqrt * num_sqrt == num:
        #number is perfect square
        return 1
    else:
        #number is not a perfect square
        return 0

def is_fibonacci(num):
    if perfectsq(5*num*num + 4) or perfectsq(5*num*num - 4):
        print(f"{num} is a fibonacci number\n")
    else:
        print(f"{num} is not a fibonacci number\n")

print("\n   CHECK FOR FIBONACCI\n--------------------------\n")

num = int(input("[+]Enter a number >>> "))

if num < 0:
    print("Invalid input, try a number greater than or equal to 0!!!")
elif num == 0 or num == 1:
    print(f"{num} is a fibonacci number\n")
else:
    #call the fabonacci function to check if the number is or not
    is_fibonacci(num)
