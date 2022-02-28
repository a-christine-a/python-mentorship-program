
#In this programm we will be checking for years that is Equals to or greator than 1600

print("\n=============== [CHECK LEAP YEAR] ===============")
print("\n1. Print Leap Years in a given range")
print("2. Check If a given year is a leap year")
print("\n==================== [ END ] ====================")

choice = int(input("[+]Select an Option >>> "))
leap_years = []
non_leap_years = []
if choice == 1:
    print("\n============ [ CKECK IN A GIVEN RANGE ] ===============")
    start_year = int(input("[+]Enter the first year in the range >>> "))
    last_year = int(input("[+]Enter the last year in the range >>> "))
    for i in range(start_year,last_year):
        if (i%4==0 and i%100!=0) or i%400==0:
            leap_years.append(i)
        else:
            non_leap_years.append(i)
    if leap_years:
        print(f"\nIn the provided range, {leap_years} are Leap Years")
    else:
        print("No leap year found in the range")
    if non_leap_years:
        print(f"\nIn the provided range, {non_leap_years} are Non-Leap Years")
    else:
        print("No leap year found")    
elif choice == 2:
    print("\n=========== [ CHECK A SPECIFIC YEAR ] ==============")
    year = int(input("[+]Enter the year to be checked >>> "))
    if year%4 == 0:
        if year%100 != 0:
            print(f"\t\t{year} is a leap Year")
    elif year%400 == 0:
        print(f"\t\t{year} is a lear year")
    else:
        print(f"\t\t{year} is not a leap year")
else:
    print("\t\tInvalid Option, Try a with 1 or 2")