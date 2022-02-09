
# Author : Jeff Odhiambo
# Date written : Feb, 09 2020
# About : This is an implementation of a code that request for a number and check wether its fibonacci or not
# Approach 1:  Request for a number and store in a variale, generate series of fibonacci upto the number entered 
#             by the user and compare if any of them matches the generated numbers
#             If they match then it is else it is not.

print("\n   CHECK FOR FIBONACCI\n--------------------------\n")
num = int(input("[+]Enter a number >>> "))
a = 0
b = 1
sum = 1
if num < 0:
    print("Invalid input, try a number greater than or equal to 0!!!")
elif num == 0 or num == 1:
    print(f"{num} is a fibonacci number\n")
else:
    while sum < num:
        b = a
        a = sum
        sum = a + b
    if sum == num:
        print(f"{num} is a fibonacci number\n")
    else:
        print(f"{num} is not a fibonacci number\n")
