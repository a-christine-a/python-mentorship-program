# python-mentorship-program

This repository contains the various projects that I did during a mentorship program organised by [LUX Academy](https://github.com/Lux-tech-Academy-Boot-Camp)
The repository contains 3 main folders name `week 1`, `week 2` and `week 3`

## Week 1
This folder contains the week one project where we were required to write a program that take input from the user and checks if a number is a Fibonacci or not.
This was implements in two ways:
- First one made use of condition statement and loop to determine if a number is Fibonacci or not.
- In second file I used a Mathematics formula that can help determine if a number is Fibonacci or not.
After executing the command the first output will be similar to as below
If a number is a Fibonacci
```
┌──(jeff㉿kali)-[~/Desktop/python mentorship program/Week 1]
└─$ python3 Fibonacci_1.py                       
   CHECK FOR FIBONACCI
--------------------------

[+]Enter a number >>> 13
13 is a fibonacci number
```
If number is not a Fibonacci
```
┌──(jeff㉿kali)-[~/Desktop/python mentorship program/Week 1]
└─$ python3 Fibonacci_1.py
   CHECK FOR FIBONACCI
--------------------------

[+]Enter a number >>> 7
7 is not a fibonacci number
```
## Week 2 
This folder contains week Two project where we were required to write a program to check if a year is a leap year or not. Here we also used conditional statements such as if and elif.
After executing the command the first output will be similar to as below
```
┌──(jeff㉿kali)-[~/Desktop/python mentorship program/Week 2]
└─$ python3 check_leap_year.py

=============== [CHECK LEAP YEAR] ===============

1. Print Leap Years in a given range
2. Check If a given year is a leap year

==================== [ END ] ====================
[+]Select an Option >>> 1

============ [ CKECK IN A GIVEN RANGE ] ===============
[+]Enter the first year in the range >>> 2011
[+]Enter the last year in the range >>> 2017

In the provided range, [2012, 2016] are Leap Years
In the provided range, [2011, 2013, 2014, 2015] are Non-Leap Years
```
Or
```
┌──(jeff㉿kali)-[~/Desktop/python mentorship program/Week 2]
└─$ python3 check_leap_year.py

=============== [CHECK LEAP YEAR] ===============

1. Print Leap Years in a given range
2. Check If a given year is a leap year

==================== [ END ] ====================
[+]Select an Option >>> 2

=========== [ CHECK A SPECIFIC YEAR ] ==============
[+]Enter the year to be checked >>> 2005
                2005 is not a leap year
```

## Week 3
For week 3 project we were required to develop a instagram video and image downloader, where i took 2 approaches.

### Command line based
In this approach, a user is prompted to enter URL through the terminal as shown below, then thereafter all the links to the associated media files are returned which are then used to download the images and videos. File name is `test.py`
```
┌──(jeff㉿kali)-[~/Desktop/python mentorship program/Week 3/Instagram_Video_downloader]
└─$ python3 test.py       
Enter Instagram url : https://www.instagram.com/p/CZJ_8eZqxGe/
Detected pictures : 
['https://instagram.fmba2-1.fna.fbcdn.net/v/t51.2885-15/272456987_498829895004603_7573574216291002592_n.jpg?stp=dst-jpg_e15&_nc_ht=instagram.fmba2-1.fna.fbcdn.net&_nc_cat=103&_nc_ohc=8C66t6bpVWIAX-V45UY&edm=AABBvjUBAAAA&ccb=7-4&oh=00_AT9EZTW_hQHZ4JKjTpojbCfY8mYmTBwZnEn0JVD1SDqyBQ&oe=6224B408&_nc_sid=83d603']
```
### Web Based
On the web based I used Django framework to implement the same.
To run it, 
1. Create a folder - `mkdir instagarm`
2. cd into the folder - `cd instagram`
3. Create virtual environment - `virtualenv my_env`
4. Activate the virtual environment - `source my_env/bin/activate` for UNIX operating systems
5. Clone the project - `git clone https://github.com/killall-nano/python-mentorship-program.git`
6. Cd into project folder - `cd python-mentorship-program/Week 3/Instagram_Video_downloader`
7. Install the requirements in the requirements.txt file - `pip install -r requirements.txt`
8. Run the server and test - `python3 manage.py runserver`

Alternatively you can visit the deployed version on [Pythonanywhere](https://smarttech.pythonanywhere.com/)
