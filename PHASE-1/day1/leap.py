''' CHECKING IF A GIVEN YEAR IS LEAP OR NOT CONDTIONS 
IF YEAR IS DIVISIBLE BY 4 AND NOT BY 100 OR IF IT IS DIVISIBLE BY 400 THEN ITS LEAP YEAR'''

year=int(input("Enter  a  year :: "))

if (year%4==0 and year%100!=0) or year%400==0:
    print("LEAP YEAR !!!!!")
else:
    print("NOT A LEAP YEAR !!!!")
